# vllm-project/vllm#37305: [RFC][XPU]: Enable Intel XPU CI for vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#37305](https://github.com/vllm-project/vllm/issues/37305) |
| 状态 | open |
| 标签 | RFC;intel-gpu |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC][XPU]: Enable Intel XPU CI for vLLM

### Issue 正文摘录

### Motivation. ## 1. Summary This RFC proposes enabling a dedicated Intel XPU CI pipeline for vLLM. The goal is to ensure that updates to vLLM maintain correctness and performance on Intel XPU devices, while improving test efficiency, parallelism, and scalability of CI. --- ## 2. Motivation / Background Currently, the vLLM CI on Intel XPU is limited: - A **single simple script** triggers both build and sanity tests. - **Build and tests execute on the same machine**, leading to low device utilization. - Tests **are not executed in parallel**, reducing efficiency. - Test case management and expansion are **inefficient**. - The current workflow **does not follow ci-infra’s design standards**. With increasing contributions targeting Intel XPU in vLLM, a dedicated Intel CI pipeline is necessary to: - Guarantee correctness and performance on Intel XPU. - Improve test parallelism and device utilization. - Enable scalable, maintainable test case management. --- ## 3. Problem Statement 1. **Inefficient device usage**: build and tests share the same Intel XPU machine sequentially. 2. **Non-parallel test execution**: limits throughput and increases CI runtime. 3. **Limited test case managem...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [RFC][XPU]: Enable Intel XPU CI for vLLM RFC;intel-gpu ### Motivation. ## 1. Summary This RFC proposes enabling a dedicated Intel XPU CI pipeline for vLLM. The goal is to ensure that updates to vLLM maintain correctness...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: intain correctness and performance on Intel XPU devices, while improving test efficiency, parallelism, and scalability of CI. --- ## 2. Motivation / Background Currently, the vLLM CI on Intel XPU is limited: - A **singl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: formance on Intel XPU devices, while improving test efficiency, parallelism, and scalability of CI. --- ## 2. Motivation / Background Currently, the vLLM CI on Intel XPU is limited: - A **single simple script** triggers...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
