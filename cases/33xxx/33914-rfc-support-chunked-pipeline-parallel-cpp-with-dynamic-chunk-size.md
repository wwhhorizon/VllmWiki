# vllm-project/vllm#33914: [RFC]: Support Chunked Pipeline Parallel(CPP) with dynamic chunk size.

| 字段 | 值 |
| --- | --- |
| Issue | [#33914](https://github.com/vllm-project/vllm/issues/33914) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Support Chunked Pipeline Parallel(CPP) with dynamic chunk size.

### Issue 正文摘录

### Motivation. Currently, vLLM supports DCP and is planning to support PCP to improve long-sequence inference capability and overall inference efficiency. However, in scenarios with heterogeneous sequence lengths, Context Parallelism can perform suboptimally and may even lead to overall performance degradation due to reduced efficiency on short sequences. In addition, to better support and optimize ultra-long sequence inputs (e.g., reaching 1M tokens or more), introducing a new partitioning dimension becomes necessary. For ultra-long and variable-length sequence workloads, combining Chunked Pipeline Parallelism (CPP, also referred to as Context Pipeline Parallelism or Sequence Pipeline Parallelism) with an SLO-based scheduling strategy can deliver better end-to-end inference performance. See the reference paper: [2409.17264](https://arxiv.org/abs/2409.17264v4). Since vLLM already supports Chunked Prefill + PP, we plan to further optimize CPP itself. Based on the above paper and the [SGLang implementation](https://lmsys.org/blog/2026-01-15-chunked-pipeline/), our plan includes the following items: 1. Enable asynchronous scheduling for PP to reduce pipeline bubbles. 2. Implement as...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: Introduce a dynamic chunk size mechanism based on empirical formulas or profiling. ### Proposed Change. ### [x] Step 1 & 2: Asynchronous Send and Asynchronous Scheduling We have implemented asynchronous P2P send and con...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ts DCP and is planning to support PCP to improve long-sequence inference capability and overall inference efficiency. However, in scenarios with heterogeneous sequence lengths, Context Parallelism can perform suboptimal...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ttps://arxiv.org/abs/2409.17264v4). Since vLLM already supports Chunked Prefill + PP, we plan to further optimize CPP itself. Based on the above paper and the [SGLang implementation](https://lmsys.org/blog/2026-01-15-ch...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: to improve long-sequence inference capability and overall inference efficiency. However, in scenarios with heterogeneous sequence lengths, Context Parallelism can perform suboptimally and may even lead to overall perfor...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: lated efforts in the community, we would greatly appreciate any shared information. ### [ ] Step 3: Dynamic Chunk Size Mechanism Our main focus at this stage is to develop an efficient and stable dynamic chunk size mech...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
