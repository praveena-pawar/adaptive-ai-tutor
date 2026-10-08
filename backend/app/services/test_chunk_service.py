from backend.app.db.database import SessionLocal
from backend.app.services.pdf_processor import process_pdf
from backend.app.services.chunk_service import create_document_chunks


db = SessionLocal()

try:
    chunks = process_pdf("sample.pdf")

    document_chunks = create_document_chunks(
        db=db,
        document_id=1,
        chunks=chunks,
    )

    for chunk in document_chunks:
        print(f"Chunk ID: {chunk.id}")
        print(f"Document ID: {chunk.document_id}")
        print(f"Chunk Index: {chunk.chunk_index}")
        print(f"Page Number: {chunk.page_number}")
        print(f"Content: {chunk.content}")
        print("-" * 60)

finally:
    db.close()