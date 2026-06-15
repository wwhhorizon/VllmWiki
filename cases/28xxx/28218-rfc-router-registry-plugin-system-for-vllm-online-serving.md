# vllm-project/vllm#28218: [RFC]: Router Registry & Plugin System for vLLM Online Serving

| 字段 | 值 |
| --- | --- |
| Issue | [#28218](https://github.com/vllm-project/vllm/issues/28218) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Router Registry & Plugin System for vLLM Online Serving

### Issue 正文摘录

### Motivation. Today, vLLM's online serving endpoints are tightly coupled within `vllm/entrypoints/openai/api_server.py`: - OpenAI-compatible routes (`/v1/chat/completions`, `/v1/completions`, etc.) - Anthropic-compatible routes (`/v1/messages`) - vLLM-specific routes (`/tokenize`, `/detokenize`, etc.) - Core infrastructure (FastAPI app, CORS, metrics, SSL, middleware) **Problems:** 1. **Tight Coupling**: Adding new API protocols (e.g., Jina reranker, custom endpoints) requires modifying core files. 2. **Scalability**: All providers share a single monolithic `api_server.py` (~2100 lines). 3. **Customization Barriers**: Third-party integrations cannot extend vLLM's API surface without forking. ### Proposed Change. Introduce `vllm.router`, a plugin-based registry that: - Allows **providers** (API protocol handlers) to register routers dynamically. - Uses Python `entry_points` for discovery (mirroring `ModelRegistry`). - Supports **lazy loading** via ` : ` strings to avoid import overhead. - Enables **selective mounting** via CLI flags (e.g., `--providers openai,anthropic`). ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. ### Architecture Overview...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: letions`, etc.) - Anthropic-compatible routes (`/v1/messages`) - vLLM-specific routes (`/tokenize`, `/detokenize`, etc.) - Core infrastructure (FastAPI app, CORS, metrics, SSL, middleware) **Problems:** 1. **Tight Coupl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: _No response_ ### CC List. _No response_ ### Any Other Things. ### Architecture Overview ``` ┌─────────────────────────────────────────────────────────────┐ │ vllm.plugins (Existing + Extended) │ │ ┌────────────────────...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ters dynamically. - Uses Python `entry_points` for discovery (mirroring `ModelRegistry`). - Supports **lazy loading** via ` : ` strings to avoid import overhead. - Enables **selective mounting** via CLI flags (e.g., `--...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [RFC]: Router Registry & Plugin System for vLLM Online Serving RFC;stale ### Motivation. Today, vLLM's online serving endpoints are tightly coupled within `vllm/entrypoints/openai/api_server.py`: - OpenAI-compatible rou...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [RFC]: Router Registry & Plugin System for vLLM Online Serving RFC;stale ### Motivation. Today, vLLM's online serving endpoints are tightly coupled within `vllm/entrypoints/openai/api_server.py`: - OpenAI-compatible rou...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
