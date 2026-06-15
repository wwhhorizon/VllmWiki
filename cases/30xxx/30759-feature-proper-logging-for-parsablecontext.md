# vllm-project/vllm#30759: [Feature]: proper logging for ParsableContext

| 字段 | 值 |
| --- | --- |
| Issue | [#30759](https://github.com/vllm-project/vllm/issues/30759) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: proper logging for ParsableContext

### Issue 正文摘录

### 🚀 The feature, motivation and pitch we recently introduced MCP for all models to reach feature parity with GPTOSS https://github.com/vllm-project/vllm/issues/30115. one thing we need to add is proper logging. ### Alternatives _No response_ ### Additional context subtasks: - [x] add unit tests for logging in HarmonyContext for _update_prefill_token_usage(): https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/context.py#L560 and _update_decode_token_usage. This is not for non harmony models but adding these unit tests should help give context on the logging we currently have for GPTOSS. - [ ] create _update_prefill_token_usage() and _update_decode_token_usage() for ParsableContext, inside append_output(). Add unit tests and also an E2E test in test_response_api_parsable_context. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: proper logging for ParsableContext feature request;stale ### 🚀 The feature, motivation and pitch we recently introduced MCP for all models to reach feature parity with GPTOSS https://github.com/vllm-project/v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: xt. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 🚀 The feature, motivation and pitch we recently introduced MCP for all models to reach feature parity with GPTOSS https://github.com/vllm-project/vllm/issues/30115. one thing we need to add is proper logging. ### Altern...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: natives _No response_ ### Additional context subtasks: - [x] add unit tests for logging in HarmonyContext for _update_prefill_token_usage(): https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/context.py#L56...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
