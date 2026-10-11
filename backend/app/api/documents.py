from fastapi import APIRouter, File, HTTPException, UploadFile
from sqlalchemy.exc import SQLAlchemyError

from backend.app.db.database import SessionLocal
from backend.app.services.chunk_service import create_document_chunks
from backend.app.services.document_service import create_document
from backend.app.services.file_storage import save_temp_file
from backend.app.services.pdf_processor import process_pdf

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="A filename is required.",
        )

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported.",
        )

    temp_path = None
    db = SessionLocal()

    try:
        temp_path = save_temp_file(file.file)

        chunks = process_pdf(str(temp_path))

        if not chunks:
            raise HTTPException(
                status_code=400,
                detail="The PDF contains no extractable text.",
            )

        document = create_document(
            db=db,
            course_id=1,
            title=file.filename,
            file_type="pdf",
            source=file.filename,
        )

        document_chunks = create_document_chunks(
            db=db,
            document_id=document.id,
            chunks=chunks,
        )

        return {
            "document_id": document.id,
            "filename": file.filename,
            "total_chunks": len(document_chunks),
            "message": "PDF processed and saved successfully",
        }

    except HTTPException:
        db.rollback()
        raise

    except SQLAlchemyError as exc:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Failed to save the PDF to the database.",
        ) from exc

    finally:
        db.close()

        if temp_path is not None:
            temp_path.unlink(missing_ok=True)

        await file.close()