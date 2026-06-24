import re


class Evaluator:

    @staticmethod
    def normalize(text):

        text = text.lower()

        text = re.sub(
            r"\s+",
            " ",
            text
        )

        return text.strip()

    @staticmethod
    def exact_match(
        prediction,
        answer
    ):

        prediction = Evaluator.normalize(
            prediction
        )

        answer = Evaluator.normalize(
            answer
        )

        return int(
            answer in prediction
        )

    @staticmethod
    def score(
        prediction,
        answer
    ):

        return Evaluator.exact_match(
            prediction,
            answer
        )