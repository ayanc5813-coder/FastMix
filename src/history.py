import pandas as pd


class OptimizationHistory:

    def __init__(self):

        self.rows = []

    def add(
        self,
        iteration,
        alpha,
        scores,
        advantage
    ):

        row = {

            "iteration":
                iteration
        }

        tasks = list(
            scores.keys()
        )

        for i, task in enumerate(tasks):

            row[
                f"{task}_score"
            ] = scores[task]

            row[
                f"{task}_alpha"
            ] = float(alpha[i])

            row[
                f"{task}_adv"
            ] = float(advantage[i])

        self.rows.append(row)

    def dataframe(self):

        return pd.DataFrame(
            self.rows
        )

    def save_csv(
        self,
        filename
    ):

        self.dataframe().to_csv(
            filename,
            index=False
        )