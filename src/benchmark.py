import asyncio

from src.openrouter_client import (
    ask_llm
)


class BenchmarkRunner:

    def __init__(
        self,
        datasets,
        evaluator
    ):

        self.datasets = datasets
        self.evaluator = evaluator

    async def evaluate_task(
        self,
        task_name
    ):

        task_data = self.datasets[
            task_name
        ]

        scores = []

        for item in task_data:

            prediction = await ask_llm(
                item["question"]
            )

            score = await self.evaluator.score(
                item["question"],
                prediction,
                item["answer"]
            )

            scores.append(score)

        return {
            "task": task_name,
            "score": sum(scores)
            / max(len(scores), 1)
        }

    async def evaluate_all(self):

        tasks = [

            self.evaluate_task(
                task_name
            )

            for task_name
            in self.datasets
        ]

        results_list = await asyncio.gather(
            *tasks
        )

        results = {}

        for result in results_list:
            results[
                result["task"]
            ] = result["score"]

        return results