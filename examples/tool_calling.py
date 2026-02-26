"""
Brainiall LLM Gateway — Advanced Tool Calling Examples

Demonstrates multi-tool agents, tool call loops, and parallel tool calls.

Base URL: https://apim-ai-apis.azure-api.net/v1
Get your API key at https://brainiall.com
"""

from openai import OpenAI
import json

client = OpenAI(
    base_url="https://apim-ai-apis.azure-api.net/v1",
    api_key="YOUR_KEY"
)

# Define multiple tools
tools = [
    {
        "type": "function",
        "function": {
            "name": "search_products",
            "description": "Search for products in the catalog",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search query"},
                    "category": {
                        "type": "string",
                        "enum": ["electronics", "clothing", "books", "home"],
                        "description": "Product category filter"
                    },
                    "max_price": {
                        "type": "number",
                        "description": "Maximum price in USD"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Max results to return",
                        "default": 5
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_product_details",
            "description": "Get detailed info about a specific product",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_id": {"type": "string", "description": "Product ID"}
                },
                "required": ["product_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "add_to_cart",
            "description": "Add a product to the shopping cart",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_id": {"type": "string", "description": "Product ID"},
                    "quantity": {"type": "integer", "description": "Quantity", "default": 1}
                },
                "required": ["product_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_shipping",
            "description": "Calculate shipping cost for the current cart",
            "parameters": {
                "type": "object",
                "properties": {
                    "zip_code": {"type": "string", "description": "Destination ZIP code"},
                    "method": {
                        "type": "string",
                        "enum": ["standard", "express", "overnight"],
                        "description": "Shipping method"
                    }
                },
                "required": ["zip_code"]
            }
        }
    }
]


def simulate_tool_result(name: str, arguments: dict) -> str:
    """Simulate tool execution — replace with real implementations."""
    if name == "search_products":
        return json.dumps({
            "results": [
                {"id": "prod-001", "name": "Wireless Headphones", "price": 79.99, "rating": 4.5},
                {"id": "prod-002", "name": "Bluetooth Speaker", "price": 49.99, "rating": 4.2},
                {"id": "prod-003", "name": "USB-C Hub", "price": 34.99, "rating": 4.7}
            ],
            "total_results": 3
        })
    elif name == "get_product_details":
        return json.dumps({
            "id": arguments["product_id"],
            "name": "Wireless Headphones",
            "price": 79.99,
            "description": "Premium noise-cancelling headphones with 30-hour battery life",
            "in_stock": True,
            "colors": ["black", "white", "navy"]
        })
    elif name == "add_to_cart":
        return json.dumps({
            "success": True,
            "cart_total": 79.99,
            "item_count": 1
        })
    elif name == "calculate_shipping":
        return json.dumps({
            "standard": {"cost": 5.99, "days": "5-7"},
            "express": {"cost": 12.99, "days": "2-3"},
            "overnight": {"cost": 24.99, "days": "1"}
        })
    return json.dumps({"error": "Unknown tool"})


def run_agent(user_message: str, max_iterations: int = 5):
    """Run a tool-calling agent loop until the model stops calling tools."""
    messages = [
        {
            "role": "system",
            "content": "You are a helpful shopping assistant. Use the available tools to help the user find and purchase products."
        },
        {"role": "user", "content": user_message}
    ]

    for i in range(max_iterations):
        print(f"\n--- Iteration {i + 1} ---")

        response = client.chat.completions.create(
            model="claude-sonnet-4-6",
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )

        message = response.choices[0].message
        messages.append(message)

        # If no tool calls, the agent is done
        if not message.tool_calls:
            print(f"\nAssistant: {message.content}")
            return message.content

        # Process each tool call
        for tool_call in message.tool_calls:
            name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)
            print(f"Calling: {name}({json.dumps(args)})")

            # Execute the tool
            result = simulate_tool_result(name, args)
            print(f"Result: {result}")

            # Add tool result to messages
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result
            })

    print("\nMax iterations reached")
    return None


def parallel_tool_calls():
    """Demonstrate parallel tool calls (model calls multiple tools at once)."""
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Search for headphones under $100 and also calculate shipping to ZIP 94105"
        }
    ]

    response = client.chat.completions.create(
        model="claude-sonnet-4-6",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    message = response.choices[0].message
    if message.tool_calls:
        print(f"Model made {len(message.tool_calls)} parallel tool calls:")
        for tc in message.tool_calls:
            print(f"  - {tc.function.name}({tc.function.arguments})")


if __name__ == "__main__":
    print("=== Shopping Agent ===")
    run_agent("I'm looking for wireless headphones under $100. Can you find some options?")

    print("\n\n=== Parallel Tool Calls ===")
    parallel_tool_calls()
