import asyncio

from src.datasets import (
    load_all_datasets
)

from src.evaluator import (
    Evaluator
)

from src.benchmark import (
    BenchmarkRunner
)


async def main():

    datasets = load_all_datasets()

    benchmark = BenchmarkRunner(
        datasets=datasets,
        evaluator=Evaluator
    )

    scores = await (
        benchmark.evaluate_all()
    )

    print("\nScores:\n")

    for task, score in scores.items():

        print(
            task,
            round(score, 3)
        )


asyncio.run(main())