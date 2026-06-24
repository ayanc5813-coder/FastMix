import numpy as np


def weighted_score(
    scores,
    alpha
):

    score_vector = np.array(
        list(scores.values())
    )

    alpha = np.array(alpha)

    return float(
        np.dot(
            score_vector,
            alpha
        )
    )