# vllm-project/vllm#25597: [Bug]: NCCL OOM at 1k concurrency using default memory for DP=16 decode with EPLB and 16 redundant experts

| 字段 | 值 |
| --- | --- |
| Issue | [#25597](https://github.com/vllm-project/vllm/issues/25597) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: NCCL OOM at 1k concurrency using default memory for DP=16 decode with EPLB and 16 redundant experts

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug While running a 1k concurrency test against a 2p2d DP=16 on B200 with `--num-redundant-experts=16`, the decode instance crashes during `rearrange` with: ``` 2025-09-24T03:57:03.905654827Z [2025-09-23 23:57:03] vllm-deepseek-ep-decode-0:1673:9080 [0] include/alloc.h:228 NCCL WARN Cuda failure 2 'out of memory' 2025-09-24T03:57:03.905658582Z vllm-deepseek-ep-decode-0:1673:9080 [0] NCCL INFO transport/p2p.cc:217 -> 1 2025-09-24T03:57:03.905660490Z vllm-deepseek-ep-decode-0:1673:9080 [0] NCCL INFO transport/net.cc:553 -> 1 2025-09-24T03:57:03.905662457Z vllm-deepseek-ep-decode-0:1673:9080 [0] NCCL INFO transport/net.cc:784 -> 1 2025-09-24T03:57:03.906184614Z ... 2025-09-24T03:57:04.477872270Z (EngineCore_DP4 pid=1675) ncclInternalError: Internal check failed. 2025-09-24T03:57:04.477874283Z (EngineCore_DP4 pid=1675) Last error: 2025-09-24T03:57:04.477876249Z (EngineCore_DP4 pid=1675) ncclProxyClientGetFd call to tpRank 7 handle 0x77ed00e001d0 failed : 3 2025-09-24T03:57:04.495062418Z (EngineCore_DP0 pid=1671) Process EngineCore_DP0: 2025-09-24T03:57:04.495794856Z (EngineCore_DP0 pid=1671) Traceback (most recent call last): 2025-09-24T...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: NCCL OOM at 1k concurrency using default memory for DP=16 decode with EPLB and 16 redundant experts bug;stale ### Your current environment ### 🐛 Describe the bug While running a 1k concurrency test against a 2p2d...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 2025-09-24T03:57:04.496371682Z (EngineCore_DP0 pid=1671) with _coalescing_manager(group, device, async_ops=True) as cm: 2025-09-24T03:57:04.496373321Z (EngineCore_DP0 pid=1671) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ibe the bug While running a 1k concurrency test against a 2p2d DP=16 on B200 with `--num-redundant-experts=16`, the decode instance crashes during `rearrange` with: ``` 2025-09-24T03:57:03.905654827Z [2025-09-23 23:57:0...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: [Bug]: NCCL OOM at 1k concurrency using default memory for DP=16 decode with EPLB and 16 redundant experts bug;stale ### Your current environment ### 🐛 Describe the bug While running a 1k concurrency test against a 2p2d...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: t environment ### 🐛 Describe the bug While running a 1k concurrency test against a 2p2d DP=16 on B200 with `--num-redundant-experts=16`, the decode instance crashes during `rearrange` with: ``` 2025-09-24T03:57:03.90565...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
