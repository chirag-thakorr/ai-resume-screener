import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

index = None
resume_ids = []


def build_index(resumes):

    global index, resume_ids

    texts = [r.parsed_text for r in resumes]
    resume_ids = [r.id for r in resumes]

    embeddings = model.encode(texts)

    dim = len(embeddings[0])

    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype("float32"))


def search_similar(text, top_k=5):

    emb = model.encode([text]).astype("float32")

    D, I = index.search(emb, top_k)

    return [resume_ids[i] for i in I[0]]
