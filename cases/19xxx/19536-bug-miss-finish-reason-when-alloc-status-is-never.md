# vllm-project/vllm#19536: [Bug]: Miss finish reason when alloc status is NEVER

| 字段 | 值 |
| --- | --- |
| Issue | [#19536](https://github.com/vllm-project/vllm/issues/19536) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Miss finish reason when alloc status is NEVER

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug This will only happen if you send a request that using streaming, and its prompt is too long. When call `can_allocate` and return `AllocStatus.NEVER`, the `SequenceStatus` will be set to `FINISHED_IGNORED`, and in `vllm/vllm/entrypoints/openai/serving_chat.py`, the code below will stop it to send finish reason: ``` if not delta_text and not output.token_ids and \ not previous_num_tokens[i]: # Chunked prefill case, don't return empty chunks continue ``` and according to the status, the finish reason should be `length`. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Miss finish reason when alloc status is NEVER bug;stale ### Your current environment ### 🐛 Describe the bug This will only happen if you send a request that using streaming, and its prompt is too long. When call...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: h`. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
