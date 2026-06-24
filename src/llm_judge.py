import re
import hashlib

from src.judge_client import (
    judge_completion
)

from config.settings import (
    JUDGE_MAX_SCORE
)


class LLMJudge:

    def __init__(self):

        self.cache = {}

    def _cache_key(
        self,
        question,
        gold,
        prediction
    ):

        text = (
            question
            + gold
            + prediction
        )

        return hashlib.md5(
            text.encode("utf-8")
        ).hexdigest()

    async def score(
        self,
        question,
        gold_answer,
        prediction
    ):

        cache_key = self._cache_key(
            question,
            gold_answer,
            prediction
        )

        if cache_key in self.cache:

            return self.cache[
                cache_key
            ]

        prompt = f"""
You are an expert benchmark evaluator.

Evaluate the candidate answer.

QUESTION:
{question}

REFERENCE ANSWER:
{gold_answer}

CANDIDATE ANSWER:
{prediction}

Scoring Rubric:

10 = Perfect

8-9 = Correct with minor issues

6-7 = Mostly correct

4-5 = Partially correct

1-3 = Weak answer

0 = Completely incorrect

Return ONLY:

SCORE: <number>

Example:

SCORE: 8
"""

        response = await (
            judge_completion(
                prompt
            )
        )

        score = self._extract_score(
            response
        )

        self.cache[
            cache_key
        ] = score

        return score

    def _extract_score(
        self,
        text
    ):

        match = re.search(
            r"(\d+(\.\d+)?)",
            text
        )

        if not match:

            return 0.0

        value = float(
            match.group(1)
        )

        value = min(
            value,
            JUDGE_MAX_SCORE
        )

        value = max(
            value,
            0
        )

        return (
            value
            /
            JUDGE_MAX_SCORE
        )