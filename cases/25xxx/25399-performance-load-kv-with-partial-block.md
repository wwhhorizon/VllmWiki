# vllm-project/vllm#25399: [Performance]: Load KV with partial block

| 字段 | 值 |
| --- | --- |
| Issue | [#25399](https://github.com/vllm-project/vllm/issues/25399) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Load KV with partial block

### Issue 正文摘录

### Proposal to improve performance In PD disaggregation, the decoder's KV cache-pulling logic currently requests only full blocks. Partial blocks are ignored, forcing the system to perform a redundant prefill computation to regenerate the missing KV cache for those tokens. This results in unnecessary computational overhead and increased latency. ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Performance]: Load KV with partial block performance;stale ### Proposal to improve performance In PD disaggregation, the decoder's KV cache-pulling logic currently requests only full blocks. Partial blocks are ignored,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: tokens. This results in unnecessary computational overhead and increased latency. ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ogic currently requests only full blocks. Partial blocks are ignored, forcing the system to perform a redundant prefill computation to regenerate the missing KV cache for those tokens. This results in unnecessary comput...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ### Proposal to improve performance In PD disaggregation, the decoder's KV cache-pulling logic currently requests only full blocks. Partial blocks are ignored, forcing the system to perform a redundant prefill computati...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
