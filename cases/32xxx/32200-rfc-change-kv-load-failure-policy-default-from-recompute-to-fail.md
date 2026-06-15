# vllm-project/vllm#32200: [RFC]: Change `kv_load_failure_policy` Default from "recompute" to "fail"

| 字段 | 值 |
| --- | --- |
| Issue | [#32200](https://github.com/vllm-project/vllm/issues/32200) |
| 状态 | open |
| 标签 | RFC;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Change `kv_load_failure_policy` Default from "recompute" to "fail"

### Issue 正文摘录

### Motivation. In disaggregated prefill setups, the `kv_load_failure_policy` controls how the system handles failures when the decode instance loads KV cache blocks from the prefill instance. Currently, the default is `"recompute"`, which recomputes failed blocks on the decode instance. This may lead to a drop in performance: 1. **Wrong instance, wrong configuration**: Decode instances use low-latency optimizations (e.g., DeepGemm low-latency mode). Recomputing prefill work on decode instances with decode-optimized settings is inefficient and surfaces and amplifies some of the co-location limitations (see next point). 2. **Interference**: Prefill recomputation on decode instances increases tail latency for ongoing decode requests (https://hao-ai-lab.github.io/blogs/distserve-retro/). This will result in higher variance/jitter in tracked metrics such as ITL. Changing the default to `"fail"` will: - Prevent performance jitter by avoiding recomputation on decode instances. - Surface infrastructure issues immediately via request failures. - Improve observability leading to a more stable "observation dashboard", making it easier to spot changes in traffic (arguably main drive). ### Pr...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: : Change `kv_load_failure_policy` Default from "recompute" to "fail" RFC;stale ### Motivation. In disaggregated prefill setups, the `kv_load_failure_policy` controls how the system handles failures when the decode insta...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: edback Period. _No response_ ### CC List. @sdavidbd @wseaton @tlrmchlsmth @hasB4K ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and as...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: controls how the system handles failures when the decode instance loads KV cache blocks from the prefill instance. Currently, the default is `"recompute"`, which recomputes failed blocks on the decode instance. This may...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: e: 1. **Wrong instance, wrong configuration**: Decode instances use low-latency optimizations (e.g., DeepGemm low-latency mode). Recomputing prefill work on decode instances with decode-optimized settings is inefficient...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: prefill work on decode instances with decode-optimized settings is inefficient and surfaces and amplifies some of the co-location limitations (see next point). 2. **Interference**: Prefill recomputation on decode instan...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
