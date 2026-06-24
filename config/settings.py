import os

# ==========================
# OpenRouter Configuration
# ==========================

OPENROUTER_API_KEY = os.getenv(
    "OPENROUTER_API_KEY",
    ""
)

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "deepseek/deepseek-chat-v3"
)

# ==========================
# Optimization Parameters
# ==========================

BATCH_SIZE = 32

LEARNING_RATE = 0.05

OPTIMIZATION_STEPS = 50

# ==========================
# Runtime
# ==========================

MAX_WORKERS = 10

RANDOM_SEED = 42

# ==========================
# Directories
# ==========================

CHECKPOINT_DIR = "checkpoints"

LOG_DIR = "logs"

# ==========================
# FastMix Tasks
# ==========================

TASKS = [
    "reasoning",
    "coding",
    "math",
    "memory",
    "tools"
]

JUDGE_MODEL = "deepseek/deepseek-chat-v3"

USE_LLM_JUDGE = True

JUDGE_MAX_SCORE = 10
ALPHA_TEMPERATURE = 1.2