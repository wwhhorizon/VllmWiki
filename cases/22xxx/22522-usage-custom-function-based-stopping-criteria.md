# vllm-project/vllm#22522: [Usage]:  Custom function-based stopping criteria

| 字段 | 值 |
| --- | --- |
| Issue | [#22522](https://github.com/vllm-project/vllm/issues/22522) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:  Custom function-based stopping criteria

### Issue 正文摘录

### Your current environment N/A ### How would you like to use vllm I’m wondering if vLLM currently supports something like a *function-based* stopper, similar to hugging faces `stoppingCriteria` where instead of stopping based on fixed stop strings or token IDs, the generation can be halted dynamically based on custom logic. For example: * An agent generates text. * As it generates, I track a **budget** made up of: * Number of tokens generated so far. * Cost of external tools the agent has called (e.g., code execution, web search). * Once the budget is exhausted, the stopper would end generation immediately. My questions: 1. Is there already a way to hook into the generation loop and stop it based on this kind of dynamic condition? 2. If not, what would be the best way to implement it? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Cost of external tools the agent has called (e.g., code execution, web search). * Once the budget is exhausted, the stopper would end generation immediately. My questions: 1. Is there already a way to hook into the gene...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Custom function-based stopping criteria usage;stale ### Your current environment N/A ### How would you like to use vllm I’m wondering if vLLM currently supports something like a *function-based* stopper, simila...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
