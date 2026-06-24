from src.metrics import (
    weighted_score
)

scores = {
    "reasoning": 0.8,
    "coding": 0.7,
    "math": 0.9,
    "memory": 0.4,
    "tools": 0.6
}

alpha = [
    0.2,
    0.2,
    0.2,
    0.2,
    0.2
]

print(
    weighted_score(
        scores,
        alpha
    )
)