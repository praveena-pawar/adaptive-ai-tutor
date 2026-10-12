from sentence_transformers import util

from backend.app.services.embedding_service import generate_embedding


question = "How do neural networks improve their predictions?"

chunks = {
    "A": "Neural networks learn by adjusting their weights.",
    "B": "Plants use sunlight to produce food through photosynthesis.",
    "C": "Machine learning models improve by minimizing their prediction errors.",
}

question_embedding = generate_embedding(question)

for label, text in chunks.items():
    chunk_embedding = generate_embedding(text)

    similarity = util.cos_sim(
        question_embedding,
        chunk_embedding,
    ).item()

    print(f"Chunk {label}: {similarity:.4f} | {text}")