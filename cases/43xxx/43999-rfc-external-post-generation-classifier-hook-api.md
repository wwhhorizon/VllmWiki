# vllm-project/vllm#43999: [RFC] External post-generation classifier hook API

| 字段 | 值 |
| --- | --- |
| Issue | [#43999](https://github.com/vllm-project/vllm/issues/43999) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC] External post-generation classifier hook API

### Issue 正文摘录

## Motivation Many production deployments need to attach a post-generation classifier to vLLM so that every completion is scored for safety, hallucination, audit, or A/B routing before the response is returned to the client. Today the only ways to do this are: 1. Monkey-patch `build_app()` in `vllm.entrypoints.openai.api_server` to inject a Starlette middleware that wraps the response. Fragile across vLLM minor releases and breaks `streaming=True` because the response body is already partially flushed by the time the middleware sees it. 2. Run vLLM behind a reverse proxy that re-parses the OpenAI JSON, calls the classifier, and re-serializes. Doubles the request latency and loses access to per-engine signals (prompt logprobs, KV state, etc). 3. Subclass `OpenAIServingChat` / `OpenAIServingCompletion` and override `create_chat_completion`. Survives one or two releases at most because vLLM iterates fast on those classes. None of these survive a vLLM upgrade comfortably. The current state pushes safety vendors into vLLM-version pinning and that hurts the ecosystem. What is missing is a small, public, opt-in hook surface where an external classifier registers a callable that receives...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: n classifier to vLLM so that every completion is scored for safety, hallucination, audit, or A/B routing before the response is returned to the client. Today the only ways to do this are: 1. Monkey-patch `build_app()` i...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: callable that receives the request, the generated text, and the engine's metadata for that request, and either returns scores (non-blocking) or returns a decision (blocking, with an optional replacement body). ## Propos...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: generated_text: str extra_fields: dict[str, Any] # from OpenAIBaseModel.get_extra_fields() finish_reason: str prompt_token_ids: list[int] output_token_ids: list[int] request_metadata: dict[str, Any] # opaque per-request...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: that every completion is scored for safety, hallucination, audit, or A/B routing before the response is returned to the client. Today the only ways to do this are: 1. Monkey-patch `build_app()` in `vllm.entrypoints.open...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: vLLM-version pinning and that hurts the ecosystem. What is missing is a small, public, opt-in hook surface where an external classifier registers a callable that receives the request, the generated text, and the engine'...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
