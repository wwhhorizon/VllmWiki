# vllm-project/vllm#20282: [Usage]:  NCCL Hang/Deadlock with Mixed GPU Setup (RTX 5070 & RTX 3080)

| 字段 | 值 |
| --- | --- |
| Issue | [#20282](https://github.com/vllm-project/vllm/issues/20282) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:  NCCL Hang/Deadlock with Mixed GPU Setup (RTX 5070 & RTX 3080)

### Issue 正文摘录

### Your current environment Hello vLLM Team and Community, I am seeking assistance with a persistent NCCL initialization hang when using a mixed-generation GPU setup for tensor parallelism (tensor_parallel_size=2). My system has an NVIDIA RTX 5070 Ti and an NVIDIA RTX 3080 (Ampere). I have already researched similar issues and understand that Peer-to-Peer (P2P) communication is often unsupported or buggy between different GPU architectures. Following the official troubleshooting documentation and community advice, I have tried the standard workarounds, but the process still hangs. ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Usage]: NCCL Hang/Deadlock with Mixed GPU Setup (RTX 5070 & RTX 3080) usage;stale ### Your current environment Hello vLLM Team and Community, I am seeking assistance with a persistent NCCL initialization hang when usin...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: upported or buggy between different GPU architectures. Following the official troubleshooting documentation and community advice, I have tried the standard workarounds, but the process still hangs. ### How would you lik...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: NCCL Hang/Deadlock with Mixed GPU Setup (RTX 5070 & RTX 3080) usage;stale ### Your current environment Hello vLLM Team and Community, I am seeking assistance with a persistent NCCL initialization hang when usin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for re...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
