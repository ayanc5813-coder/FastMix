from src.evaluator import Evaluator
from src.llm_judge import LLMJudge


class HybridEvaluator:

    def __init__(self):

        self.judge = LLMJudge()

    async def score(
        self,
        question,
        prediction,
        answer
    ):

        exact = Evaluator.score(
            prediction,
            answer
        )

        try:

            judge = await self.judge.score(
                question,
                answer,
                prediction
            )

        except Exception as e:

            print(
                f"Judge failed: {e}"
            )

            judge = exact

        final_score = (
            0.20 * exact
            +
            0.80 * judge
        )

        return final_score