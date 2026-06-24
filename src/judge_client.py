from openai import AsyncOpenAI

from tenacity import retry
from tenacity import stop_after_attempt
from tenacity import wait_exponential

from config.settings import (
    OPENROUTER_API_KEY,
    JUDGE_MODEL
)

client = AsyncOpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://openrouter.ai/api/v1"
)


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential()
)
async def judge_completion(
    prompt
):

    response = await client.chat.completions.create(
        model=JUDGE_MODEL,
        temperature=0,
        max_tokens=32,
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return (
        response
        .choices[0]
        .message
        .content
    )