# vllm-project/vllm#14450: [Performance]: LoRA is not taken into account when determining the number of KV cache blocks

| 字段 | 值 |
| --- | --- |
| Issue | [#14450](https://github.com/vllm-project/vllm/issues/14450) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: LoRA is not taken into account when determining the number of KV cache blocks

### Issue 正文摘录

### Proposal to improve performance I noticed that when LLMengine calls the determine_KV_cache_blocks function, only the GPU memory occupied by the model weight and activation is considered. But when LoRA is enabled, LoRA will also occupy a part of the memory. In my experiment, using different LoRa Rank and Max LoRas did not affect the number of kv cache blocks which is decided in the profiling, this resullt supported my suspicions. I'd like to know the reason behind this design, it's a bug? Or does vLLM really not want to take it into account at the moment to avoid wasting memory? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: formance]: LoRA is not taken into account when determining the number of KV cache blocks performance ### Proposal to improve performance I noticed that when LLMengine calls the determine_KV_cache_blocks function, only t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: Ras did not affect the number of kv cache blocks which is decided in the profiling, this resullt supported my suspicions. I'd like to know the reason behind this design, it's a bug? Or does vLLM really not want to take...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nk and Max LoRas did not affect the number of kv cache blocks which is decided in the profiling, this resullt supported my suspicions. I'd like to know the reason behind this design, it's a bug? Or does vLLM really not...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: : LoRA is not taken into account when determining the number of KV cache blocks performance ### Proposal to improve performance I noticed that when LLMengine calls the determine_KV_cache_blocks function, only the GPU me...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
