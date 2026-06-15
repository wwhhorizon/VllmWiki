# vllm-project/vllm#37422: [Feature]: Add kv_transfer_params to Responses API for PD disaggregation

| 字段 | 值 |
| --- | --- |
| Issue | [#37422](https://github.com/vllm-project/vllm/issues/37422) |
| 状态 | closed |
| 标签 | rocm |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add kv_transfer_params to Responses API for PD disaggregation

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The Chat Completions API (`/v1/chat/completions`) supports `kv_transfer_params` on both request and response, enabling PD disaggregation. However, the Responses API (`/v1/responses`) does not have this field, so PD disaggregation cannot be used through it. Since the Responses API is becoming more widely adopted, it would be valuable to add `kv_transfer_params` support for feature parity with Chat Completions. The change is straightforward: add the field to `ResponsesRequest`/`ResponsesResponse`, inject it into `SamplingParams.extra_args` in `to_sampling_params()`, and track it through all context types (`SimpleContext`, `ParsableContext`, `HarmonyContext`, `StreamingHarmonyContext`). This follows the exact same pattern already used in `ChatCompletionRequest`/`ChatCompletionResponse`. I have an implementation ready and have tested E2E PD disaggregation (NixlConnector, AMD MI250) across all context types — will submit a PR shortly. ### Alternatives Users must use the Chat Completions API instead of the Responses API when PD disaggregation is needed. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you a...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Add kv_transfer_params to Responses API for PD disaggregation rocm ### 🚀 The feature, motivation and pitch The Chat Completions API (`/v1/chat/completions`) supports `kv_transfer_params` on both request and r...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: tions API (`/v1/chat/completions`) supports `kv_transfer_params` on both request and response, enabling PD disaggregation. However, the Responses API (`/v1/responses`) does not have this field, so PD disaggregation cann...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: uest`/`ChatCompletionResponse`. I have an implementation ready and have tested E2E PD disaggregation (NixlConnector, AMD MI250) across all context types — will submit a PR shortly. ### Alternatives Users must use the Ch...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
