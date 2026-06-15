# vllm-project/vllm#40691: [Bug]: The KV cache size log is wrong for Qwen3.5

| 字段 | 值 |
| --- | --- |
| Issue | [#40691](https://github.com/vllm-project/vllm/issues/40691) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The KV cache size log is wrong for Qwen3.5

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Run: `vllm serve Qwen3.5-27B --trust-remote-code --max-model-len 32768 --max-num-seqs 16 --max-num-batched-token 16384 --load-format dummy ` The log as: `INFO [kv_cache_utils.py:1319] GPU KV cache size: 290,864 tokens` `INFO [kv_cache_utils.py:1324] Maximum concurrency for 32,768 tokens per request: 33.04x` Issue: The maximum concurrency * max_model_ken is not equal GPU KV cache size. The calculation of GPU KV cache size has two simplifying assumptions for hybrid models, both of which may introduce errors: 1. num-blocks//len (kv_cache_groups): assuming that blocks are evenly distributed to each group, but in reality, blocks are shared (all groups in the hybrid model share the same tensor pool) 2. min-blocksize: using the minimum blocksize conversion, for hybrid models with large differences in blocksizes such as full attention+Mamba, the result deviation is significant My Qustions： Can I use `maximum concurrency * max_model_ken` as the right `GPU KV cache size` ? Is it necessary to fix this erroneous log to avoid ambiguity? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked th...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: The KV cache size log is wrong for Qwen3.5 bug ### Your current environment ### 🐛 Describe the bug Run: `vllm serve Qwen3.5-27B --trust-remote-code --max-model-len 32768 --max-num-seqs 16 --max-num-batched-token...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: the same tensor pool) 2. min-blocksize: using the minimum blocksize conversion, for hybrid models with large differences in blocksizes such as full attention+Mamba, the result deviation is significant My Qustions： Can I...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ty? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: The KV cache size log is wrong for Qwen3.5 bug ### Your current environment ### 🐛 Describe the bug Run: `vllm serve Qwen3.5-27B --trust-remote-code --max-model-len 32768 --max-num-seqs 16 --max-num-batched-token...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ssumptions for hybrid models, both of which may introduce errors: 1. num-blocks//len (kv_cache_groups): assuming that blocks are evenly distributed to each group, but in reality, blocks are shared (all groups in the hyb...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
