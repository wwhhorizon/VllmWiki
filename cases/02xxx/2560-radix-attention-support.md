# vllm-project/vllm#2560: Radix Attention support

| 字段 | 值 |
| --- | --- |
| Issue | [#2560](https://github.com/vllm-project/vllm/issues/2560) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Radix Attention support

### Issue 正文摘录

RadixAttention, a novel technique for automatic KV cache reuse during runtime. Furthermore, RadixAttention is compatible with existing techniques like continuous batching and paged attention. Blog: https://lmsys.org/blog/2024-01-17-sglang/ Paper:https://arxiv.org/abs/2312.07104 Code:https://github.com/sgl-project/sglang ![llama_7b](https://github.com/vllm-project/vllm/assets/1152904/33d5ef34-3528-45c3-904b-a9b4b1262eee)

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: Radix Attention support RadixAttention, a novel technique for automatic KV cache reuse during runtime. Furthermore, RadixAttention is compatible with existing techniques like continuous batching and paged attention. Blo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ://arxiv.org/abs/2312.07104 Code:https://github.com/sgl-project/sglang ![llama_7b](https://github.com/vllm-project/vllm/assets/1152904/33d5ef34-3528-45c3-904b-a9b4b1262eee)

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
