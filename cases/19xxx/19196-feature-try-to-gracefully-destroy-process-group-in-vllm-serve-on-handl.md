# vllm-project/vllm#19196: [Feature]: try to gracefully destroy process group in `vllm serve` on handling Ctrl+C (prior to processes termination)

| 字段 | 值 |
| --- | --- |
| Issue | [#19196](https://github.com/vllm-project/vllm/issues/19196) |
| 状态 | open |
| 标签 | feature request;unstale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: try to gracefully destroy process group in `vllm serve` on handling Ctrl+C (prior to processes termination)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Otherwise I get `[rank0]:[W604 11:18:57.117195760 ProcessGroupNCCL.cpp:1476] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/docs/stable/distributed.html#shutdown (function operator())` which seems harmless, but it would be better to not have this warning if possible ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: `vllm serve` on handling Ctrl+C (prior to processes termination) feature request;unstale ### 🚀 The feature, motivation and pitch Otherwise I get `[rank0]:[W604 11:18:57.117195760 ProcessGroupNCCL.cpp:1476] Warning: WARN...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
