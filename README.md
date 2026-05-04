# Brainiall LLM Gateway

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Models](https://img.shields.io/badge/AI%20Models-104-blue)](https://chat.brainiall.com/v1/models)
[![Pricing](https://img.shields.io/badge/Pricing-%245.99%2Fmo%20flat-green)](https://chat.brainiall.com/pricing)
[![EU Hosted](https://img.shields.io/badge/EU%20Hosted-Frankfurt%20%2B%20Madrid-blueviolet)](https://chat.brainiall.com)
[![GDPR](https://img.shields.io/badge/GDPR-compliant-success)](https://chat.brainiall.com/dpa)
[![AI Act](https://img.shields.io/badge/AI%20Act-Article%2050-success)](https://chat.brainiall.com/ai-disclosure)
[![OpenAI Compatible](https://img.shields.io/badge/OpenAI%20SDK-compatible-orange)](https://chat.brainiall.com/openai-compatible-providers)

**104 AI models behind one OpenAI-compatible API.** Access Claude 4.7, GPT-5, Gemini 3 Pro, Llama 4, DeepSeek R1, Mistral and more for **$5.99/mo flat** — predictable, no per-token surprises.

→ **[Free 7-day Pro trial at chat.brainiall.com](https://chat.brainiall.com)** (no credit card required)

## Quick Start (30 seconds)

Drop-in replacement for OpenAI SDK — change two lines:

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.brainiall.com/v1",  # CHANGE this
    api_key="brnl-...",                         # CHANGE this
)

response = client.chat.completions.create(
    model="claude-sonnet-4-7",  # also: gpt-5, gemini-3-pro, llama-4-maverick, deepseek-r1
    messages=[{"role": "user", "content": "Hello!"}],
)
print(response.choices[0].message.content)
```

That's it. Your existing code (function calling, streaming, JSON mode, vision) works unchanged.

## Why Brainiall?

- **Single API key** for 104 models (Claude, GPT, Gemini, Llama, DeepSeek, Mistral, Cohere)
- **$5.99/mo flat** — predictable cost (vs per-token surprises that hit $300/mo from runaway agents)
- **EU-hosted** bare-metal (Frankfurt + Madrid) — GDPR + AI Act Article 50 compliant
- **Multi-currency native** (USD / EUR / BRL — PIX/Boleto coming Q2 2026)
- **Bundled multimodal**: chat + embeddings + speech (TTS/STT) + vision + image gen — all flat plan
- **Drop-in OpenAI SDK** — works with LangChain, LlamaIndex, Vercel AI SDK, n8n, Continue.dev, Cline
- **No training on customer data** + signed DPA + Article 50 transparency

## Documentation

### 📚 Full Guides (GitHub Issues)

- **[Roadmap Q2-Q3 2026 + Use Cases](../../issues/1)** — community input welcome
- **[FAQ — Common Questions](../../issues/2)** — Brainiall vs OpenRouter / Cloudflare AI Gateway
- **[Integration Examples](../../issues/3)** — LangChain, LlamaIndex, Vercel AI SDK, n8n, Continue.dev, Cline
- **[Migration Guide](../../issues/4)** — From OpenAI / Anthropic / OpenRouter (5-min switch)
- **[Performance & Latency](../../issues/5)** — Real measured P50/P95 numbers + reproducible benchmark
- **[Pricing Calculator](../../issues/6)** — Break-even analysis vs per-token providers

### 💻 Code Tutorials (Public Gists)

- **[Python Tutorial](https://gist.github.com/fasuizu-br/fd1b2bd91dd616516456e8d84257fd31)** (12 examples — chat, streaming, tools, vision, JSON, embeddings, RAG, STT, TTS, image gen, agent loop, model comparison)
- **[TypeScript / Node.js Tutorial](https://gist.github.com/fasuizu-br/ab61e67356d7df9bbc3c32362ff9417e)** (12 examples + Vercel AI SDK + Cloudflare Workers)
- **[Bash / curl CLI](https://gist.github.com/fasuizu-br/52e4f74701c87817dfa17df181184e7e)** (13 patterns + CI/CD health gate)
- **[n8n Workflow JSON](https://gist.github.com/fasuizu-br/46e94a944348e98723f24150c19d4483)** (importable: chat + embeddings + TTS)
- **[Go Client](https://gist.github.com/fasuizu-br/49834336ac65c712f8579e6c33c93b3a)** (dependency-free `net/http` + K8s sidecar example)

## Available Models (104 curated)

### Chat (60+ models)
- **Claude** 4.7 Sonnet/Opus/Haiku, 4.6, 3.7
- **GPT** 5, 4o, 4-turbo, o1, o3-mini
- **Gemini** 3 Pro/Flash, 2.5
- **Llama** 4 Maverick/Scout, 3.3
- **DeepSeek** R1, V3
- **Mistral** Large 2, Codestral, Pixtral
- **Cohere** Command R+, R
- ...and 40+ more

### Embeddings
- text-embedding-3-large (3072 dim)
- text-embedding-3-small (1536 dim)

### Vision (image-in)
- GPT-5, Claude 4.7, Gemini 3 Pro

### Speech
- **STT**: Whisper-large-v3 + variants
- **TTS**: Multiple voices, multi-language

### Image Generation
- FLUX.1 Pro, Schnell
- Stable Diffusion XL
- GPT-image-1

### Video Generation (limited)
- Seedance 2.0
- Veo

Full catalog: https://chat.brainiall.com/v1/models

## Authentication

```bash
# 1. Sign up at https://chat.brainiall.com (7-day free trial, no card)
# 2. Settings → API Keys → Create Key
# 3. Use the brnl-... key
curl https://api.brainiall.com/v1/chat/completions \
  -H "Authorization: Bearer brnl-..." \
  -H "Content-Type: application/json" \
  -d '{"model": "claude-sonnet-4-7", "messages": [{"role": "user", "content": "Hello"}]}'
```

## Compliance + Trust

- **GDPR Article 28 DPA**: signed copy at https://chat.brainiall.com/dpa
- **AI Act Article 50 transparency**: https://chat.brainiall.com/ai-disclosure
- **Subprocessors**: https://chat.brainiall.com/subprocessors
- **Security disclosure (RFC 9116)**: https://chat.brainiall.com/.well-known/security.txt
- **SLA tiers**: 99.5% baseline / 99.9% Pro / 99.95% Enterprise — https://chat.brainiall.com/sla
- **Status page**: https://chat.brainiall.com/status

## Honest Current State

Brainiall is bootstrapped — no VC, built independently. Currently **23 users, 0 paying customers** (May 2026). This GitHub repo focuses on documentation + dev experience so future paying customers can find us via real reference material rather than marketing claims.

We track public metrics + open roadmap. Star this repo if you want to follow progress.

## What's Next

See [Issue #1 Roadmap](../../issues/1) for Q2-Q3 2026 plan. Highlights:

- PIX/Boleto payment for Brazilian customers (Q2 2026)
- Self-hosted enterprise option (Q3 2026)
- Per-model usage analytics dashboard (Q3 2026)
- LangChain + LlamaIndex official integration packages
- ZenMux / Bifrost competitive comparison guides

## Get Started

→ **Free 7-day Pro trial: [chat.brainiall.com](https://chat.brainiall.com)** (no credit card required)
→ **Documentation**: [chat.brainiall.com/api](https://chat.brainiall.com/api)
→ **Quickstart**: [chat.brainiall.com/start-1-minute](https://chat.brainiall.com/start-1-minute)
→ **Pricing**: [chat.brainiall.com/pricing](https://chat.brainiall.com/pricing)

## Want a Specific Integration?

Open an issue or comment on [#3 Integration Examples](../../issues/3). Common requests already covered:

LangChain · LlamaIndex · Vercel AI SDK · n8n · Continue.dev · Cline · Cloudflare Workers · Next.js Edge · K8s sidecar · Docker compose · Bash CLI

## License

MIT

---

## Recently shipped (May 2026)

- 📊 [Real cost analysis: 7 LLM gateways tested with $100 budget](https://chat.brainiall.com/blog-real-cost-7-llm-gateways-tested-may-2026)
- 🧮 [AI Subscription Savings Calculator](https://chat.brainiall.com/savings-calculator) — see your monthly savings switching to flat $5.99/mo
- 📦 [Free embeddable widgets](https://chat.brainiall.com/widgets) — 3 cross-origin JS widgets for any site (cost calculator, badge, comparison card)
- 🔄 [All 38+ alternatives](https://chat.brainiall.com/alternatives/) — Brainiall vs OpenAI, Anthropic, OpenRouter, Groq, LiteLLM, Portkey, Bifrost, MegaLLM, and more

_Last updated: 2026-05-04_
