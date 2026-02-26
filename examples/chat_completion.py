"""
Brainiall LLM Gateway — Python Chat Completion Examples

Base URL: https://apim-ai-apis.azure-api.net/v1
Get your API key at https://brainiall.com
"""

from openai import OpenAI

# Initialize client
client = OpenAI(
    base_url="https://apim-ai-apis.azure-api.net/v1",
    api_key="YOUR_KEY"  # Replace with your API key
)


def basic_chat():
    """Simple chat completion."""
    response = client.chat.completions.create(
        model="claude-sonnet-4-6",
        messages=[{"role": "user", "content": "What is the capital of Japan?"}]
    )
    print(response.choices[0].message.content)
    print(f"Tokens: {response.usage.total_tokens}")


def streaming_chat():
    """Streaming chat completion with real-time output."""
    stream = client.chat.completions.create(
        model="claude-sonnet-4-6",
        messages=[
            {"role": "system", "content": "You are a creative writer."},
            {"role": "user", "content": "Write a short poem about the ocean."}
        ],
        stream=True,
        max_tokens=256
    )

    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
    print()


def multi_turn_conversation():
    """Multi-turn conversation with message history."""
    messages = [
        {"role": "system", "content": "You are a math tutor. Be concise."},
        {"role": "user", "content": "What is the derivative of x^3?"}
    ]

    # First turn
    response = client.chat.completions.create(
        model="claude-haiku-4-5",
        messages=messages
    )
    assistant_msg = response.choices[0].message.content
    print(f"Assistant: {assistant_msg}")

    # Second turn
    messages.append({"role": "assistant", "content": assistant_msg})
    messages.append({"role": "user", "content": "What about x^4 + 2x^2?"})

    response = client.chat.completions.create(
        model="claude-haiku-4-5",
        messages=messages
    )
    print(f"Assistant: {response.choices[0].message.content}")


def json_mode():
    """Force JSON output from the model."""
    response = client.chat.completions.create(
        model="claude-sonnet-4-6",
        messages=[
            {"role": "system", "content": "Extract structured data. Return valid JSON."},
            {"role": "user", "content": "John Smith, 35 years old, works at Google in Mountain View as a Senior Engineer."}
        ],
        response_format={"type": "json_object"},
        max_tokens=256
    )

    import json
    data = json.loads(response.choices[0].message.content)
    print(json.dumps(data, indent=2))


def compare_models():
    """Compare responses from different models."""
    models = ["claude-haiku-4-5", "nova-micro", "deepseek-v3"]
    prompt = "In one sentence, what is machine learning?"

    for model in models:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100
        )
        print(f"[{model}] {response.choices[0].message.content}")
        print(f"  Tokens: {response.usage.total_tokens}")
        print()


def vision_example():
    """Analyze an image using a vision-capable model."""
    response = client.chat.completions.create(
        model="claude-sonnet-4-6",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe this image briefly."},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Camponotus_flavomarginatus_ant.jpg/320px-Camponotus_flavomarginatus_ant.jpg"
                        }
                    }
                ]
            }
        ],
        max_tokens=256
    )
    print(response.choices[0].message.content)


def list_models():
    """List all available models."""
    models = client.models.list()
    for model in sorted(models.data, key=lambda m: m.id):
        print(f"{model.id:40s} — {model.owned_by}")


if __name__ == "__main__":
    print("=== Basic Chat ===")
    basic_chat()

    print("\n=== Streaming ===")
    streaming_chat()

    print("\n=== Multi-Turn ===")
    multi_turn_conversation()

    print("\n=== JSON Mode ===")
    json_mode()

    print("\n=== Compare Models ===")
    compare_models()

    print("\n=== Vision ===")
    vision_example()

    print("\n=== List Models ===")
    list_models()
