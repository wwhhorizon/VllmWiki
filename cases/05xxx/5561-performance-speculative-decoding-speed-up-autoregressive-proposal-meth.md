# vllm-project/vllm#5561: [Performance] [Speculative decoding] Speed up autoregressive proposal methods by making sampler CPU serialization optional

| 字段 | 值 |
| --- | --- |
| Issue | [#5561](https://github.com/vllm-project/vllm/issues/5561) |
| 状态 | closed |
| 标签 | performance;speculative-decoding |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance] [Speculative decoding] Speed up autoregressive proposal methods by making sampler CPU serialization optional

### Issue 正文摘录

## Background Speculative decoding leverages the ability to cheaply generate proposals, and cheaply verify them to achieve speedup for memory-bound inference. Different methods of speculative decoding explore the frontier between cost of proposal, alignment with the target model, and cost of verification. For example, Medusa produces very cheap proposals, but the quality of the proposals are strictly less than Eagle because the heads do not have access to the previous proposals. Eagle on the other hand pays more for the proposals by sampling autoregressively instead of 1-shot, but it brings the benefit of higher-quality proposals. At the end of the day, what the user cares about will dictate which speculative technique is used. vLLM's job is to provide them with the option for best speedup for their use case. Draft-model, EAGLE, and MLPSpeculator rely on autoregressive proposals. This means their top-1 proposals are higher-quality than Medusa, which gives vLLM an ITL reduction that is more flops-efficient than Medusa. This is what our speculative decoding efforts are focused on first -- afterward, we can support top-k proposals with Medusa so users who care more about ITL reductio...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Performance] [Speculative decoding] Speed up autoregressive proposal methods by making sampler CPU serialization optional performance;speculative-decoding ## Background Speculative decoding leverages the ability to che...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ty than Medusa, which gives vLLM an ITL reduction that is more flops-efficient than Medusa. This is what our speculative decoding efforts are focused on first -- afterward, we can support top-k proposals with Medusa so...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: explore the frontier between cost of proposal, alignment with the target model, and cost of verification. For example, Medusa produces very cheap proposals, but the quality of the proposals are strictly less than Eagle...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ative decoding efforts are focused on first -- afterward, we can support top-k proposals with Medusa so users who care more about ITL reduction can use vLLM. ## Speedup autoregressive proposal methods This issue is to s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: n are pure overhead in speculative decoding. ### How much overhead? In [profiling vLLM](https://docs.google.com/spreadsheets/d/1GMyebF9XwlLJzpkpRxZrzUNcQTSibHlQ7zifldaDPtI/edit#gid=0), I found that copy + serialization...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
