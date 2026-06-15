# vllm-project/vllm#3359: FlashAttentionBackend only supports head sizes supported by xformers

| 字段 | 值 |
| --- | --- |
| Issue | [#3359](https://github.com/vllm-project/vllm/issues/3359) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> FlashAttentionBackend only supports head sizes supported by xformers

### Issue 正文摘录

`FlashAttentionBackend` currently only supports head sizes supported by `XFormersBackend`, specifically `[64, 80, 96, 112, 128, 256]`. Is there any reason to only support these head sizes with flash attention? If not, I can open a PR to remove this constraint (flash should support all dimensions up to 256) so that smaller models or those with unsupported head sizes can be used with vLLM w/flash attention. ```python suppored_head_sizes = PagedAttentionImpl.get_supported_head_sizes() if head_size not in suppored_head_sizes: raise ValueError( f"Head size {head_size} is not supported by PagedAttention. " f"Supported head sizes are: {suppored_head_sizes}.") ```

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: FlashAttentionBackend only supports head sizes supported by xformers `FlashAttentionBackend` currently only supports head sizes supported by `XFormersBackend`, specifically `[64, 80, 96, 112, 128, 256]`. Is there any rea
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: d` currently only supports head sizes supported by `XFormersBackend`, specifically `[64, 80, 96, 112, 128, 256]`. Is there any reason to only support these head sizes with flash attention? If not, I can open a PR to rem...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: this constraint (flash should support all dimensions up to 256) so that smaller models or those with unsupported head sizes can be used with vLLM w/flash attention. ```python suppored_head_sizes = PagedAttentionImpl.get...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: nstraint (flash should support all dimensions up to 256) so that smaller models or those with unsupported head sizes can be used with vLLM w/flash attention. ```python suppored_head_sizes = PagedAttentionImpl.get_suppor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
