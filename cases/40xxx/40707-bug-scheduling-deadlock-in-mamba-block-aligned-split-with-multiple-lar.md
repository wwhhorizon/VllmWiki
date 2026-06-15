# vllm-project/vllm#40707: [Bug]: Scheduling deadlock in _mamba_block_aligned_split with multiple large multimodal inputs on hybrid Mamba models

| 字段 | 值 |
| --- | --- |
| Issue | [#40707](https://github.com/vllm-project/vllm/issues/40707) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Scheduling deadlock in _mamba_block_aligned_split with multiple large multimodal inputs on hybrid Mamba models

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Description When serving `Qwen/Qwen3.5-35B-A3B` (a hybrid model with FullAttention + GatedDeltaNet layers) with default `max_num_batched_tokens=8192`, sending a request containing **two or more 3024×4032 images** causes the engine to hang permanently. Both GPUs show ~89% memory utilization but 0% compute utilization. The request never completes and the engine never recovers. One image or multiple small (360p) images work fine. ### Root Cause The deadlock arises from the interaction of three mechanisms: 1. **Encoder cache capacity**: With `max_num_batched_tokens=8192`, the final `encoder_cache_size = max(scheduler_config.encoder_cache_size, max_tokens_per_mm_item) = max(8192, 16384) = 16,384` (see `compute_mm_encoder_budget` in `encoder_cache_manager.py`). Each 3024×4032 image produces ~11,844 placeholder tokens (Qwen3.5-35B-A3B uses `patch_size=16`, `merge_size=2`, `factor=32`; after `smart_resize` the image becomes 3008×4032, yielding `252×188/4 = 11,844` vision tokens). The cache can hold **one** image (11,844 ≤ 16,384) but **not two** simultaneously (23,688 > 16,384). 2. **Chunked prefill with encoder inputs**: During chun...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Scheduling deadlock in _mamba_block_aligned_split with multiple large multimodal inputs on hybrid Mamba models bug ### Your current environment ### 🐛 Describe the bug ### Description When serving `Qwen/Qwen3.5-35...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ]: Scheduling deadlock in _mamba_block_aligned_split with multiple large multimodal inputs on hybrid Mamba models bug ### Your current environment ### 🐛 Describe the bug ### Description When serving `Qwen/Qwen3.5-35B-A3...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: arises from the interaction of three mechanisms: 1. **Encoder cache capacity**: With `max_num_batched_tokens=8192`, the final `encoder_cache_size = max(scheduler_config.encoder_cache_size, max_tokens_per_mm_item) = max(...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: st never completes and the engine never recovers. One image or multiple small (360p) images work fine. ### Root Cause The deadlock arises from the interaction of three mechanisms: 1. **Encoder cache capacity**: With `ma...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: deadlock arises from the interaction of three mechanisms: 1. **Encoder cache capacity**: With `max_num_batched_tokens=8192`, the final `encoder_cache_size = max(scheduler_config.encoder_cache_size, max_tokens_per_mm_ite...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
