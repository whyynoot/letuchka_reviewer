import numpy as np

def cosine_similarity(v1, v2):
    dot_product = np.dot(v1, v2)
    norm_vector1 = np.linalg.norm(v1)
    norm_vector2 = np.linalg.norm(v2)

    if norm_vector1 == 0 or norm_vector2 == 0:
        return 0  # Handle division by zero

    similarity_score = dot_product / (norm_vector1 * norm_vector2)
    return similarity_score