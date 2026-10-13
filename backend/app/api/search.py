from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from backend.app.db.database import SessionLocal
from backend.app.services.search_service import search_similar_chunks


router = APIRouter(
    prefix="/search",
    tags=["Semantic Search"],
)


class SearchRequest(BaseModel):
    query: str = Field(min_length=1, max_length=2000)
    limit: int = Field(default=5, ge=1, le=20)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/")
def search_documents(
    request: SearchRequest,
    db: Session = Depends(get_db),
):
    query = request.query.strip()

    if not query:
        raise HTTPException(
            status_code=422,
            detail="Search query cannot be empty.",
        )

    try:
        results = search_similar_chunks(
            db=db,
            query=query,
            limit=request.limit,
        )

        return {
            "query": query,
            "total_results": len(results),
            "results": results,
        }

    except SQLAlchemyError as exc:
        raise HTTPException(
            status_code=500,
            detail="Failed to search educational materials.",
        ) from exc