# vllm-project/vllm#34782: [Feature]: Support structured outputs for beam search

| 字段 | 值 |
| --- | --- |
| Issue | [#34782](https://github.com/vllm-project/vllm/issues/34782) |
| 状态 | open |
| 标签 | feature request;unstale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support structured outputs for beam search

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I'm attempting to do certain code generation with structured outputs (grammar guided). I find it falled short because of the auto-regressive generation pattern, so I want to try beam search but find the structured outputs do not work. ### Alternatives Nothing yet. It is possible to do multiple samplings and pick the most probable one, but this is still different from beam search, as beam search selects the most probable sequences at every step ### Additional context According to AI, this is because the structured_outputs param is not passed into the `beam_search` method and is not used when sampling: https://github.com/vllm-project/vllm/blob/a49ea5a58fc0f8170027abd79168d6f7ca3e4789/vllm/entrypoints/llm.py#L663-L670 https://github.com/vllm-project/vllm/blob/a49ea5a58fc0f8170027abd79168d6f7ca3e4789/vllm/entrypoints/llm.py#L711-L716 To resolve this, apart from adding structured_output param, it needs to deal with request_id, as vLLM use request_id to manage state machines I'm not sure whether there is something else required ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot livi...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support structured outputs for beam search feature request;unstale ### 🚀 The feature, motivation and pitch I'm attempting to do certain code generation with structured outputs (grammar guided). I find it fall...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Feature]: Support structured outputs for beam search feature request;unstale ### 🚀 The feature, motivation and pitch I'm attempting to do certain code generation with structured outputs (grammar guided). I find it fall...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: st_id to manage state machines I'm not sure whether there is something else required ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bot...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
