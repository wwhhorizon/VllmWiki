# vllm-project/vllm#33429: [Feature]: Investigate if higher TORCHINDUCTOR_COMPILE_THREADS leads to faster compile times

| 字段 | 值 |
| --- | --- |
| Issue | [#33429](https://github.com/vllm-project/vllm/issues/33429) |
| 状态 | closed |
| 标签 | feature request;torch.compile;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Investigate if higher TORCHINDUCTOR_COMPILE_THREADS leads to faster compile times

### Issue 正文摘录

### 🚀 The feature, motivation and pitch This is currently set to 1: https://github.com/search?q=repo%3Avllm-project%2Fvllm%20TORCHINDUCTOR_COMPILE_THREADS&type=code I don't have context over why it was set to 1. I've seen things like: - vscode debugging issue https://github.com/vllm-project/vllm/issues/10480 (@angelayi have you seen this before?) - it seems undesirable for it to generate multiple processes (https://github.com/vllm-project/vllm/issues/10619, @jeejeelee and @youkaichao why was it undesirable?) I'm opening this issue for the following investigation: 1) understand how much TORCHINDUCTOR_COMPILE_THREADS actually influences the compile times 2) if it is significant, figure out how we can bring it back. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: gher TORCHINDUCTOR_COMPILE_THREADS leads to faster compile times feature request;torch.compile;stale ### 🚀 The feature, motivation and pitch This is currently set to 1: https://github.com/search?q=repo%3Avllm-project%2F...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: Investigate if higher TORCHINDUCTOR_COMPILE_THREADS leads to faster compile times feature request;torch.compile;stale ### 🚀 The feature, motivation and pitch This is currently set to 1: https://github.com/sea...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: , motivation and pitch This is currently set to 1: https://github.com/search?q=repo%3Avllm-project%2Fvllm%20TORCHINDUCTOR_COMPILE_THREADS&type=code I don't have context over why it was set to 1. I've seen things like: -...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
