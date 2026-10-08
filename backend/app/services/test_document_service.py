from backend.app.db.database import SessionLocal
from backend.app.models.course import Course
from backend.app.services.document_service import create_document


db = SessionLocal()

try:
    course = Course(
        title="Machine Learning Fundamentals",
        description="Sample course for testing document ingestion.",
    )

    db.add(course)
    db.commit()
    db.refresh(course)

    print(f"Course created: {course.id}")

    document = create_document(
        db=db,
        course_id=course.id,
        title="Sample Course Material",
        file_type="pdf",
        source="sample.pdf",
    )

    print(f"Document created: {document.id}")

finally:
    db.close()