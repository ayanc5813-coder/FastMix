import asyncio

from src.datasets import (
    load_all_datasets
)

from src.evaluator import (
    Evaluator
)

from src.fastmix_runner import (
    FastMixRunner
)


async def main():

    datasets = (
        load_all_datasets()
    )

    runner = (
        FastMixRunner(
            datasets,
            Evaluator
        )
    )

    history = await (
        runner.run()
    )

    df = history.dataframe()

    print(df.head())


asyncio.run(main())