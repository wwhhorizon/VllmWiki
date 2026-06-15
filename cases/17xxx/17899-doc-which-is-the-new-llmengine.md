# vllm-project/vllm#17899: [Doc]: Which is the new LLMEngine?

| 字段 | 值 |
| --- | --- |
| Issue | [#17899](https://github.com/vllm-project/vllm/issues/17899) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Which is the new LLMEngine?

### Issue 正文摘录

### 📚 The doc issue Following V0-> V1 update there are now two `LLMEngine` classes defined in the project: 1. https://github.com/vllm-project/vllm/blob/v0.8.5/vllm/v1/engine/llm_engine.py#L37 2. https://github.com/vllm-project/vllm/blob/v0.8.5/vllm/engine/llm_engine.py#L123 The docstring of (1.) says that it is "Legacy LLMEngine for backwards compatibility". But I guess this is the class of choice to be used currently, right? This is a bit confusing to me. ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Doc]: Which is the new LLMEngine? documentation;stale ### 📚 The doc issue Following V0-> V1 update there are now two `LLMEngine` classes defined in the project: 1. https://github.com/vllm-project/vllm/blob/v0.8.5/vllm/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
