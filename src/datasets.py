from datasets import load_dataset


def load_reasoning_dataset(limit=50):

    ds = load_dataset(
        "gsm8k",
        "main",
        split="test"
    )

    data = []

    for row in ds.select(range(limit)):

        data.append(
            {
                "question": row["question"],
                "answer": row["answer"]
            }
        )

    return data


def load_coding_dataset(limit=50):

    ds = load_dataset(
        "mbpp",
        split="test"
    )

    data = []

    for row in ds.select(range(limit)):

        data.append(
            {
                "question": row["text"],
                "answer": row["code"]
            }
        )

    return data


def load_math_dataset(limit=50):

    ds = load_dataset(
        "gsm8k",
        "main",
        split="test"
    )

    data = []

    for row in ds.select(range(limit)):

        data.append(
            {
                "question": row["question"],
                "answer": row["answer"]
            }
        )

    return data


def load_memory_dataset():

    return [
        {
            "question":
            "Remember banana. What was the word?",
            "answer":
            "banana"
        },
        {
            "question":
            "Remember elephant. What was the word?",
            "answer":
            "elephant"
        }
    ]


def load_tools_dataset():

    return [
        {
            "question":
            "Which tool retrieves web information?",
            "answer":
            "web"
        },
        {
            "question":
            "Which tool executes Python code?",
            "answer":
            "python"
        }
    ]


def load_all_datasets():

    return {

        "reasoning":
            load_reasoning_dataset(),

        "coding":
            load_coding_dataset(),

        "math":
            load_math_dataset(),

        "memory":
            load_memory_dataset(),

        "tools":
            load_tools_dataset()
    }