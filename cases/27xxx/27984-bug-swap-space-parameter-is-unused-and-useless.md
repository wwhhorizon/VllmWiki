# vllm-project/vllm#27984: [Bug]: `swap_space` parameter is unused and useless

| 字段 | 值 |
| --- | --- |
| Issue | [#27984](https://github.com/vllm-project/vllm/issues/27984) |
| 状态 | closed |
| 标签 | bug;good first issue;keep-open |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `swap_space` parameter is unused and useless

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Since the deprecation of `best_of` sampling in #13997 (see also #13361), the `swap_space` parameter is useless and unused in the codebase. To make matters worse, it seems `best_of` was never properly implemented because `num_cpu_blocks` in `EngineCore::_initialize_kv_caches()` is hard coded to zero at `vllm/v1/engine/core.py:252` and always has been according to the git history. This is probably why `best_of` had no usage -- it never worked and has always been disabled. I propose to finish deprecating `best_of` and remove the `swap_space` parameter entirely. It's quite confusing as there are other inference technologies (e.g. LMCache) that could in principle be using CPU memory for caching pieces of the KV cache (and I think that's a good idea FWIW). But that's not what `swap_space` does, or ever did. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: there are other inference technologies (e.g. LMCache) that could in principle be using CPU memory for caching pieces of the KV cache (and I think that's a good idea FWIW). But that's not what `swap_space` does, or ever...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: id. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: e) that could in principle be using CPU memory for caching pieces of the KV cache (and I think that's a good idea FWIW). But that's not what `swap_space` does, or ever did. ### Before submitting a new issue... - [x] Mak...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: orse, it seems `best_of` was never properly implemented because `num_cpu_blocks` in `EngineCore::_initialize_kv_caches()` is hard coded to zero at `vllm/v1/engine/core.py:252` and always has been according to the git hi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
