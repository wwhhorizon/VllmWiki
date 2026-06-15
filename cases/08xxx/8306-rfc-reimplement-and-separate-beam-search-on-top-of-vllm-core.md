# vllm-project/vllm#8306: [RFC]: Reimplement and separate beam search on top of vLLM core

| 字段 | 值 |
| --- | --- |
| Issue | [#8306](https://github.com/vllm-project/vllm/issues/8306) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Reimplement and separate beam search on top of vLLM core

### Issue 正文摘录

### Motivation. A rework of https://github.com/vllm-project/vllm/issues/6226 After discussing further with the community, we find that the common use case for beam search is: 1. throughput oriented 2. mainly offline batch inference 3. use one beam search parameter for all the prompts in the batch After discussing with many contributors, we find: because beam search is a **search** algorithm, it conflicts with all the rest **sampling** algorithm. As a result, many features in vllm already directly assert beam search is not used, e.g. https://github.com/vllm-project/vllm/blob/6e36f4fa6ce64619b9ea94c88a157f5783a63a65/vllm/spec_decode/batch_expansion.py#L303-L305 https://github.com/vllm-project/vllm/blob/6e36f4fa6ce64619b9ea94c88a157f5783a63a65/vllm/engine/output_processor/multi_step.py#L100-L103 **keeping beam-search as-is in the codebase, will not benefit current beam search user, as no optimization will target at better beam search performance. What's worse, very few developers understand beam search. Keeping beam-search as-is will not only increase the bugs for beam search as the codebase evolves, but also increase the maintenance cost of all contributors.** in search of a win-win...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: llm-project/vllm/blob/6e36f4fa6ce64619b9ea94c88a157f5783a63a65/vllm/spec_decode/batch_expansion.py#L303-L305 https://github.com/vllm-project/vllm/blob/6e36f4fa6ce64619b9ea94c88a157f5783a63a65/vllm/engine/output_processo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [RFC]: Reimplement and separate beam search on top of vLLM core RFC ### Motivation. A rework of https://github.com/vllm-project/vllm/issues/6226 After discussing further with the community, we find that the common use c...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: the community, we find that the common use case for beam search is: 1. throughput oriented 2. mainly offline batch inference 3. use one beam search parameter for all the prompts in the batch After discussing with many c...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rate and reimplement beam search on top of the vllm core code. to be specific, we can: 1. remove beam search logic from the scheduler 2. add an `LLM.beam_search` interface, that calls the engine to generate 1 tokens wit...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: se computation from the last step so that we don't need to recompute the kv cache of prompt again and again. 2. after separating beam search and the vllm core, they can be optimized individually. The simplified code wil...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
