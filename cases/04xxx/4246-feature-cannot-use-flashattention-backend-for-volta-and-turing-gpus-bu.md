# vllm-project/vllm#4246: [Feature]: Cannot use FlashAttention backend for Volta and Turing GPUs. (but FlashAttention v1.0.9 supports Turing GPU.)

| 字段 | 值 |
| --- | --- |
| Issue | [#4246](https://github.com/vllm-project/vllm/issues/4246) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Cannot use FlashAttention backend for Volta and Turing GPUs. (but FlashAttention v1.0.9 supports Turing GPU.)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Turing GPU can use FlashAttention v1.0.9 which can reduce use of vram significantly. FlashAttention has no plan to support Turing GPU in FlashAttention v2 actually. so please support FlashAttention v1.0.9. thanks a lot! many friends having 8*2080ti need this help. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Feature]: Cannot use FlashAttention backend for Volta and Turing GPUs. (but FlashAttention v1.0.9 supports Turing GPU.) feature request ### 🚀 The feature, motivation and pitch Turing GPU can use FlashAttention v1.0.9 w...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: nd Turing GPUs. (but FlashAttention v1.0.9 supports Turing GPU.) feature request ### 🚀 The feature, motivation and pitch Turing GPU can use FlashAttention v1.0.9 which can reduce use of vram significantly. FlashAttentio...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
