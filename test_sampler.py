from src.datasets import (
    load_all_datasets
)

from src.sampler import (
    MixtureSampler
)


datasets = load_all_datasets()

alpha = [
    0.20,
    0.20,
    0.20,
    0.20,
    0.20
]

sampler = MixtureSampler(
    datasets,
    alpha
)

batch = sampler.sample_batch(
    batch_size=10
)

for item in batch:

    print(item)