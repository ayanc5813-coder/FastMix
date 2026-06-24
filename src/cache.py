import hashlib


class JudgeCache:

    def __init__(self):

        self.cache = {}

    def key(
        self,
        question,
        answer
    ):

        text = (
            question +
            answer
        )

        return hashlib.md5(
            text.encode()
        ).hexdigest()

    def get(
        self,
        question,
        answer
    ):

        return self.cache.get(
            self.key(
                question,
                answer
            )
        )

    def set(
        self,
        question,
        answer,
        score
    ):

        self.cache[
            self.key(
                question,
                answer
            )
        ] = score