# vllm-project/vllm#2767: Import FlashInfer: 3x faster PagedAttention than vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#2767](https://github.com/vllm-project/vllm/issues/2767) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Import FlashInfer: 3x faster PagedAttention than vLLM

### Issue 正文摘录

It looks like vLLM could directly import the PagedAttention kernels from FlashInfer to support GQA. "*For batch GQA decoding attention, FlashInfer w/ Tensor Cores is 3x faster than vLLM PagaAttention when batch_size=64.*" @WoosukKwon https://github.com/flashinfer-ai/flashinfer/ https://flashinfer.ai/2024/02/02/introduce-flashinfer.html ![image](https://github.com/vllm-project/vllm/assets/27340033/48d40b10-a5d0-4ea3-9c9f-53cc8a7bca4a)

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: Import FlashInfer: 3x faster PagedAttention than vLLM It looks like vLLM could directly import the PagedAttention kernels from FlashInfer to support GQA. "*For batch GQA decoding attention, FlashInfer w/ Tensor Cores is...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Import FlashInfer: 3x faster PagedAttention than vLLM It looks like vLLM could directly import the PagedAttention kernels from FlashInfer to support GQA. "*For batch GQA decoding attention, FlashInfer w/ Tensor Cores is

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
