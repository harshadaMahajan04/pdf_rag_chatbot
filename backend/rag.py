# rag.py
from vector_store import search_similar_chunks

def generate_answer(context_chunks, question):
    """
    Simple extractive RAG:
    - Finds relevant chunks
    - Returns them as the answer
    """

    if not context_chunks:
        return "I don't know. The answer is not present in the document."

    # Join top chunks into a readable answer
    answer = " ".join(context_chunks)

    return answer


print("rag.py loaded successfully")
print(dir())
