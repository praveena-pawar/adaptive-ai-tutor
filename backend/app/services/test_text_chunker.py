from backend.app.services.text_chunker import chunk_text


text = """
Machine learning is a field of artificial intelligence.
Supervised learning uses labeled data.
Linear regression predicts continuous values.
Gradient descent minimizes a loss function.
"""


chunks = chunk_text(text, chunk_size=10, overlap=2)

for index, chunk in enumerate(chunks):
    print(f"Chunk {index}:")
    print(chunk)
    print("-" * 50)