from backend.app.services.pdf_processor import process_pdf


pdf_path = "sample.pdf"

chunks = process_pdf(pdf_path)

for chunk in chunks:
    print(f"Chunk index: {chunk['chunk_index']}")
    print(f"Page number: {chunk['page_number']}")
    print(f"Content: {chunk['content']}")
    print("-" * 60) 