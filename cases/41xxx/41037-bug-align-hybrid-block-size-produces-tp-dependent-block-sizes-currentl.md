# vllm-project/vllm#41037: [Bug] _align_hybrid_block_size produces TP-dependent block sizes, currently unsupported when local and remote kernel block size mismatch

| 字段 | 值 |
| --- | --- |
| Issue | [#41037](https://github.com/vllm-project/vllm/issues/41037) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | fp8;kernel |
| 症状 | mismatch |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] _align_hybrid_block_size produces TP-dependent block sizes, currently unsupported when local and remote kernel block size mismatch

### Issue 正文摘录

`_align_hybrid_block_size` computes `attn_page_size_1_token` using per-GPU KV heads (`get_num_kv_heads(parallel_config)`), making the inflated logical block size TP-dependent. When prefill and decode use different TP sizes, this causes different kernel block sizes, triggering `block_size_ratio != 1` assertions in the NIXL connector. **Model:** `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8` (`kv_cache_dtype=fp8_e4m3`, `mamba_cache_mode=none`) ## Block size through the pipeline User `--block-size 32`: | TP | After `_align_hybrid_block_size` | After `select_common_block_size` (flash_attn/flashinfer) | After `select_common_block_size` (triton_attn) | |----|-----|-----|-----| | 1 | 4192 | 32 | 4192 | | 2 | 4192 | 32 | 4192 | | 4 | 2112 | 64 | 2112 | ### Why TP=4 differs `num_kv_heads=2` → at TP≥2, `num_kv_heads_per_gpu` clamps to 1, but `mamba_page_size` keeps halving with TP. TP=1/2 both get `ceil(2134016/512) = 4167 → aligned to 4192`. TP=4 gets `ceil(533504/256) = 2084 → aligned to 2112`. ### `_align_hybrid_block_size` inputs | TP | `num_kv_heads_per_gpu` | `attn_page_size_1_token` | `mamba_page_size` | |----|------------------------|--------------------------|-------------------| | 1...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: _align_hybrid_block_size` | After `select_common_block_size` (flash_attn/flashinfer) | After `select_common_block_size` (triton_attn) | |----|-----|-----|-----| | 1 | 4192 | 32 | 4192 | | 2 | 4192 | 32 | 4192 | | 4 | 21...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: n the NIXL connector. **Model:** `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8` (`kv_cache_dtype=fp8_e4m3`, `mamba_cache_mode=none`) ## Block size through the pipeline User `--block-size 32`: | TP | After `_align_hybrid_bl...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug] _align_hybrid_block_size produces TP-dependent block sizes, currently unsupported when local and remote kernel block size mismatch `_align_hybrid_block_size` computes `attn_page_size_1_token` using per-GPU KV head...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: tn_page_size_1_token` using per-GPU KV heads (`get_num_kv_heads(parallel_config)`), making the inflated logical block size TP-dependent. When prefill and decode use different TP sizes, this causes different kernel block...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: lel_config)`), making the inflated logical block size TP-dependent. When prefill and decode use different TP sizes, this causes different kernel block sizes, triggering `block_size_ratio != 1` assertions in the NIXL con...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
