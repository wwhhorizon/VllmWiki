# vllm-project/vllm#1506: [Question] Why vLLM using float32 bit width when `_check_if_can_support_max_seq_len`?

| 字段 | 值 |
| --- | --- |
| Issue | [#1506](https://github.com/vllm-project/vllm/issues/1506) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Question] Why vLLM using float32 bit width when `_check_if_can_support_max_seq_len`?

### Issue 正文摘录

I checked the size of `cudaDevAttrMaxSharedMemoryPerBlockOptin` on several kinds of GPU, most of them are 101376 bytes, which means vLLM doesn't support model taht context length large than ~24832. But we got lots of model that have 32K 40K or larger context length right now. SO why we need float32 bit width here? How can we fix this issue? Can `float32_bytes` be `model_config.dtype`?

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Question] Why vLLM using float32 bit width when `_check_if_can_support_max_seq_len`? I checked the size of `cudaDevAttrMaxSharedMemoryPerBlockOptin` on several kinds of GPU, most of them are 101376 bytes, which means v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: of GPU, most of them are 101376 bytes, which means vLLM doesn't support model taht context length large than ~24832. But we got lots of model that have 32K 40K or larger context length right now. SO why we need float32...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: t width when `_check_if_can_support_max_seq_len`? I checked the size of `cudaDevAttrMaxSharedMemoryPerBlockOptin` on several kinds of GPU, most of them are 101376 bytes, which means vLLM doesn't support model taht conte...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: upport_max_seq_len`? I checked the size of `cudaDevAttrMaxSharedMemoryPerBlockOptin` on several kinds of GPU, most of them are 101376 bytes, which means vLLM doesn't support model taht context length large than ~24832....

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
