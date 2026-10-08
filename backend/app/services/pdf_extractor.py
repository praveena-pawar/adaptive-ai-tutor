import pymupdf


def extract_pdf_text(file_path: str) -> list[dict]:
    pages = []

    with pymupdf.open(file_path) as document:
        for page_number, page in enumerate(document, start=1):
            text = page.get_text().strip()

            if not text:
                continue

            pages.append(
                {
                    "page_number": page_number,
                    "text": text,
                }
            )

    return pages