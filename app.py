import asyncio
import os

import pandas as pd
import gradio as gr

from src.datasets import load_all_datasets
from src.hybrid_evaluator import HybridEvaluator
from src.fastmix_runner import FastMixRunner

from dashboard.plots import DashboardPlots


# =====================================
# Initialize
# =====================================

datasets = load_all_datasets()

runner = FastMixRunner(
    datasets,
    HybridEvaluator()
)


# =====================================
# Run FastMix
# =====================================

def run_fastmix_sync():

    try:

        print("RUN BUTTON CLICKED")

        history = asyncio.run(
            runner.run()
        )

        history.save_csv(
            "history.csv"
        )

        print("RUN COMPLETE")

        return "Optimization Finished"

    except Exception as e:

        print(f"ERROR: {e}")

        import traceback
        traceback.print_exc()

        return f"ERROR: {str(e)}"


# =====================================
# Load History
# =====================================

def load_history():

    try:

        return pd.read_csv(
            "history.csv"
        )

    except Exception as e:

        print(
            f"History load error: {e}"
        )

        return pd.DataFrame()


# =====================================
# Charts
# =====================================

def alpha_chart():

    df = load_history()

    if len(df) == 0:

        return None

    return DashboardPlots.alpha_plot(
        df
    )


def score_chart():

    df = load_history()

    if len(df) == 0:

        return None

    return DashboardPlots.score_plot(
        df
    )


def advantage_chart():

    df = load_history()

    if len(df) == 0:

        return None

    return DashboardPlots.advantage_plot(
        df
    )


# =====================================
# Upload Dataset
# =====================================

def upload_dataset(file):

    if file is None:

        return "No file uploaded"

    return f"Uploaded: {file.name}"


# =====================================
# Leaderboard
# =====================================

def leaderboard():

    df = load_history()

    if len(df) == 0:

        return pd.DataFrame()

    score_cols = [

        c

        for c in df.columns

        if c.endswith("_score")
    ]

    latest = (
        df.iloc[-1]
        [score_cols]
    )

    return (
        latest
        .sort_values(
            ascending=False
        )
        .reset_index()
    )


# =====================================
# Latest Alpha
# =====================================

def latest_alpha():

    df = load_history()

    if len(df) == 0:

        return pd.DataFrame()

    alpha_cols = [

        c

        for c in df.columns

        if c.endswith("_alpha")
    ]

    latest = (
        df.iloc[-1]
        [alpha_cols]
    )

    return (
        latest
        .reset_index()
    )


# =====================================
# Report Export
# =====================================

def generate_report():

    if not os.path.exists(
        "history.csv"
    ):

        return None

    return "history.csv"


# =====================================
# UI
# =====================================

with gr.Blocks() as demo:

    gr.Markdown(
        "# FastMix Dashboard"
    )

    with gr.Tab("Run"):

        run_btn = gr.Button(
            "Run FastMix"
        )

        status = gr.Textbox()

        run_btn.click(
            fn=run_fastmix_sync,
            outputs=status
        )

    with gr.Tab("Dataset"):

        upload = gr.File()

        upload_status = gr.Textbox()

        upload.change(
            upload_dataset,
            upload,
            upload_status
        )

    with gr.Tab("Alpha"):

        alpha_btn = gr.Button(
            "Show Alpha Evolution"
        )

        alpha_plot = gr.Plot()

        alpha_btn.click(
            alpha_chart,
            outputs=alpha_plot
        )

        alpha_table_btn = gr.Button(
            "Latest Alpha"
        )

        alpha_table = gr.Dataframe()

        alpha_table_btn.click(
            latest_alpha,
            outputs=alpha_table
        )

    with gr.Tab("Scores"):

        score_btn = gr.Button(
            "Show Score Evolution"
        )

        score_plot = gr.Plot()

        score_btn.click(
            score_chart,
            outputs=score_plot
        )

    with gr.Tab("Advantage"):

        adv_btn = gr.Button(
            "Show Advantages"
        )

        adv_plot = gr.Plot()

        adv_btn.click(
            advantage_chart,
            outputs=adv_plot
        )

    with gr.Tab("Leaderboard"):

        leaderboard_btn = gr.Button(
            "Refresh Leaderboard"
        )

        leaderboard_table = gr.Dataframe()

        leaderboard_btn.click(
            leaderboard,
            outputs=leaderboard_table
        )

    with gr.Tab("Reports"):

        report_btn = gr.Button(
            "Download Report"
        )

        report_file = gr.File()

        report_btn.click(
            generate_report,
            outputs=report_file
        )


demo.launch(
    share=False
)