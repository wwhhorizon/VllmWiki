# vllm-project/vllm#39221: [Bug]: Inconsistent tool-calling behavior between Chat Completions and Responses API when tool parsing params is not set

| 字段 | 值 |
| --- | --- |
| Issue | [#39221](https://github.com/vllm-project/vllm/issues/39221) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Inconsistent tool-calling behavior between Chat Completions and Responses API when tool parsing params is not set

### Issue 正文摘录

### Your current environment ### Describe the bug When the vLLM server is started **without** `--enable-auto-tool-choice` / `--tool-call-parser`, the Chat Completions API and the Responses API handle tool-calling requests differently: | API | Behavior when tool parsing params are missing | |---|---| | Chat Completions (`/v1/chat/completions`) | Returns a **400 error**: `"auto" tool choice requires --enable-auto-tool-choice and --tool-call-parser to be set` | | Responses (`/v1/responses`) | **Silently succeeds** — the model's raw ` ` markup is returned as a `ResponseOutputText` instead of a structured `ResponseFunctionToolCall` | These two APIs should behave consistently. Either both should error, or both should return the unparsed output gracefully. Right now a user can get a hard error on one endpoint and silent, broken output on the other for the exact same server configuration and tools payload. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ad. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: to be set` | | Responses (`/v1/responses`) | **Silently succeeds** — the model's raw ` ` markup is returned as a `ResponseOutputText` instead of a structured `ResponseFunctionToolCall` | These two APIs should behave con...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ser`, the Chat Completions API and the Responses API handle tool-calling requests differently: | API | Behavior when tool parsing params are missing | |---|---| | Chat Completions (`/v1/chat/completions`) | Returns a **...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
