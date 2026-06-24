from src.optimizer import (
    FastMixOptimizer
)

optimizer = FastMixOptimizer(
    num_tasks=5,
    learning_rate=0.1
)

scores = [
    0.8,
    0.9,
    0.4,
    0.2,
    0.6
]

for i in range(10):

    alpha = optimizer.step(
        scores
    )

    print(
        i,
        alpha
    )