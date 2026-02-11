from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")


def semantic_score(text1, text2):

    if not text1 or not text2:
        return 0.0

    emb1 = model.encode([text1])
    emb2 = model.encode([text2])

    score = cosine_similarity(emb1, emb2)[0][0]

    return round(float(score * 100), 2)
