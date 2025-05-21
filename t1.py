from huggingface_hub import InferenceClient

API_HF = "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"

client = InferenceClient(
    model="microsoft/trocr-base-printed",
    provider="hf-inference",
    api_key=API_HF,
)

image_path = "agenda.jpg"

# Puedes pasar ruta local directamente
response = client.image_to_text(image=image_path)

print(response['generated_text'])
