# vllm-project/vllm#13760: [Usage]: Does vllm support to deploy one model on multiple type GPUs(e.g. one is A100, the other is H20)?

| 字段 | 值 |
| --- | --- |
| Issue | [#13760](https://github.com/vllm-project/vllm/issues/13760) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Does vllm support to deploy one model on multiple type GPUs(e.g. one is A100, the other is H20)?

### Issue 正文摘录

### Your current environment ```text Does vllm support to deploy one model on multiple type GPUs(e.g. one is A100, the other is H20, use vllm to deploy one model on the above two GPUs)? ``` ### How would you like to use vllm If i have two GPUs, one is A100, the other is H20, i want to use vllm to deploy one model on the above two GPUs. Does vllm support this? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Does vllm support to deploy one model on multiple type GPUs(e.g. one is A100, the other is H20)? usage;stale ### Your current environment ```text Does vllm support to deploy one model on multiple type GPUs(e.g. one is A...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: Does vllm support to deploy one model on multiple type GPUs(e.g. one is A100, the other is H20)? usage;stale ### Your current environment ```text Does vllm support to deploy one model on multiple type GPUs(e.g....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e model on multiple type GPUs(e.g. one is A100, the other is H20)? usage;stale ### Your current environment ```text Does vllm support to deploy one model on multiple type GPUs(e.g. one is A100, the other is H20, use vll...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
