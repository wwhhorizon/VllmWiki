# vllm-project/vllm#33996: [RFC]: Add an option to use NCCL-based symmetric memory when pytorch symmetric memory is applied

| 字段 | 值 |
| --- | --- |
| Issue | [#33996](https://github.com/vllm-project/vllm/issues/33996) |
| 状态 | open |
| 标签 | RFC;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Add an option to use NCCL-based symmetric memory when pytorch symmetric memory is applied

### Issue 正文摘录

### Motivation. Pytorch now supports different backends for symmetric memory including 'CUDA', 'NVSHMEM', 'NCCL' which can be controlled with `TORCH_SYMMMEM`. ### Proposed Change. - We need to find out if NCCL-based pytorch symmetric memory replicates NCCL symmetric memory we use in vLLM. - We need to refactor our usage of symmetric memory so that it has a single entry point. - Benchmark the collectives we use in vLLM to pick the best version of symmetric memory on different hardware. ### Feedback Period. _No response_ ### CC List. @Amir-19 @RohitRathore1 @kwen2501 @ProExpertProg ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Pytorch now supports different backends for symmetric memory including 'CUDA', 'NVSHMEM', 'NCCL' which can be controlled with `TORCH_SYMMMEM`. ### Proposed Change. - We need to find out if NCCL-based pytorch symmetric m...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: or our usage of symmetric memory so that it has a single entry point. - Benchmark the collectives we use in vLLM to pick the best version of symmetric memory on different hardware. ### Feedback Period. _No response_ ###...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ory is applied RFC;stale ### Motivation. Pytorch now supports different backends for symmetric memory including 'CUDA', 'NVSHMEM', 'NCCL' which can be controlled with `TORCH_SYMMMEM`. ### Proposed Change. - We need to f...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ntry point. - Benchmark the collectives we use in vLLM to pick the best version of symmetric memory on different hardware. ### Feedback Period. _No response_ ### CC List. @Amir-19 @RohitRathore1 @kwen2501 @ProExpertProg...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: iod. _No response_ ### CC List. @Amir-19 @RohitRathore1 @kwen2501 @ProExpertProg ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and ask...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
