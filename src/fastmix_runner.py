import asyncio

from src.benchmark import (
    BenchmarkRunner
)

from src.optimizer import (
    AdamAlphaOptimizer
)

from src.history import (
    OptimizationHistory
)

from config.settings import (
    TASKS,
    LEARNING_RATE,
    OPTIMIZATION_STEPS
)
from src.checkpoint import (
    CheckpointManager
)

from src.logger import (
    fastmix_logger
)


class FastMixRunner:

    def __init__(
        self,
        datasets,
        evaluator,

    ):

        self.datasets = datasets

        self.benchmark = (
            BenchmarkRunner(
                datasets,
                evaluator
            )
        )
        self.checkpoints = (
            CheckpointManager()
        )

        self.optimizer = (
            AdamAlphaOptimizer(
                num_tasks=len(TASKS),
                lr=LEARNING_RATE,
                temperature=1.2
            )
        )

        self.history = (
            OptimizationHistory()
        )

    async def run(self):

        start_iteration = (
            self.resume_latest()
        )

        for iteration in range(
                start_iteration,
                OPTIMIZATION_STEPS
        ):
            scores = await (
                self.benchmark
                .evaluate_all()
            )

            score_vector = [

                scores[t]

                for t in TASKS
            ]

            result = (
                self.optimizer.step(
                    score_vector
                )
            )

            alpha = result[
                "alpha"
            ]

            advantage = result[
                "advantage"
            ]

            self.history.add(
                iteration,
                alpha,
                scores,
                advantage
            )

            checkpoint_state = {

                "iteration":
                    iteration,

                "optimizer":
                    self.optimizer
                    .state_dict(),

                "history":
                    self.history.rows
            }

            self.checkpoints.save(

                f"iter_{iteration}.pkl",

                checkpoint_state
            )

            print(
                f"Iteration {iteration}"
            )

            print(
                alpha
            )
        self.history.save_csv(
            "history.csv"
        )

        return self.history

    def resume_latest(self):

        latest = (
            self.checkpoints
            .latest_checkpoint()
        )

        if latest is None:
            print(
                "No checkpoint found."
            )

            return 0

        checkpoint = (
            self.checkpoints
            .load(latest)
        )

        self.optimizer.load_state_dict(
            checkpoint[
                "optimizer"
            ]
        )

        self.history.rows = (
            checkpoint[
                "history"
            ]
        )

        print(
            f"Resumed from {latest}"
        )

        return (
                checkpoint[
                    "iteration"
                ] + 1
        )

    async def run_single_iteration(
            self,
            iteration
    ):

        scores = await (
            self.benchmark
            .evaluate_all()
        )

        score_vector = [

            scores[t]

            for t in TASKS
        ]

        result = (
            self.optimizer.step(
                score_vector
            )
        )

        alpha = result["alpha"]

        advantage = (
            result["advantage"]
        )

        self.history.add(
            iteration,
            alpha,
            scores,
            advantage
        )

        return {

            "iteration":
                iteration,

            "alpha":
                alpha.tolist(),

            "scores":
                scores
        }