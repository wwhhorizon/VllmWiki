# vllm-project/vllm#6323: [Feature]: Hybrid Attention  

| 字段 | 值 |
| --- | --- |
| Issue | [#6323](https://github.com/vllm-project/vllm/issues/6323) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Hybrid Attention  

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Some models(Gemma2 ...) uses hybrid attention, global-attention + local-attention. But vllm currently ignores local-attn and uses global-attn. By simply setting the window size, we can use local-attention in vllm/flashattn. This can accelerate the prefill phase (on long context case). In decode phase, the local-attention layer caches all the kvcache and then only compute the window size. But that does not reduce the kvcache consumption. So is there any plan to optimize the problem? Or development advice. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: Hybrid Attention feature request;stale ### 🚀 The feature, motivation and pitch Some models(Gemma2 ...) uses hybrid attention, global-attention + local-attention. But vllm currently ignores local-attn and uses...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: on feature request;stale ### 🚀 The feature, motivation and pitch Some models(Gemma2 ...) uses hybrid attention, global-attention + local-attention. But vllm currently ignores local-attn and uses global-attn. By simply s...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ature request;stale ### 🚀 The feature, motivation and pitch Some models(Gemma2 ...) uses hybrid attention, global-attention + local-attention. But vllm currently ignores local-attn and uses global-attn. By simply settin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
