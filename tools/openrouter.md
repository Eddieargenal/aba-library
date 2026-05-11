---
type: tool
tool: openrouter
status: active
updated: 2026-05-06
---

# Tool: OpenRouter

## Purpose

Routes LLM API calls to multiple providers (OpenAI, Anthropic, Mistral, etc.) through a single unified API.

## Used For

- Calling different models based on mode (cheap / fix / code / plan)
- Comparing model outputs across providers
- Falling back to an alternate provider when one is unavailable
- Managing API cost by routing to lower-cost models for simple tasks

## Safety Rules

- Do not store API keys in this wiki.
- Do not log raw request/response content that may contain user data.
- Rate limits and cost caps should be configured in OpenRouter dashboard, not hardcoded in prompts.
- Always confirm the model being called matches the intended mode tier.

## Related Workflows

- [[../governance/workflows/model-routing]]
- [[../agents/Hermes]]

## Notes

- OpenRouter API endpoint: `https://openrouter.ai/api/v1`
- Model selection is passed as `model` parameter in the API call.
- Check OpenRouter pricing page for current model costs before routing.
