class CostTracker:

    def __init__(self):

        self.calls = 0

        self.judge_calls = 0

    def llm_call(self):

        self.calls += 1

    def judge_call(self):

        self.judge_calls += 1

    def report(self):

        return {
            "generation_calls":
                self.calls,

            "judge_calls":
                self.judge_calls,

            "total_calls":
                self.calls +
                self.judge_calls
        }