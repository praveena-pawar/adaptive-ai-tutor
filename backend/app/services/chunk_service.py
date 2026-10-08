from sqlalchemy.orm import Session

from backend.app.models.document_chunk import DocumentChunk


def create_document_chunks(
    db: Session,
    document_id: int,
    chunks: list[dict],
) -> list[DocumentChunk]:
    document_chunks = []

    for chunk in chunks:
        document_chunk = DocumentChunk(
            document_id=document_id,
            content=chunk["content"],
            chunk_index=chunk["chunk_index"],
            page_number=chunk["page_number"],
        )

        db.add(document_chunk)
        document_chunks.append(document_chunk)

    db.commit()

    for document_chunk in document_chunks:
        db.refresh(document_chunk)

    return document_chunks