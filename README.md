# Brainiall LLM Gateway

**113+ AI models via a single OpenAI-compatible API.** Access Claude, DeepSeek, Llama, Qwen, Nova, Mistral, and more through AWS Bedrock at 35-50% lower cost.

## Overview

Brainiall LLM Gateway is a production-ready API gateway that provides OpenAI-compatible access to 113+ language models from 17 providers via AWS Bedrock. It supports streaming, tool/function calling, vision, and structured outputs.

**Base URL:** `https://apim-ai-apis.azure-api.net/v1`

**Key Features:**
- OpenAI SDK compatible (drop-in replacement)
- 113+ models from 17 providers
- Streaming support (SSE)
- Tool/function calling
- Vision (image inputs)
- JSON mode / structured outputs
- 35-50% cheaper via Bedrock Flex pricing, prompt caching, and cross-region inference

## Authentication

Three authentication methods are supported. Use any one:

| Method | Header | Example |
|--------|--------|---------|
| Bearer Token | `Authorization: Bearer YOUR_KEY` | OpenAI SDK standard |
| API Key | `api-key: YOUR_KEY` | Azure OpenAI standard |
| Subscription Key | `Ocp-Apim-Subscription-Key: YOUR_KEY` | APIM native |

Get your API key at [brainiall.com](https://brainiall.com).

## Quick Start

### Python (OpenAI SDK)

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://apim-ai-apis.azure-api.net/v1",
    api_key="YOUR_KEY"
)

response = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

### JavaScript (OpenAI SDK)

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://apim-ai-apis.azure-api.net/v1",
  apiKey: "YOUR_KEY",
});

const response = await client.chat.completions.create({
  model: "claude-sonnet-4-6",
  messages: [{ role: "user", content: "Hello!" }],
});
console.log(response.choices[0].message.content);
```

### curl

```bash
curl -X POST https://apim-ai-apis.azure-api.net/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_KEY" \
  -d '{
    "model": "claude-sonnet-4-6",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

## Streaming

### Python Streaming

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://apim-ai-apis.azure-api.net/v1",
    api_key="YOUR_KEY"
)

stream = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[{"role": "user", "content": "Write a haiku about programming"}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
print()
```

### JavaScript Streaming

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://apim-ai-apis.azure-api.net/v1",
  apiKey: "YOUR_KEY",
});

const stream = await client.chat.completions.create({
  model: "claude-sonnet-4-6",
  messages: [{ role: "user", content: "Write a haiku about programming" }],
  stream: true,
});

for await (const chunk of stream) {
  const content = chunk.choices[0]?.delta?.content;
  if (content) process.stdout.write(content);
}
console.log();
```

### curl Streaming

```bash
curl -X POST https://apim-ai-apis.azure-api.net/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_KEY" \
  -N \
  -d '{
    "model": "claude-sonnet-4-6",
    "messages": [{"role": "user", "content": "Write a haiku about programming"}],
    "stream": true
  }'
```

## Tool / Function Calling

### Python Tool Calling

```python
from openai import OpenAI
import json

client = OpenAI(
    base_url="https://apim-ai-apis.azure-api.net/v1",
    api_key="YOUR_KEY"
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "City name, e.g. 'San Francisco, CA'"
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "Temperature unit"
                    }
                },
                "required": ["location"]
            }
        }
    }
]

response = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[{"role": "user", "content": "What's the weather in Tokyo?"}],
    tools=tools,
    tool_choice="auto"
)

message = response.choices[0].message
if message.tool_calls:
    for tool_call in message.tool_calls:
        print(f"Function: {tool_call.function.name}")
        print(f"Arguments: {tool_call.function.arguments}")
        args = json.loads(tool_call.function.arguments)
        print(f"Location: {args['location']}")
```

### JavaScript Tool Calling

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://apim-ai-apis.azure-api.net/v1",
  apiKey: "YOUR_KEY",
});

const tools = [
  {
    type: "function",
    function: {
      name: "get_weather",
      description: "Get the current weather for a location",
      parameters: {
        type: "object",
        properties: {
          location: {
            type: "string",
            description: "City name, e.g. 'San Francisco, CA'",
          },
          unit: {
            type: "string",
            enum: ["celsius", "fahrenheit"],
            description: "Temperature unit",
          },
        },
        required: ["location"],
      },
    },
  },
];

const response = await client.chat.completions.create({
  model: "claude-sonnet-4-6",
  messages: [{ role: "user", content: "What's the weather in Tokyo?" }],
  tools: tools,
  tool_choice: "auto",
});

const message = response.choices[0].message;
if (message.tool_calls) {
  for (const toolCall of message.tool_calls) {
    console.log(`Function: ${toolCall.function.name}`);
    console.log(`Arguments: ${toolCall.function.arguments}`);
  }
}
```

## JSON Mode / Structured Outputs

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://apim-ai-apis.azure-api.net/v1",
    api_key="YOUR_KEY"
)

response = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[
        {"role": "system", "content": "Extract structured data from the user's text."},
        {"role": "user", "content": "John Smith is 35 years old and works at Google as a senior engineer in Mountain View."}
    ],
    response_format={"type": "json_object"}
)

import json
data = json.loads(response.choices[0].message.content)
print(json.dumps(data, indent=2))
# {
#   "name": "John Smith",
#   "age": 35,
#   "company": "Google",
#   "title": "Senior Engineer",
#   "location": "Mountain View"
# }
```

## Vision (Image Inputs)

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://apim-ai-apis.azure-api.net/v1",
    api_key="YOUR_KEY"
)

response = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What do you see in this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Camponotus_flavomarginatus_ant.jpg/320px-Camponotus_flavomarginatus_ant.jpg"
                    }
                }
            ]
        }
    ]
)
print(response.choices[0].message.content)
```

## Multi-Turn Conversation

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://apim-ai-apis.azure-api.net/v1",
    api_key="YOUR_KEY"
)

messages = [
    {"role": "system", "content": "You are a helpful math tutor."},
    {"role": "user", "content": "What is the derivative of x^3?"}
]

response = client.chat.completions.create(
    model="claude-haiku-4-5",
    messages=messages
)
assistant_msg = response.choices[0].message.content
print(f"Assistant: {assistant_msg}")

messages.append({"role": "assistant", "content": assistant_msg})
messages.append({"role": "user", "content": "Now what about the integral of that result?"})

response = client.chat.completions.create(
    model="claude-haiku-4-5",
    messages=messages
)
print(f"Assistant: {response.choices[0].message.content}")
```

## List Available Models

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://apim-ai-apis.azure-api.net/v1",
    api_key="YOUR_KEY"
)

models = client.models.list()
for model in models.data:
    print(f"{model.id} — owned by {model.owned_by}")
```

```bash
curl -s https://apim-ai-apis.azure-api.net/v1/models \
  -H "Authorization: Bearer YOUR_KEY" | python3 -m json.tool
```

## Available Models & Pricing

| Model | Provider | Input $/MTok | Output $/MTok | Context | Features |
|-------|----------|-------------|--------------|---------|----------|
| `claude-opus-4-6` | Anthropic | $5.00 | $25.00 | 200K | Vision, Tools, JSON |
| `claude-sonnet-4-6` | Anthropic | $3.00 | $15.00 | 200K | Vision, Tools, JSON |
| `claude-haiku-4-5` | Anthropic | $1.00 | $5.00 | 200K | Vision, Tools, JSON |
| `claude-opus-4-5` | Anthropic | $15.00 | $75.00 | 200K | Vision, Tools, JSON |
| `deepseek-r1` | DeepSeek | $1.35 | $5.40 | 128K | Reasoning, Tools |
| `deepseek-v3` | DeepSeek | $0.27 | $1.10 | 128K | Tools, JSON |
| `llama-3.3-70b` | Meta | $0.72 | $0.72 | 128K | Tools, JSON |
| `llama-4-scout-17b` | Meta | $0.17 | $0.17 | 512K | Vision, Tools |
| `llama-4-maverick-17b` | Meta | $0.20 | $0.60 | 512K | Vision, Tools |
| `qwen3-235b` | Alibaba | $0.80 | $2.40 | 128K | Reasoning, Tools |
| `qwen3-30b` | Alibaba | $0.13 | $0.50 | 128K | Reasoning, Tools |
| `nova-pro` | Amazon | $0.80 | $3.20 | 300K | Vision, Tools, JSON |
| `nova-lite` | Amazon | $0.06 | $0.24 | 300K | Vision, Tools, JSON |
| `nova-micro` | Amazon | $0.035 | $0.14 | 128K | Tools, JSON |
| `mistral-large-3` | Mistral | $2.00 | $6.00 | 128K | Vision, Tools, JSON |
| `mistral-small-3` | Mistral | $0.10 | $0.30 | 128K | Vision, Tools |
| `minimax-m2` | MiniMax | $0.50 | $2.20 | 1M | Tools, JSON |
| `jamba-2-0-large` | AI21 | $2.00 | $8.00 | 256K | Tools, JSON |

**Flex Pricing:** All models support Bedrock Flex tier at 50% discount (synchronous, variable latency).

## Integration Examples

### Cline (VS Code Extension)

In Cline settings, select "OpenAI Compatible" provider:
- Base URL: `https://apim-ai-apis.azure-api.net/v1`
- API Key: `YOUR_KEY`
- Model: `claude-sonnet-4-6`

### Continue.dev

Add to `~/.continue/config.yaml`:

```yaml
models:
  - model: claude-sonnet-4-6
    title: Brainiall Claude Sonnet
    provider: openai
    apiBase: https://apim-ai-apis.azure-api.net/v1
    apiKey: YOUR_KEY
  - model: claude-haiku-4-5
    title: Brainiall Claude Haiku
    provider: openai
    apiBase: https://apim-ai-apis.azure-api.net/v1
    apiKey: YOUR_KEY
```

### Aider

```bash
export OPENAI_API_BASE=https://apim-ai-apis.azure-api.net/v1
export OPENAI_API_KEY=YOUR_KEY
aider --model openai/claude-sonnet-4-6
```

### Claude Code (via Bedrock)

```bash
export ANTHROPIC_MODEL=us.anthropic.claude-sonnet-4-6-20250514-v1:0
export AWS_REGION=us-east-1
claude --model $ANTHROPIC_MODEL
```

### SillyTavern

1. Go to API Connections > Chat Completion
2. Select "Custom (OpenAI-compatible)"
3. Custom Endpoint: `https://apim-ai-apis.azure-api.net/v1`
4. API Key: `YOUR_KEY`
5. Select model from dropdown

### Open WebUI

```bash
docker run -d -p 3000:8080 \
  -e OPENAI_API_BASE_URLS="https://apim-ai-apis.azure-api.net/v1" \
  -e OPENAI_API_KEYS="YOUR_KEY" \
  ghcr.io/open-webui/open-webui:main
```

### LangChain (Python)

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url="https://apim-ai-apis.azure-api.net/v1",
    api_key="YOUR_KEY",
    model="claude-sonnet-4-6",
    streaming=True
)

response = llm.invoke("Explain quantum computing in simple terms")
print(response.content)
```

### LangChain with Tool Calling

```python
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers together."""
    return a * b

@tool
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

llm = ChatOpenAI(
    base_url="https://apim-ai-apis.azure-api.net/v1",
    api_key="YOUR_KEY",
    model="claude-sonnet-4-6"
)

llm_with_tools = llm.bind_tools([multiply, add])
response = llm_with_tools.invoke("What is 3 * 12 + 5?")
print(response.tool_calls)
```

### n8n

1. Create a new credential: "OpenAI API" type
2. API Key: `YOUR_KEY`
3. Base URL: `https://apim-ai-apis.azure-api.net/v1`
4. Use the "Chat Model" or "OpenAI" node with your credential

### Vercel AI SDK

```typescript
import { createOpenAI } from "@ai-sdk/openai";
import { generateText } from "ai";

const brainiall = createOpenAI({
  baseURL: "https://apim-ai-apis.azure-api.net/v1",
  apiKey: "YOUR_KEY",
});

const { text } = await generateText({
  model: brainiall("claude-sonnet-4-6"),
  prompt: "Write a TypeScript function to reverse a string.",
});
console.log(text);
```

### CrewAI

```python
from crewai import Agent, Crew, Task
import os

os.environ["OPENAI_API_BASE"] = "https://apim-ai-apis.azure-api.net/v1"
os.environ["OPENAI_API_KEY"] = "YOUR_KEY"
os.environ["OPENAI_MODEL_NAME"] = "claude-sonnet-4-6"

researcher = Agent(
    role="Researcher",
    goal="Research and summarize topics",
    backstory="You are a thorough researcher."
)

task = Task(
    description="Research the latest trends in AI agents",
    expected_output="A summary of AI agent trends",
    agent=researcher
)

crew = Crew(agents=[researcher], tasks=[task])
result = crew.kickoff()
print(result)
```

## Error Handling

```python
from openai import OpenAI, APIError, RateLimitError, AuthenticationError

client = OpenAI(
    base_url="https://apim-ai-apis.azure-api.net/v1",
    api_key="YOUR_KEY"
)

try:
    response = client.chat.completions.create(
        model="claude-sonnet-4-6",
        messages=[{"role": "user", "content": "Hello"}]
    )
    print(response.choices[0].message.content)
except AuthenticationError:
    print("Invalid API key. Check your key at brainiall.com")
except RateLimitError:
    print("Rate limited. Retry after a moment.")
except APIError as e:
    print(f"API error: {e.status_code} - {e.message}")
```

## Rate Limits

| Plan | Requests/min | Models |
|------|-------------|--------|
| Free | 10 | All models |
| Basic ($29/mo) | 100 | All models |
| Pro ($79/mo) | 500 | All models |
| Enterprise ($199/mo) | 2,000 | All models + priority |

## Links

- Website: [brainiall.com](https://brainiall.com)
- API Documentation: [brainiall.com/docs-page](https://brainiall-portal.thankfulfield-a7857897.eastus.azurecontainerapps.io/docs-page)
- Get API Key: [brainiall.com](https://brainiall.com)
- Status: [brainiall.com/health](https://apim-ai-apis.azure-api.net/v1/health)
- Speech AI APIs: [github.com/fasuizu-br/speech-ai-examples](https://github.com/fasuizu-br/speech-ai-examples)
- NLP APIs: [github.com/fasuizu-br/brainiall-nlp-api](https://github.com/fasuizu-br/brainiall-nlp-api)
- Image APIs: [github.com/fasuizu-br/brainiall-image-api](https://github.com/fasuizu-br/brainiall-image-api)

## License

MIT
