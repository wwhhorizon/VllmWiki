# vllm-project/vllm#27982: [Usage]: How can I access or return hidden states (representations) after generation?

| 字段 | 值 |
| --- | --- |
| Issue | [#27982](https://github.com/vllm-project/vllm/issues/27982) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How can I access or return hidden states (representations) after generation?

### Issue 正文摘录

### Your current environment In my training pipeline (GRPO), I need to access hidden-state representations of all layers and store prompt representations alongside generated sequences. Is there any supported way to extract or return hidden states from the vLLM inference engine? Environment vllm==0.11.0 Python 3.12 ### How would you like to use vllm ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: llm ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: access or return hidden states (representations) after generation? usage;stale ### Your current environment In my training pipeline (GRPO), I need to access hidden-state representations of all layers and store prompt re...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
