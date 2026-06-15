# vllm-project/vllm#24280: [Feature]: decouple attention backend block size from KVCacheManager block size

| 字段 | 值 |
| --- | --- |
| Issue | [#24280](https://github.com/vllm-project/vllm/issues/24280) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: decouple attention backend block size from KVCacheManager block size

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, the attention block size (AKA page size) used in the `KVCacheManager` is also used by the attention backend. Yet, in some cases the `KVCacheManager` and the attention backend have contradicting limitations on the attention page size. For example, in hybrid mamba/attention models the `KVCacheManager` requires the mamba and attention page sizes to match, which might cause large attention page sizes (672 tokens for [nvidia/NVIDIA-Nemotron-Nano-9B-v2](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2)). On the other hand, the FlashInfer attention backend uses TRTLLM FMHA kernels for Blackwell, which require page size up to 128 (see [here](https://github.com/flashinfer-ai/flashinfer/blob/1649e236e414bb8f0a50b6026cad2c430d1047b2/include/flashinfer/trtllm/fmha/fmhaKernels.cuh#L98)). The idea is to decouple the two page sizes. If the `KVCacheManager` requires a page size larger than what is supported by the attention backend, we can create multiple pages for the attention backend from a single `KVCacheManager` page. Concretely, if the `KVCacheManager` needs block_size 1024, and attention backend needs block_size 128, we can pass th...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Feature]: decouple attention backend block size from KVCacheManager block size feature request ### 🚀 The feature, motivation and pitch Currently, the attention block size (AKA page size) used in the `KVCacheManager` is...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ther hand, the FlashInfer attention backend uses TRTLLM FMHA kernels for Blackwell, which require page size up to 128 (see [here](https://github.com/flashinfer-ai/flashinfer/blob/1649e236e414bb8f0a50b6026cad2c430d1047b2...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Feature]: decouple attention backend block size from KVCacheManager block size feature request ### 🚀 The feature, motivation and pitch Currently, the attention block size (AKA page size) used in the `KVCacheManager` is...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: tions on the attention page size. For example, in hybrid mamba/attention models the `KVCacheManager` requires the mamba and attention page sizes to match, which might cause large attention page sizes (672 tokens for [nv...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: uple attention backend block size from KVCacheManager block size feature request ### 🚀 The feature, motivation and pitch Currently, the attention block size (AKA page size) used in the `KVCacheManager` is also used by t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
