# vllm-project/vllm#13652: [Usage]: What normalization is applied in LLM.embed function. Can we create our own?

| 字段 | 值 |
| --- | --- |
| Issue | [#13652](https://github.com/vllm-project/vllm/issues/13652) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: What normalization is applied in LLM.embed function. Can we create our own?

### Issue 正文摘录

### How would you like to use vllm I want to get the last hidden state without Normalization. I am using `LLM.embed` function to do this, but this function is returning Normalized outputs. I want to understand what kind of Normalization is being used and is there a way to change that? Model - Qwen2VL ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: kind of Normalization is being used and is there a way to change that? Model - Qwen2VL ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 2VL ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: alization is applied in LLM.embed function. Can we create our own? usage;stale ### How would you like to use vllm I want to get the last hidden state without Normalization. I am using `LLM.embed` function to do this, bu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
