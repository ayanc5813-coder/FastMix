import random
import numpy as np


class MixtureSampler:

    def __init__(
        self,
        datasets,
        alpha
    ):

        self.datasets = datasets

        self.alpha = np.array(
            alpha,
            dtype=float
        )

        self.tasks = list(
            datasets.keys()
        )

    def update_alpha(
        self,
        alpha
    ):

        alpha = np.array(
            alpha,
            dtype=float
        )

        alpha = alpha / alpha.sum()

        self.alpha = alpha

    def get_alpha(self):

        return self.alpha

    def sample_task(self):

        task = np.random.choice(
            self.tasks,
            p=self.alpha
        )

        return task

    def sample_example(self):

        task = self.sample_task()

        example = random.choice(
            self.datasets[task]
        )

        return {
            "task": task,
            "question": example["question"],
            "answer": example["answer"]
        }

    def sample_batch(
        self,
        batch_size=32
    ):

        batch = []

        for _ in range(batch_size):

            batch.append(
                self.sample_example()
            )

        return batch