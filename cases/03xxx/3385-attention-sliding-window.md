# vllm-project/vllm#3385: Attention sliding window

| 字段 | 值 |
| --- | --- |
| Issue | [#3385](https://github.com/vllm-project/vllm/issues/3385) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Attention sliding window

### Issue 正文摘录

In Hugging Face "eager" Mistral implementation, a sliding window of size 2048 will mask 2049 tokens. This is also true for flash attention. In the current vLLM implementation a window of 2048 will mask 2048 tokens: ``` import torch from xformers.ops.fmha.attn_bias import BlockDiagonalCausalMask attn_bias = BlockDiagonalCausalMask.from_seqlens([4096]) attn_bias = attn_bias.make_local_attention(2048) mask = attn_bias._create_block_mask([4096, 4096]) print(torch.sum(mask == 0, dim=1)) ``` **Output: tensor([ 1, 2, 3, ..., 2048, 2048, 2048])** The output should be: **tensor([ 1, 2, 3, ..., 2049, 2049, 2049])** Context: https://github.com/huggingface/transformers/issues/29623

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sliding window of size 2048 will mask 2049 tokens. This is also true for flash attention. In the current vLLM implementation a window of 2048 will mask 2048 tokens: ``` import torch from xformers.ops.fmha.attn_bias impo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: current vLLM implementation a window of 2048 will mask 2048 tokens: ``` import torch from xformers.ops.fmha.attn_bias import BlockDiagonalCausalMask attn_bias = BlockDiagonalCausalMask.from_seqlens([4096]) attn_bias = a...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: k 2048 tokens: ``` import torch from xformers.ops.fmha.attn_bias import BlockDiagonalCausalMask attn_bias = BlockDiagonalCausalMask.from_seqlens([4096]) attn_bias = attn_bias.make_local_attention(2048) mask = attn_bias....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 1, 2, 3, ..., 2049, 2049, 2049])** Context: https://github.com/huggingface/transformers/issues/29623
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Attention sliding window stale In Hugging Face "eager" Mistral implementation, a sliding window of size 2048 will mask 2049 tokens. This is also true for flash attention. In the current vLLM implementation a window of 2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
