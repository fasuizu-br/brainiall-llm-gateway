#!/bin/bash
# Brainiall LLM Gateway — curl Examples
#
# Base URL: https://apim-ai-apis.azure-api.net/v1
# Get your API key at https://brainiall.com

BASE_URL="https://apim-ai-apis.azure-api.net/v1"
API_KEY="YOUR_KEY"  # Replace with your API key

echo "=== Basic Chat Completion ==="
curl -s -X POST "$BASE_URL/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $API_KEY" \
  -d '{
    "model": "claude-sonnet-4-6",
    "messages": [{"role": "user", "content": "What is 2+2?"}],
    "max_tokens": 100
  }' | python3 -m json.tool

echo ""
echo "=== Streaming ==="
curl -s -N -X POST "$BASE_URL/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $API_KEY" \
  -d '{
    "model": "claude-haiku-4-5",
    "messages": [{"role": "user", "content": "Count from 1 to 5"}],
    "stream": true
  }'

echo ""
echo ""
echo "=== Using api-key header ==="
curl -s -X POST "$BASE_URL/chat/completions" \
  -H "Content-Type: application/json" \
  -H "api-key: $API_KEY" \
  -d '{
    "model": "nova-micro",
    "messages": [{"role": "user", "content": "Say hello in 3 languages"}],
    "max_tokens": 100
  }' | python3 -m json.tool

echo ""
echo "=== Using Ocp-Apim-Subscription-Key header ==="
curl -s -X POST "$BASE_URL/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Ocp-Apim-Subscription-Key: $API_KEY" \
  -d '{
    "model": "deepseek-v3",
    "messages": [{"role": "user", "content": "What is Python?"}],
    "max_tokens": 100
  }' | python3 -m json.tool

echo ""
echo "=== JSON Mode ==="
curl -s -X POST "$BASE_URL/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $API_KEY" \
  -d '{
    "model": "claude-sonnet-4-6",
    "messages": [
      {"role": "system", "content": "Extract data as JSON."},
      {"role": "user", "content": "Alice, 28, engineer at Microsoft in Seattle"}
    ],
    "response_format": {"type": "json_object"},
    "max_tokens": 200
  }' | python3 -m json.tool

echo ""
echo "=== Tool Calling ==="
curl -s -X POST "$BASE_URL/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $API_KEY" \
  -d '{
    "model": "claude-sonnet-4-6",
    "messages": [{"role": "user", "content": "What is the weather in Paris?"}],
    "tools": [{
      "type": "function",
      "function": {
        "name": "get_weather",
        "description": "Get the current weather for a location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {"type": "string", "description": "City name"}
          },
          "required": ["location"]
        }
      }
    }],
    "tool_choice": "auto"
  }' | python3 -m json.tool

echo ""
echo "=== List Models ==="
curl -s "$BASE_URL/models" \
  -H "Authorization: Bearer $API_KEY" | python3 -c "
import json, sys
data = json.load(sys.stdin)
print(f'Total models: {len(data[\"data\"])}')
for m in sorted(data['data'], key=lambda x: x['id'])[:20]:
    print(f'  {m[\"id\"]:40s} {m[\"owned_by\"]}')
print('  ...')
"
