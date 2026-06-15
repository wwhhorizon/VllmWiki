# vllm-project/vllm#1880: [Performance] Use optimized kernels for MQA/GQA

| 字段 | 值 |
| --- | --- |
| Issue | [#1880](https://github.com/vllm-project/vllm/issues/1880) |
| 状态 | closed |
| 标签 | help wanted;performance;stale |
| 评论 | 34; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance] Use optimized kernels for MQA/GQA

### Issue 正文摘录

In theory, MQA/GQA can reduce memory bandwidth for reading KV cache and enable using TensorCore for the dot products in attention mechanism. However, this benefit can be only realized when using optimized kernels that vLLM does not have at the moment. 1. For prefill, vLLM explicitly expands the incoming keys and values before running the attention op: https://github.com/vllm-project/vllm/blob/e5452ddfd6e9a08d5e15bd81a010934550b9b507/vllm/model_executor/layers/attention.py#L121-L128 because xformers (nor PyTorch SDPA) does not support MQA/GQA at the moment. This is bad for performance since 1) it causes extra overhead of expanding the tensor, and 2) the attention kernel cannot leverage the advantage described above. While [FlashAttention](https://github.com/Dao-AILab/flash-attention#how-to-use-flashattention) efficiently supports MQA/GQA, we need to use it carefully since it does not cover all GPUs/data types/head sizes that xformers supports. 2. For decode, vLLM's current paged attention kernel also does not leverage the benefits of MQA/GQA. To enjoy the benefit, we need to either significantly rewrite the paged attention kernel, or modify the FlashAttention kernel to support page...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Performance] Use optimized kernels for MQA/GQA help wanted;performance;stale In theory, MQA/GQA can reduce memory bandwidth for reading KV cache and enable using TensorCore for the dot products in attention mechanism....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: e attention kernel cannot leverage the advantage described above. While [FlashAttention](https://github.com/Dao-AILab/flash-attention#how-to-use-flashattention) efficiently supports MQA/GQA, we need to use it carefully...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ernels that vLLM does not have at the moment. 1. For prefill, vLLM explicitly expands the incoming keys and values before running the attention op: https://github.com/vllm-project/vllm/blob/e5452ddfd6e9a08d5e15bd81a0109...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: che and enable using TensorCore for the dot products in attention mechanism. However, this benefit can be only realized when using optimized kernels that vLLM does not have at the moment. 1. For prefill, vLLM explicitly...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ormance;stale In theory, MQA/GQA can reduce memory bandwidth for reading KV cache and enable using TensorCore for the dot products in attention mechanism. However, this benefit can be only realized when using optimized...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
