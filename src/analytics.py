import pandas as pd


class Analytics:

    def __init__(
        self,
        csv_path
    ):

        self.df = pd.read_csv(
            csv_path
        )

    def dataframe(self):

        return self.df

    def latest_alpha(self):

        alpha_cols = [

            c

            for c in self.df.columns

            if c.endswith("_alpha")
        ]

        return (
            self.df.iloc[-1]
            [alpha_cols]
            .to_dict()
        )

    def latest_scores(self):

        score_cols = [

            c

            for c in self.df.columns

            if c.endswith("_score")
        ]

        return (
            self.df.iloc[-1]
            [score_cols]
            .to_dict()
        )

    def leaderboard(self):

        score_cols = [

            c

            for c in self.df.columns

            if c.endswith("_score")
        ]

        latest = (
            self.df.iloc[-1]
            [score_cols]
        )

        return (
            latest
            .sort_values(
                ascending=False
            )
        )

    def leaderboard_table(self):
        board = (
            self.leaderboard()
            .reset_index()
        )

        board.columns = [
            "Task",
            "Score"
        ]

        return board

    def export_html(
            self,
            fig,
            filename
    ):
        fig.write_html(
            filename
        )