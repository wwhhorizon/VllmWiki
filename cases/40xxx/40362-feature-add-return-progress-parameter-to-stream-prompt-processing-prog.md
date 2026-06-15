# vllm-project/vllm#40362: [Feature]: Add return_progress parameter to stream prompt processing progress during prefill

| 字段 | 值 |
| --- | --- |
| Issue | [#40362](https://github.com/vllm-project/vllm/issues/40362) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add return_progress parameter to stream prompt processing progress during prefill

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When serving very long contexts (100k+ tokens), clients have no visibility into prefill progress, the connection appears frozen until the first generated token arrives, which can take tens of seconds or more. llama.cpp server implements this via a `return_progress` parameter: when set alongside `stream: true`, the server emits SSE chunks during prefill with a `prompt_progress` field: ```json {"prompt_progress": {"total": 4096, "cache": 512, "processed": 1024, "time_ms": 340}} ``` Fields: - `total` — total prompt tokens - `cache` — tokens already served from prefix cache - `processed` — tokens processed so far - `time_ms` — elapsed time since prefill started ### Alternatives Polling `/metrics` is possible but requires a separate connection, adds complexity client-side, and the Prometheus metrics don't map cleanly to per-request prefill progress. ### Additional context Reference implementation: [`tools/server` in llama.cpp](https://github.com/ggml-org/llama.cpp/tree/master/tools/server). The parameter would naturally be passed via `extra_body` with the OpenAI Python SDK since it's outside the OpenAI spec. ### Before submitting a new issue... -...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: dd return_progress parameter to stream prompt processing progress during prefill feature request ### 🚀 The feature, motivation and pitch When serving very long contexts (100k+ tokens), clients have no visibility into pr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ec. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: : - `total` — total prompt tokens - `cache` — tokens already served from prefix cache - `processed` — tokens processed so far - `time_ms` — elapsed time since prefill started ### Alternatives Polling `/metrics` is possi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: first generated token arrives, which can take tens of seconds or more. llama.cpp server implements this via a `return_progress` parameter: when set alongside `stream: true`, the server emits SSE chunks during prefill wi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
