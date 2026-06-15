# vllm-project/vllm#31634: [RFC]: Decouple page_size_bytes calculation in AttentionSpec for TPU/RPA Compatibility

| 字段 | 值 |
| --- | --- |
| Issue | [#31634](https://github.com/vllm-project/vllm/issues/31634) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Decouple page_size_bytes calculation in AttentionSpec for TPU/RPA Compatibility

### Issue 正文摘录

### Motivation. In the current vLLM V1 implementation, `AttentionSpec` (in `kv_cache_interface.py`) calculates the `page_size_bytes` as a fixed product of `num_kv_heads`, `head_size`, `dtype`, and `block_size`. The issue: Ragged Paged Attention (RPA) on TPUs often requires the KV cache to be padded to specific byte boundaries (e.g., for XLA memory alignment or specific TPU tiling). * Because page_size_bytes is a @property, it cannot be overridden during initialization. * Backends are currently forced to use "hacky" workarounds like `num_gpu_blocks_override` to trick the system into allocating the correct amount of memory, which leads to technical debt and fragile integration in uLLM. * Multi-host executor (RayExecutor) cannot use `num_gpu_blocks_override` to override num_gpu_blocks. When creating workers across a cluster, `vllm_config` is passed by value (serialized via Ray). The updates made in the `tpu_worker` do not propagate back to the `EngineCore`. ### Proposed Change. Convert page_size_bytes from a @property to a field that is assigned during __post_init__. This allows a backend to either: * Accept the default calculation (platform-agnostic). * Provide a pre-calculated, pad...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [RFC]: Decouple page_size_bytes calculation in AttentionSpec for TPU/RPA Compatibility RFC;stale ### Motivation. In the current vLLM V1 implementation, `AttentionSpec` (in `kv_cache_interface.py`) calculates the `page_s...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _bytes is a @property, it cannot be overridden during initialization. * Backends are currently forced to use "hacky" workarounds like `num_gpu_blocks_override` to trick the system into allocating the correct amount of m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: d Attention (RPA) on TPUs often requires the KV cache to be padded to specific byte boundaries (e.g., for XLA memory alignment or specific TPU tiling). * Because page_size_bytes is a @property, it cannot be overridden d...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: he `page_size_bytes` as a fixed product of `num_kv_heads`, `head_size`, `dtype`, and `block_size`. The issue: Ragged Paged Attention (RPA) on TPUs often requires the KV cache to be padded to specific byte boundaries (e....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
