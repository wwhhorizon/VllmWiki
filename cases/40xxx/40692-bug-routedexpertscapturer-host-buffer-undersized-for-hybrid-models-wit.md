# vllm-project/vllm#40692: [Bug]: RoutedExpertsCapturer host buffer undersized for hybrid models with multiple KV cache groups

| 字段 | 值 |
| --- | --- |
| Issue | [#40692](https://github.com/vllm-project/vllm/issues/40692) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: RoutedExpertsCapturer host buffer undersized for hybrid models with multiple KV cache groups

### Issue 正文摘录

## Your current environment - vLLM version: 0.18.1.dev0 (commit bcf2be961) - Platform: Ascend NPU (**but the bug is in platform-independent code**) - Model: Qwen3.5-35B-A3B (MoE + Mamba hybrid, 2 KV cache groups) - Config: `--tensor-parallel-size 4 --enable-expert-parallel --enable-return-routed-experts` ## 🐛 Describe the bug `RoutedExpertsCapturer.init_buffer()` is called with an undersized `max_num_kv_tokens` when the model has **multiple KV cache groups** (e.g. attention + mamba). This causes an `IndexError` during stress testing under concurrent load. ### Root cause In [`gpu_model_runner.py:init_routed_experts_capturer()`](https://github.com/vllm-project/vllm/blob/main/vllm/v1/worker/gpu_model_runner.py#L6799-L6827), the host buffer size is calculated as: ```python num_groups = len(self.kv_cache_config.kv_cache_groups) self.max_num_kv_tokens = ( self.kv_cache_config.num_blocks // num_groups ) * min_block_size ``` This assumes each KV cache group uses at most `num_blocks // num_groups` blocks. However, block IDs are allocated from a **single shared `BlockPool`** spanning `[0, num_blocks)`. The slot mapping is computed as: ```python slot_ids = block_numbers * block_size + local_...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: xpertsCapturer host buffer undersized for hybrid models with multiple KV cache groups ## Your current environment - vLLM version: 0.18.1.dev0 (commit bcf2be961) - Platform: Ascend NPU (**but the bug is in platform-indep...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: RoutedExpertsCapturer host buffer undersized for hybrid models with multiple KV cache groups ## Your current environment - vLLM version: 0.18.1.dev0 (commit bcf2be961) - Platform: Ascend NPU (**but the bug is in...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: models with multiple KV cache groups ## Your current environment - vLLM version: 0.18.1.dev0 (commit bcf2be961) - Platform: Ascend NPU (**but the bug is in platform-independent code**) - Model: Qwen3.5-35B-A3B (MoE + Ma...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: RoutedExpertsCapturer host buffer undersized for hybrid models with multiple KV cache groups ## Your current environment - vLLM version: 0.18.1.dev0 (commit bcf2be961) - Platform: Ascend NPU (**but the bug is in...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: pace regardless of how blocks are distributed across groups. ### How to reproduce Run any hybrid model (attention + mamba layers, i.e. 2+ KV cache groups) with `--enable-return-routed-experts` under concurrent load. The...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
