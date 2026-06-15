# vllm-project/vllm#39734: [Bug]: Scheduler deadlocks when request exceeds KV cache capacity but is within max_model_len

| 字段 | 值 |
| --- | --- |
| Issue | [#39734](https://github.com/vllm-project/vllm/issues/39734) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Scheduler deadlocks when request exceeds KV cache capacity but is within max_model_len

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When a request's token count exceeds the GPU KV cache capacity but is within the configured max_model_len, the request gets stuck at the head of the scheduler's waiting queue and blocks all other inference requests indefinitely. The server remains responsive to non-inference endpoints (e.g. /v1/models) but no generation occurs until the client times out and disconnects. The root cause is in the waiting request scheduling loop in vllm/v1/core/sched/scheduler.py. When scheduler_reserve_full_isl is True (the default), can_fit_full_sequence() returns False for a request that will never fit, and the scheduler breaks out of the loop without popping the request from the queue. On the next scheduling step, it encounters the same request, fails again, and breaks again. This causes head-of-line blocking of all waiting requests. This situation arises naturally with models like Gemma-4-31B that have high per-token KV cache costs (60 layers, large head dimensions). On 2x H100 80GB with TP=2, the KV cache only holds ~76k tokens while max_model_len defaults to 262k. Any request between 76k and 262k tokens triggers the deadlock. Reproduction: 1....

## 现有链接修复摘要

#39828 [V1][Scheduler] Reject impossible waiting requests that exceed KV capacity | #40946 [Bugfix] Cap SWA/chunked-local runtime admission to startup pool-sizing bound

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Scheduler deadlocks when request exceeds KV cache capacity but is within max_model_len bug ### Your current environment ### 🐛 Describe the bug When a request's token count exceeds the GPU KV cache capacity but is
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: high per-token KV cache costs (60 layers, large head dimensions). On 2x H100 80GB with TP=2, the KV cache only holds ~76k tokens while max_model_len defaults to 262k. Any request between 76k and 262k tokens triggers the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: Scheduler deadlocks when request exceeds KV cache capacity but is within max_model_len bug ### Your current environment ### 🐛 Describe the bug When a request's token count exceeds the GPU KV cache capacity but is...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: duler deadlocks when request exceeds KV cache capacity but is within max_model_len bug ### Your current environment ### 🐛 Describe the bug When a request's token count exceeds the GPU KV cache capacity but is within the...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: Scheduler deadlocks when request exceeds KV cache capacity but is within max_model_len bug ### Your current environment ### 🐛 Describe the bug When a request's token count exceeds the GPU KV cache capacity but is...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39828](https://github.com/vllm-project/vllm/pull/39828) | closes_keyword | 0.95 | [V1][Scheduler] Reject impossible waiting requests that exceed KV capacity | Fixes #39734. ## Why this is not duplicate work - checked the current discussion on issue `#39734` on April 14, 2026 - searched open PRs for `39734` and for `KV cache capacity sch |
| [#40946](https://github.com/vllm-project/vllm/pull/40946) | closes_keyword | 0.95 | [Bugfix] Cap SWA/chunked-local runtime admission to startup pool-sizing bound | Fixes #39734 (and the same root cause that motivates #39866 / #40027): on hybrid full + sliding-window models with the pool sized at the startup minimum, runtime admission rejects |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
