from sqlalchemy.orm import Session

from backend.app.models.document import Document


def create_document(
    db: Session,
    course_id: int,
    title: str,
    file_type: str,
    source: str | None = None,
) -> Document:
    document = Document(
        course_id=course_id,
        title=title,
        file_type=file_type,
        source=source,
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return document