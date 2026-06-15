# vllm-project/vllm#8069: [Usage]: Does VLLM support starting multiple cards using mpirun? Want to bind different CPUs to each card.

| 字段 | 值 |
| --- | --- |
| Issue | [#8069](https://github.com/vllm-project/vllm/issues/8069) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Does VLLM support starting multiple cards using mpirun? Want to bind different CPUs to each card.

### Issue 正文摘录

### Your current environment Does VLLM support starting multiple cards using mpirun? Want to bind different CPUs to each card. When testing performance, use mpirun to bind different CPUs to different cards. ### How would you like to use vllm Does VLLM support starting multiple cards using mpirun? Want to bind different CPUs to each card. When testing performance, use mpirun to bind different CPUs to different cards. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ds. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: iple cards using mpirun? Want to bind different CPUs to each card. usage;stale ### Your current environment Does VLLM support starting multiple cards using mpirun? Want to bind different CPUs to each card. When testing...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: tiple cards using mpirun? Want to bind different CPUs to each card. When testing performance, use mpirun to bind different CPUs to different cards. ### How would you like to use vllm Does VLLM support starting multiple...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
