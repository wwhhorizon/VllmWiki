# vllm-project/vllm#8332: [Usage]: How to stop VLLM during generation ?

| 字段 | 值 |
| --- | --- |
| Issue | [#8332](https://github.com/vllm-project/vllm/issues/8332) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to stop VLLM during generation ?

### Issue 正文摘录

### Your current environment Hi, While serving VLLM and generating a text let's say, how could i trigger a `curl` to stop the current generation ? Currently using llama 3.1 70b. Thanks ### How would you like to use vllm _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ould i trigger a `curl` to stop the current generation ? Currently using llama 3.1 70b. Thanks ### How would you like to use vllm _No response_ ### Before submitting a new issue... - [X] Make sure you already searched f...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: How to stop VLLM during generation ? usage;stale ### Your current environment Hi, While serving VLLM and generating a text let's say, how could i trigger a `curl` to stop the current generation ? Currently usin...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
