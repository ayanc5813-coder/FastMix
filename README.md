# FastMix

FastMix is a lightweight implementation of adaptive dataset mixture optimization inspired by recent research on data mixture learning for large language models.

Instead of manually deciding how much training data should come from reasoning, coding, math, memory, or tool-use datasets, FastMix automatically learns optimal mixture weights (α) through iterative evaluation and optimization.

The system evaluates model performance across multiple task categories, updates dataset weights using an Adam-based optimizer, and visualizes learning dynamics through an interactive Gradio dashboard.

---

## Features

* Adaptive dataset mixture optimization
* Multi-task evaluation pipeline
* Adam-based alpha optimization
* Checkpoint recovery support
* Interactive Gradio dashboard
* Alpha evolution tracking
* Score evolution tracking
* Leaderboard visualization
* CSV report export
* Modular architecture
* OpenRouter integration
* Local mock model fallback support

---

## Architecture

```text
Datasets
│
├── Reasoning
├── Coding
├── Math
├── Memory
└── Tools
        │
        ▼
Benchmark Evaluation
        │
        ▼
Task Scores
        │
        ▼
Adam Alpha Optimizer
        │
        ▼
Updated Mixture Weights (α)
        │
        ▼
Checkpoint + Analytics
        │
        ▼
Gradio Dashboard
```

---

## Optimization Loop

```text
     Web      Code      Math
      |         |         |
      v         v         v

      +-------------------+
      | Mixture Weights α |
      +-------------------+
                 |
                 v

      +-------------------+
      |   Proxy Model θ   |
      +-------------------+
                 |
                 v

          Validation Score
                 |
                 v

      +-------------------+
      | Gradient Update α |
      +-------------------+

                 ^
                 |
           Repeat Loop
```

---

## Project Structure

```text
FastMix/

├── app.py
├── requirements.txt
├── README.md

├── config/
│   └── settings.py

├── data/
│   ├── reasoning.json
│   ├── coding.json
│   ├── math.json
│   ├── memory.json
│   └── tools.json

├── src/
│   ├── benchmark.py
│   ├── checkpoint.py
│   ├── datasets.py
│   ├── evaluator.py
│   ├── fastmix_runner.py
│   ├── history.py
│   ├── hybrid_evaluator.py
│   ├── judge_client.py
│   ├── llm_judge.py
│   ├── openrouter_client.py
│   └── optimizer.py

├── dashboard/
│   └── plots.py

├── checkpoints/
├── logs/
└── notebooks/
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/FastMix.git

cd FastMix
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## OpenRouter Setup

Create an environment variable:

Windows:

```bash
set OPENROUTER_API_KEY=your_key_here
```

Linux / Mac:

```bash
export OPENROUTER_API_KEY=your_key_here
```

Optional:

```bash
export MODEL_NAME=deepseek/deepseek-chat-v3
```

---

## Running FastMix

Launch the dashboard:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:7860
```

---

## Dashboard Features

### Run FastMix

Runs the complete optimization pipeline.

### Alpha Evolution

Visualizes changing dataset mixture weights.

### Score Evolution

Tracks benchmark performance over time.

### Leaderboard

Ranks task categories by latest performance.

### Reports

Exports optimization history as CSV.

### Checkpoint Recovery

Automatically resumes from the latest saved checkpoint.

---

## Example Output

```text
RUN BUTTON CLICKED

Iteration 0
[0.20 0.20 0.20 0.20 0.20]

Iteration 1
[0.18 0.24 0.22 0.19 0.17]

Iteration 2
[0.16 0.28 0.23 0.18 0.15]

...
```

---

## Optimization Method

FastMix learns dataset weights using an Adam optimizer over task performance.

For each iteration:

1. Evaluate all task datasets
2. Compute task scores
3. Calculate advantages
4. Update alpha logits
5. Apply temperature-scaled softmax
6. Save checkpoint
7. Log analytics

Result:

```text
Better Tasks
      ↑
More Weight

Worse Tasks
      ↓
Less Weight
```

---

## Future Improvements

* Bayesian optimization
* Population-based training
* Reinforcement learning based alpha search
* Multi-model evaluation
* Distributed execution
* Hugging Face integration
* Weights & Biases tracking
* Automated benchmark suites

---

## Disclaimer

This project is an educational and experimental implementation designed to demonstrate adaptive dataset mixture optimization concepts. It is not intended to reproduce large-scale training results from production foundation models.

---

## License

MIT License
