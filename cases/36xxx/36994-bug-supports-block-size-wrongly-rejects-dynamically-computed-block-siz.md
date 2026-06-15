# vllm-project/vllm#36994: [Bug]: supports_block_size wrongly rejects dynamically computed block sizes (e.g., Qwen3.5 on ROCm)

| 字段 | 值 |
| --- | --- |
| Issue | [#36994](https://github.com/vllm-project/vllm/issues/36994) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: supports_block_size wrongly rejects dynamically computed block sizes (e.g., Qwen3.5 on ROCm)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In vllm/v1/attention/backend.py, the supports_block_size class method includes an early guard that checks the given `block_size` against a hardcoded whitelist using the BlockSize literal from vllm.config.cache. This early guard incorrectly rejects perfectly valid block sizes that are calculated dynamically by certain model architectures. Raised here: https://github.com/kyuz0/amd-strix-halo-vllm-toolboxes/issues/28#issuecomment-4056712277 For example, Qwen3.5's hybrid architecture triggers HybridAttentionMambaModelConfig, which computes a block_size=1056 to align attention and mamba page sizes. This is a valid size because the Triton attention kernel only requires it to be a multiple of 16 (1056 % 16 == 0). However, because 1056 is not in the hardcoded valid_sizes list, it gets rejected before the Triton kernel even has a chance to run its own capability checks. On NVIDIA platforms, FlashAttention handles this correctly so the issue isn't seen. However, on AMD/ROCm where Triton is the only available backend for this path, this early rejection prevents the model from running. # Expected Behavior The attention backend should defer t...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: _size wrongly rejects dynamically computed block sizes (e.g., Qwen3.5 on ROCm) bug;rocm ### Your current environment ### 🐛 Describe the bug In vllm/v1/attention/backend.py, the supports_block_size class method includes...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: our current environment ### 🐛 Describe the bug In vllm/v1/attention/backend.py, the supports_block_size class method includes an early guard that checks the given `block_size` against a hardcoded whitelist using the Blo...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug]: supports_block_size wrongly rejects dynamically computed block sizes (e.g., Qwen3.5 on ROCm) bug;rocm ### Your current environment ### 🐛 Describe the bug In vllm/v1/attention/backend.py, the supports_block_size c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ports_block_size wrongly rejects dynamically computed block sizes (e.g., Qwen3.5 on ROCm) bug;rocm ### Your current environment ### 🐛 Describe the bug In vllm/v1/attention/backend.py, the supports_block_size class metho...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s. # Proposed Fix Remove the early whitelist check and let the kernel decide if the `block_size` is supported via its get_supported_kernel_block_sizes() method. vllm/v1/attention/backend.py ```python @classmethod def su...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
