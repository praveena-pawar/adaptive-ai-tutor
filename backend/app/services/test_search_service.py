from backend.app.db.database import SessionLocal
from backend.app.services.search_service import search_similar_chunks


def main():
    query = "How does gradient descent help a model learn?"

    with SessionLocal() as db:
        results = search_similar_chunks(
            db=db,
            query=query,
            limit=3,
        )

    print(f"\nQuestion: {query}\n")
    print("Most relevant textbook passages:\n")

    for result in results:
        print(f"Chunk ID: {result['chunk_id']}")
        print(f"Document ID: {result['document_id']}")
        print(f"Page: {result['page_number']}")
        print(f"Similarity: {result['similarity']:.4f}")
        print(f"Content: {result['content']}")
        print("-" * 60)


if __name__ == "__main__":
    main()