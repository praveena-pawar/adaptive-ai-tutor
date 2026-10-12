from backend.app.services.embedding_service import generate_embedding


text = "Neural networks learn by adjusting their weights."

embedding = generate_embedding(text)

print("Input text:", text)
print("Embedding dimensions:", len(embedding))
print("First five values:", embedding[:5])