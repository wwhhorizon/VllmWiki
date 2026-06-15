# vllm-project/vllm#8419: [Misc]: Can vLLM go out of memory during the decode phase if too many tokens are generated?

| 字段 | 值 |
| --- | --- |
| Issue | [#8419](https://github.com/vllm-project/vllm/issues/8419) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Can vLLM go out of memory during the decode phase if too many tokens are generated?

### Issue 正文摘录

### Anything you want to discuss about vllm. Can vLLM go out of memory during the decode phase if too many tokens are generated? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Misc]: Can vLLM go out of memory during the decode phase if too many tokens are generated? stale ### Anything you want to discuss about vllm. Can vLLM go out of memory during the decode phase if too many tokens are gen...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
