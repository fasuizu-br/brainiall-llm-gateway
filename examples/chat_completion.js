/**
 * Brainiall LLM Gateway — JavaScript Chat Completion Examples
 *
 * Base URL: https://apim-ai-apis.azure-api.net/v1
 * Get your API key at https://brainiall.com
 *
 * Install: npm install openai
 */

import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://apim-ai-apis.azure-api.net/v1",
  apiKey: "YOUR_KEY", // Replace with your API key
});

// Basic chat completion
async function basicChat() {
  const response = await client.chat.completions.create({
    model: "claude-sonnet-4-6",
    messages: [{ role: "user", content: "What is the capital of Japan?" }],
  });
  console.log(response.choices[0].message.content);
  console.log(`Tokens: ${response.usage.total_tokens}`);
}

// Streaming chat completion
async function streamingChat() {
  const stream = await client.chat.completions.create({
    model: "claude-sonnet-4-6",
    messages: [
      { role: "system", content: "You are a creative writer." },
      { role: "user", content: "Write a haiku about programming." },
    ],
    stream: true,
    max_tokens: 256,
  });

  for await (const chunk of stream) {
    const content = chunk.choices[0]?.delta?.content;
    if (content) process.stdout.write(content);
  }
  console.log();
}

// Tool/function calling
async function toolCalling() {
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
    tools,
    tool_choice: "auto",
  });

  const message = response.choices[0].message;
  if (message.tool_calls) {
    for (const toolCall of message.tool_calls) {
      console.log(`Function: ${toolCall.function.name}`);
      console.log(`Arguments: ${toolCall.function.arguments}`);
    }
  }
}

// JSON mode
async function jsonMode() {
  const response = await client.chat.completions.create({
    model: "claude-sonnet-4-6",
    messages: [
      {
        role: "system",
        content: "Extract structured data. Return valid JSON.",
      },
      {
        role: "user",
        content:
          "John Smith, 35 years old, works at Google in Mountain View as a Senior Engineer.",
      },
    ],
    response_format: { type: "json_object" },
  });

  const data = JSON.parse(response.choices[0].message.content);
  console.log(JSON.stringify(data, null, 2));
}

// Multi-turn conversation
async function multiTurn() {
  const messages = [
    { role: "system", content: "You are a helpful math tutor." },
    { role: "user", content: "What is the derivative of x^3?" },
  ];

  let response = await client.chat.completions.create({
    model: "claude-haiku-4-5",
    messages,
  });

  const firstAnswer = response.choices[0].message.content;
  console.log(`Turn 1: ${firstAnswer}`);

  messages.push({ role: "assistant", content: firstAnswer });
  messages.push({ role: "user", content: "And the integral of that?" });

  response = await client.chat.completions.create({
    model: "claude-haiku-4-5",
    messages,
  });
  console.log(`Turn 2: ${response.choices[0].message.content}`);
}

// List all available models
async function listModels() {
  const models = await client.models.list();
  for (const model of models.data.sort((a, b) => a.id.localeCompare(b.id))) {
    console.log(`${model.id.padEnd(40)} — ${model.owned_by}`);
  }
}

// Run examples
console.log("=== Basic Chat ===");
await basicChat();

console.log("\n=== Streaming ===");
await streamingChat();

console.log("\n=== Tool Calling ===");
await toolCalling();

console.log("\n=== JSON Mode ===");
await jsonMode();

console.log("\n=== Multi-Turn ===");
await multiTurn();

console.log("\n=== List Models ===");
await listModels();
