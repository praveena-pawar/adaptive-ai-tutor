from backend.app.services.pdf_extractor import extract_pdf_text
from backend.app.services.text_chunker import chunk_text


def process_pdf(file_path: str) -> list[dict]:
    pages = extract_pdf_text(file_path)

    chunks = []
    chunk_index = 0

    for page in pages:
        page_chunks = chunk_text(page["text"])

        for chunk in page_chunks:
            chunks.append(
                {
                    "content": chunk,
                    "chunk_index": chunk_index,
                    "page_number": page["page_number"],
                }
            )

            chunk_index += 1

    return chunks