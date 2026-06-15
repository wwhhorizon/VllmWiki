# vllm-project/vllm#2039: [FEATURE REQUEST] SparQ Attention

| 字段 | 值 |
| --- | --- |
| Issue | [#2039](https://github.com/vllm-project/vllm/issues/2039) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [FEATURE REQUEST] SparQ Attention

### Issue 正文摘录

A newly released paper, [SparQ Attention: Bandwidth-Efficient LLM Inference](https://arxiv.org/pdf/2312.04985.pdf), suggests a method for increasing the inference throughput of LLMs up to 8x by reducing the memory bandwidth requirements within the attention blocks through selective fetching of the cached history. A sample implementation looks like this: ```py from torch import abs, softmax, sqrt, tensor, topk def gather(t, dim, i): dim += (dim < 0) * t.ndim return t.gather(dim, i.expand(*t.shape[:dim], i.shape[dim], *t.shape[dim + 1 :])) def attn(Q, K, V, M): s = (Q @ K.transpose(-1, -2)) / sqrt(tensor(Q.shape[-1])) + M return softmax(s, dim=-) @ V def sparq_attn(Q, K, V, V_mean, M, r, k): # Approximate attention scores using r largest components of Q i1 = topk(abs(Q), r, -1).indices Q_hat, K_hat = gather(Q, -1, i1), gather(K, -1, i1) scale = sqrt( Q.shape[-1] * abs(Q_hat).sum(dim=-1, keepdim=True) / abs(Q).sum(dim=-1, keepdim=True) ) s_hat = softmax(Q_hat @ K_hat.transpose(-1, -2) / scale + M, dim=-1) # Gather top_k positions based on approximate attention scores and run attention i2 = topk(s_hat, k, -1).indices iKV = i2[..., 0, :, None] K, V, M = gather(K, -2, iKV), gather(V, -2...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: re request;stale A newly released paper, [SparQ Attention: Bandwidth-Efficient LLM Inference](https://arxiv.org/pdf/2312.04985.pdf), suggests a method for increasing the inference throughput of LLMs up to 8x by reducing...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [FEATURE REQUEST] SparQ Attention feature request;stale A newly released paper, [SparQ Attention: Bandwidth-Efficient LLM Inference](https://arxiv.org/pdf/2312.04985.pdf), suggests a method for increasing the inference...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: -1).indices Q_hat, K_hat = gather(Q, -1, i1), gather(K, -1, i1) scale = sqrt( Q.shape[-1] * abs(Q_hat).sum(dim=-1, keepdim=True) / abs(Q).sum(dim=-1, keepdim=True) ) s_hat = softmax(Q_hat @ K_hat.transpose(-1, -2) / sca...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: to 8x by reducing the memory bandwidth requirements within the attention blocks through selective fetching of the cached history. A sample implementation looks like this: ```py from torch import abs, softmax, sqrt, tens...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: on looks like this: ```py from torch import abs, softmax, sqrt, tensor, topk def gather(t, dim, i): dim += (dim < 0) * t.ndim return t.gather(dim, i.expand(*t.shape[:dim], i.shape[dim], *t.shape[dim + 1 :])) def attn(Q,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
