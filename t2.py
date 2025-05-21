from huggingface_hub import InferenceClient
from config import API_HF

client = InferenceClient(
    provider="novita",
    api_key=API_HF,
)

completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3-0324",
    messages=[
        {
            "role": "user",
            "content": "How many 'G's in 'huggingface'?"
        }
    ],
)

print(completion.choices[0].message)