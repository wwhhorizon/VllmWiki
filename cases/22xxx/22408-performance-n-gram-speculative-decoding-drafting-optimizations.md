# vllm-project/vllm#22408: [Performance]: n-gram speculative decoding drafting optimizations

| 字段 | 值 |
| --- | --- |
| Issue | [#22408](https://github.com/vllm-project/vllm/issues/22408) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: n-gram speculative decoding drafting optimizations

### Issue 正文摘录

### Proposal to improve performance n-gram speculative decoding drafting consumes 5-8% critical path time for small models (e.g. opt-125M), and 0.9% for large models (e.g. Llama4 Scout 17B). And the cost would increase linearly when we increase the ngram range (e.g. reducing min_gram or increasing max_gram). With [A draft PR](https://github.com/vllm-project/vllm/pull/22390), we could reduced n-gram speculative decoding drafting cost by 38+%. It mainly consists of 2 changes - improved the time complexity from O(ngram_range*total_tokens) to O(total_tokens) In the following chart, the drafting cost became constant when max-ngram increased. - moved the whole batch drafting to Numba We will create a few PRs to productionize the optimizations. ### Followup: Further optimization We should replace KMP approach with Rabin-Karp or SuffixAutomaton, which should - preprocess input prompts in O(ngram*input_len) and overlap with prefill (so it's not on ciritcal path) - while the critical path drafting cost could be reduced from O(ngram) ### Report of performance regression N/A ### Misc discussion on performance N/A ### Your current environment (if you think it is necessary) ```text The output o...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Performance]: n-gram speculative decoding drafting optimizations performance;stale ### Proposal to improve performance n-gram speculative decoding drafting consumes 5-8% critical path time for small models (e.g. opt-12...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: -gram speculative decoding drafting consumes 5-8% critical path time for small models (e.g. opt-125M), and 0.9% for large models (e.g. Llama4 Scout 17B). And the cost would increase linearly when we increase the ngram r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: speculative decoding drafting consumes 5-8% critical path time for small models (e.g. opt-125M), and 0.9% for large models (e.g. Llama4 Scout 17B). And the cost would increase linearly when we increase the ngram range (...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: drafting cost could be reduced from O(ngram) ### Report of performance regression N/A ### Misc discussion on performance N/A ### Your current environment (if you think it is necessary) ```text The output of `python coll...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: cost would increase linearly when we increase the ngram range (e.g. reducing min_gram or increasing max_gram). With [A draft PR](https://github.com/vllm-project/vllm/pull/22390), we could reduced n-gram speculative deco...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
