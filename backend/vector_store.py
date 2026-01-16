# import os
# os.environ["TRANSFORMERS_NO_TF"] = "1"
# os.environ["TRANSFORMERS_NO_FLAX"] = "1"


# from sentence_transformers import SentenceTransformer
# from sklearn.neighbors import NearestNeighbors
# import numpy as np

# # Load embedding model (PyTorch only)
# model = SentenceTransformer("all-MiniLM-L6-v2")

# documents = []
# embeddings = None
# nn_model = None

# def add_chunks_to_vector_db(chunks):
#     global embeddings, nn_model

#     new_embeddings = model.encode(chunks)

#     if embeddings is None:
#         embeddings = new_embeddings
#     else:
#         embeddings = np.vstack((embeddings, new_embeddings))

#     documents.extend(chunks)

#     nn_model = NearestNeighbors(n_neighbors=3, metric="cosine")
#     nn_model.fit(embeddings)

# def search_similar_chunks(query, k=3):
#     query_embedding = model.encode([query])
#     distances, indices = nn_model.kneighbors(query_embedding, n_neighbors=k)

#     return [documents[i] for i in indices[0]]


# vector_store.py
import os
os.environ["TRANSFORMERS_NO_TF"] = "1"
os.environ["TRANSFORMERS_NO_FLAX"] = "1"

from sentence_transformers import SentenceTransformer
from sklearn.neighbors import NearestNeighbors
import numpy as np

# Load embedding model (PyTorch only)
model = SentenceTransformer("all-MiniLM-L6-v2")

# Global storage
documents = []
embeddings = None
nn_model = None

def add_chunks_to_vector_db(chunks):
    """
    Add new text chunks to the vector database.
    Updates embeddings and fits the NearestNeighbors model.
    """
    global embeddings, nn_model, documents

    if not chunks:
        return  # Do nothing if chunks list is empty

    # Encode the chunks
    new_embeddings = model.encode(chunks)

    if embeddings is None:
        embeddings = new_embeddings
    else:
        embeddings = np.vstack((embeddings, new_embeddings))

    # Add chunks to the documents list
    documents.extend(chunks)

    # Fit the NearestNeighbors model
    nn_model = NearestNeighbors(n_neighbors=min(3, len(documents)), metric="cosine")
    nn_model.fit(embeddings)


def search_similar_chunks(query, k=3):
    """
    Search for the top-k most similar chunks to the query.
    Returns a list of strings (chunks). Returns empty list if no data.
    """
    global nn_model, documents

    if nn_model is None or not documents:
        # Vector DB not initialized yet
        return []

    query_embedding = model.encode([query])
    k = min(k, len(documents))  # Avoid asking for more neighbors than available
    distances, indices = nn_model.kneighbors(query_embedding, n_neighbors=k)

    # Return the matched chunks
    return [documents[i] for i in indices[0]]
