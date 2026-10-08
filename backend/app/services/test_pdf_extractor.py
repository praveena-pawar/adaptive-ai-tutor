from backend.app.services.pdf_extractor import extract_pdf_text


pdf_path = "sample.pdf"

pages = extract_pdf_text(pdf_path)

for page in pages:
    print(f"Page {page['page_number']}")
    print(page["text"][:500])
    print("-" * 50)