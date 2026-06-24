from openai import AsyncOpenAI

from tenacity import retry
from tenacity import stop_after_attempt
from tenacity import wait_exponential

from config.settings import (
    OPENROUTER_API_KEY,
    MODEL_NAME
)

client = AsyncOpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://openrouter.ai/api/v1"
)


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(
        multiplier=1,
        min=2,
        max=10
    )
)
async def ask_llm(
    prompt: str
):

    response = await client.chat.completions.create(
        model=MODEL_NAME,
        temperature=0.2,
        max_tokens=128,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

    )

    return (
        response
        .choices[0]
        .message
        .content
    )


async def test_connection():

    response = await ask_llm(
        "What is 2+2?"
    )

    print(response)


if __name__ == "__main__":

    import asyncio

    asyncio.run(
        test_connection()
    )