# vllm-project/vllm#31966: [Feature]: Proposal: Optional Admin Control Plane API + CLI for Safe Production Operations

| 字段 | 值 |
| --- | --- |
| Issue | [#31966](https://github.com/vllm-project/vllm/issues/31966) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Proposal: Optional Admin Control Plane API + CLI for Safe Production Operations

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Introduce a minimal, optional admin control plane for vLLM, consisting of: A small HTTP Admin API for inspecting runtime state and performing safe lifecycle operations A thin CLI reference client (vllm admin …) built on top of this API This control plane is strictly for production operations, not inference, and is: Disabled by default Read-only by default UI-agnostic Separate from the inference API surface Proposed Admin API (high-level) GET /v1/admin/health # health & readiness GET /v1/admin/models # loaded models GET /v1/admin/queue # queue / concurrency stats POST /v1/admin/drain # drain traffic (optional) POST /v1/admin/reload_model # reload models (optional / gated) CLI (reference client) vllm admin status vllm admin models vllm admin queue vllm admin drain vllm admin reload The CLI is intentionally thin and acts as a reference implementation for how the API is intended to be used. ### 🎯 Motivation and Pitch vLLM has become a widely adopted inference engine and is frequently run in production environments, including Kubernetes deployments. In practice, many operators treat vLLM as a long-running service that must be monitored, drained,...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: duce a minimal, optional admin control plane for vLLM, consisting of: A small HTTP Admin API for inspecting runtime state and performing safe lifecycle operations A thin CLI reference client (vllm admin …) built on top...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: nal Admin Control Plane API + CLI for Safe Production Operations feature request;stale ### 🚀 The feature, motivation and pitch Introduce a minimal, optional admin control plane for vLLM, consisting of: A small HTTP Admi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: rnatives Considered 1. External Sidecars / Wrappers Many teams already build wrappers around vLLM to expose health, drain, or reload logic. #### Downside: Fragmented implementations No shared contract Increased operatio...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: -level) GET /v1/admin/health # health & readiness GET /v1/admin/models # loaded models GET /v1/admin/queue # queue / concurrency stats POST /v1/admin/drain # drain traffic (optional) POST /v1/admin/reload_model # reload...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
