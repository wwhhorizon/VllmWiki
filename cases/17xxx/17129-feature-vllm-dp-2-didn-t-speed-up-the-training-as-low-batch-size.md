# vllm-project/vllm#17129: [Feature]: vLLM DP=2 didn't speed up the training as low batch size.

| 字段 | 值 |
| --- | --- |
| Issue | [#17129](https://github.com/vllm-project/vllm/issues/17129) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: vLLM DP=2 didn't speed up the training as low batch size.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi team, First of all, thanks for the recent efforts, especially to @qgallouedec, for supporting the new `data_parallel_size` feature in vLLM. I tested the `vllm-serve-dp` branch with `data_parallel_size=2`, and confirmed that it launches two processes for rollouts as expected. Great work! However, **the speedup of having `data_parallel_size=2` isn't quite as significant as I hoped**. In my previous setup using a single GPU, I was achieving around 4000–6000 toks/s generation. With `data_parallel_size=2`, this drops to only 1000–1200 tokens/s per process, which results in an overall slower or comparable throughput. It seems that the GPUs may be underutilized, possibly waiting on input (prompts/questions) to arrive. I suspect the issue could be mitigated by **allowing larger batch sizes for generation in the vLLM server, while keeping a smaller batch size for gradient calculations to avoid OOM errors.** I’m reporting this primarily for visibility, and I’m confident that the team can fine-tune the implementation to achieve near-linear speedup. Looking forward to seeing future improvements! Thanks again for your hard work! ### Alternatives _No r...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ng larger batch sizes for generation in the vLLM server, while keeping a smaller batch size for gradient calculations to avoid OOM errors.** I’m reporting this primarily for visibility, and I’m confident that the team c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ture]: vLLM DP=2 didn't speed up the training as low batch size. feature request ### 🚀 The feature, motivation and pitch Hi team, First of all, thanks for the recent efforts, especially to @qgallouedec, for supporting t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: llouedec, for supporting the new `data_parallel_size` feature in vLLM. I tested the `vllm-serve-dp` branch with `data_parallel_size=2`, and confirmed that it launches two processes for rollouts as expected. Great work!...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: on and pitch Hi team, First of all, thanks for the recent efforts, especially to @qgallouedec, for supporting the new `data_parallel_size` feature in vLLM. I tested the `vllm-serve-dp` branch with `data_parallel_size=2`...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: r, while keeping a smaller batch size for gradient calculations to avoid OOM errors.** I’m reporting this primarily for visibility, and I’m confident that the team can fine-tune the implementation to achieve near-linear...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
