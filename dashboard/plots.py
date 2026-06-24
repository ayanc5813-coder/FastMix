import plotly.express as px


class DashboardPlots:

    @staticmethod
    @staticmethod
    def alpha_plot(df):
        alpha_cols = [

            c

            for c in df.columns

            if c.endswith("_alpha")
        ]

        fig = px.line(
            df,
            x="iteration",
            y=alpha_cols,
            title="Alpha Evolution"
        )

        fig.update_layout(

            template="plotly_dark",

            height=600,

            width=1000
        )

        return fig

    @staticmethod
    @staticmethod
    def score_plot(df):
        score_cols = [

            c

            for c in df.columns

            if c.endswith("_score")
        ]

        fig = px.line(
            df,
            x="iteration",
            y=score_cols,
            title="Task Scores"
        )

        fig.update_layout(

            template="plotly_dark",

            height=600,

            width=1000
        )

        return fig

    @staticmethod
    def advantage_plot(df):
        adv_cols = [

            c

            for c in df.columns

            if c.endswith("_adv")
        ]

        fig = px.line(
            df,
            x="iteration",
            y=adv_cols,
            title="Advantages"
        )

        fig.update_layout(

            template="plotly_dark",

            height=600,

            width=1000
        )

        return fig
class DashboardPlots:

    @staticmethod
    def beautify(fig):

        fig.update_layout(
            template="plotly_dark",
            height=600,
            width=1000,
            hovermode="x unified"
        )

        return fig