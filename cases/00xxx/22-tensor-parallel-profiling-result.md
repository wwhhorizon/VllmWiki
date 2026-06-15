# vllm-project/vllm#22: Tensor Parallel profiling result

| 字段 | 值 |
| --- | --- |
| Issue | [#22](https://github.com/vllm-project/vllm/issues/22) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Tensor Parallel profiling result

### Issue 正文摘录

Will update the profiling results in this PR. ## BS=8, input_len=32, output_len=128 ``` OPT-13B TP 1: 3.5404738585154214 seconds TP 2: 4.742188215255737 seconds TP 4: 4.907034238179524 seconds OPT-30B TP 1: OOM TP 2: 5.9848620891571045 seconds TP 4: 5.943212985992432 seconds ```

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: 4.742188215255737 seconds TP 4: 4.907034238179524 seconds OPT-30B TP 1: OOM TP 2: 5.9848620891571045 seconds TP 4: 5.943212985992432 seconds ```
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Tensor Parallel profiling result Will update the profiling results in this PR. ## BS=8, input_len=32, output_len=128 ``` OPT-13B TP 1: 3.5404738585154214 seconds TP 2: 4.742188215255737 seconds TP 4: 4.907034238179524 s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
