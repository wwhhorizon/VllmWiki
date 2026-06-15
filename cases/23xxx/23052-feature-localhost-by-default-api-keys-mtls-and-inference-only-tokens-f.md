# vllm-project/vllm#23052: [Feature]: Localhost-by-default, API keys/mTLS, and inference-only tokens for vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#23052](https://github.com/vllm-project/vllm/issues/23052) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Localhost-by-default, API keys/mTLS, and inference-only tokens for vLLM

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Summary In our testbed, **vLLM** (like other backends) returned **successful POST** responses for text-generation endpoints (e.g., `/v1/completions`) out-of-the-box—consistent with backend servers being directly exposed for inference. Across platforms, a notable fraction of exposed assets respond to endpoint probes, and many of those allow unauthenticated interactions when misconfigured. ### Risks (misconfig scenario) If bound to public interfaces without controls, attackers could consume resources, abuse quotas, or pivot via attached model/FS features depending on the environment. (Our validation was **testbed-only**.) ### Requested features / suggestions - **Localhost-by-default** bind; explicit flag to listen on `0.0.0.0`. - **Built-in auth**: API keys (per-route scopes) and **mTLS** option; **inference-only tokens** that cannot call admin/management routes. - **Rate limits & quotas**: per-key QPS/tokens budget to deter resource abuse. - **CORS/CSRF hardening**: conservative CORS presets off by default. - **Security checklist** in docs: reverse-proxy templates, TLS, firewall, least-privilege FS access. ### Coordination We can share de...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: int probes, and many of those allow unauthenticated interactions when misconfigured. ### Risks (misconfig scenario) If bound to public interfaces without controls, attackers could consume resources, abuse quotas, or piv...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: st-by-default, API keys/mTLS, and inference-only tokens for vLLM feature request;stale ### 🚀 The feature, motivation and pitch ### Summary In our testbed, **vLLM** (like other backends) returned **successful POST** resp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: , motivation and pitch ### Summary In our testbed, **vLLM** (like other backends) returned **successful POST** responses for text-generation endpoints (e.g., `/v1/completions`) out-of-the-box—consistent with backend ser...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: # Requested features / suggestions - **Localhost-by-default** bind; explicit flag to listen on `0.0.0.0`. - **Built-in auth**: API keys (per-route scopes) and **mTLS** option; **inference-only tokens** that cannot call...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
