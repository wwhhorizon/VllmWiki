# vllm-project/vllm#14213: [Misc]: How does the system evenly distribute the requests to multiple micro batches?

| 字段 | 值 |
| --- | --- |
| Issue | [#14213](https://github.com/vllm-project/vllm/issues/14213) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: How does the system evenly distribute the requests to multiple micro batches?

### Issue 正文摘录

### Anything you want to discuss about vllm. Hi there, lately we've been testing some distributed features of vLLM, when we deal with pipeline parallelism, we find an interesting thing that the system would automatically and evenly distribute the requests to multiple micro batches, which is a good way to avoid pipeline bubble. But we couldn't find related logic from the source codes. Can you explain where or in which component does this procedure actually happen? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: g some distributed features of vLLM, when we deal with pipeline parallelism, we find an interesting thing that the system would automatically and evenly distribute the requests to multiple micro batches, which is a good...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Misc]: How does the system evenly distribute the requests to multiple micro batches? stale ### Anything you want to discuss about vllm. Hi there, lately we've been testing some distributed features of vLLM, when we dea...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ## Anything you want to discuss about vllm. Hi there, lately we've been testing some distributed features of vLLM, when we deal with pipeline parallelism, we find an interesting thing that the system would automatically...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
