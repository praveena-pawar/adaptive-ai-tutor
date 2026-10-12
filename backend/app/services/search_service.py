from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.app.models.document_chunk import DocumentChunk
from backend.app.services.embedding_service import generate_embedding


def search_similar_chunks(
    db: Session,
    query: str,
    limit: int = 5,
) -> list[dict]:
    query_embedding = generate_embedding(query)

    distance = DocumentChunk.embedding.cosine_distance(query_embedding)

    statement = (
        select(DocumentChunk, distance.label("distance"))
        .where(DocumentChunk.embedding.is_not(None))
        .order_by(distance)
        .limit(limit)
    )

    results = db.execute(statement).all()

    return [
        {
            "chunk_id": chunk.id,
            "document_id": chunk.document_id,
            "content": chunk.content,
            "page_number": chunk.page_number,
            "similarity": 1 - distance_value,
        }
        for chunk, distance_value in results
    ]