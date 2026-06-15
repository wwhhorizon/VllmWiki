# vllm-project/vllm#39760: [RFC]: Async Failure Notification for Fault Tolerant EP Kernels

| 字段 | 值 |
| --- | --- |
| Issue | [#39760](https://github.com/vllm-project/vllm/issues/39760) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;moe;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;kernel;moe |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [RFC]: Async Failure Notification for Fault Tolerant EP Kernels

### Issue 正文摘录

# [RFC]: Async Failure Notification for Fault Tolerant EP Kernels ### Motivation. Fault-tolerant EP kernels (e.g. NIXL-EP) detect rank failures on the GPU — via a per-rank integer mask written atomically on timeout — without any CPU involvement. The CPU only learns about a failure if it explicitly reads that mask back from VRAM, which forces a GPU→CPU sync. The problem is not detection speed. The problem is **when and how often that sync is paid**. When [`SchedulerConfig.async_scheduling = True`](https://github.com/vllm-project/vllm/blob/54b0578adacd0413b18c0f59948dabc7533a6524/vllm/config/scheduler.py#L144), vLLM pipelines CPU scheduling with GPU execution: the CPU schedules pass N+1 while the GPU runs pass N. A blocking GPU→CPU sync collapses that overlap and eliminates the throughput benefit of async scheduling — even during healthy operation when no rank has failed. The natural "check after every forward pass" approach pays this cost on every pass: ```python query_mask_buffer(...) # enqueues a CUDA copy kernel active_ranks.copy_(...) # still a GPU tensor torch.equal(active_ranks, ...) # blocks — drains the CUDA stream, crosses PCIe ``` As the NIXL team noted: > "Raising a form...

## 现有链接修复摘要

#38862 [EP] Fault tolerance: automatic elastic scale-down on DP engine death

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: : ``` Option A — inside All2AllManagerBase.dispatch() [recommended]: MoE layer N: dispatch → experts → combine ← failure detected MoE layer N+1: dispatch ← check here → raise EPRankFailureError stops here; remaining lay...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: hout any CPU involvement. The CPU only learns about a failure if it explicitly reads that mask back from VRAM, which forces a GPU→CPU sync. The problem is not detection speed. The problem is **when and how often that sy...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: s cost on every pass: ```python query_mask_buffer(...) # enqueues a CUDA copy kernel active_ranks.copy_(...) # still a GPU tensor torch.equal(active_ranks, ...) # blocks — drains the CUDA stream, crosses PCIe ``` As the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: speed. The problem is **when and how often that sync is paid**. When [`SchedulerConfig.async_scheduling = True`](https://github.com/vllm-project/vllm/blob/54b0578adacd0413b18c0f59948dabc7533a6524/vllm/config/scheduler.p...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ass N. A blocking GPU→CPU sync collapses that overlap and eliminates the throughput benefit of async scheduling — even during healthy operation when no rank has failed. The natural "check after every forward pass" appro...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38862](https://github.com/vllm-project/vllm/pull/38862) | mentioned | 0.45 | [EP] Fault tolerance: automatic elastic scale-down on DP engine death | er_ptr` to enumerate all failed rank indices. the recovery path in pr #38862 already handles a list of failed ranks. ### cc list. @itayalroy @fangyuchu @tylermsmith @sagemoore ###… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
