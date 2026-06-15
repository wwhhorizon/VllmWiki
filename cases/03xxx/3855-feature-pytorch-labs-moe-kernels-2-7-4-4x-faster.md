# vllm-project/vllm#3855: [Feature]: PyTorch Labs MoE Kernels (2.7-4.4x faster)

| 字段 | 值 |
| --- | --- |
| Issue | [#3855](https://github.com/vllm-project/vllm/issues/3855) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: PyTorch Labs MoE Kernels (2.7-4.4x faster)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch vLLM should adopt the PyTorch Labs Triton kernels that were developed recently since they can yield *2.7x faster for bs=2 and 4.4x for bs=512*. @WoosukKwon Note that the new kernels were developed on top of the existing vLLM kernels, so they should be highly compatible. Blog: https://pytorch.org/blog/accelerating-moe-model/?utm_content=288416924 Code: https://github.com/pytorch-labs/applied-ai/tree/main/kernels/triton/inference/col_major_moe_gemm ![image](https://github.com/vllm-project/vllm/assets/27340033/eb99d7be-2470-47fe-88df-9ed608f84377) ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Feature]: PyTorch Labs MoE Kernels (2.7-4.4x faster) feature request;stale ### 🚀 The feature, motivation and pitch vLLM should adopt the PyTorch Labs Triton kernels that were developed recently since they can yield *2....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: PyTorch Labs MoE Kernels (2.7-4.4x faster) feature request;stale ### 🚀 The feature, motivation and pitch vLLM should adopt the PyTorch Labs Triton kernels that were developed recently since they can yield *2....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 🚀 The feature, motivation and pitch vLLM should adopt the PyTorch Labs Triton kernels that were developed recently since they can yield *2.7x faster for bs=2 and 4.4x for bs=512*. @WoosukKwon Note that the new kernels w...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: d be highly compatible. Blog: https://pytorch.org/blog/accelerating-moe-model/?utm_content=288416924 Code: https://github.com/pytorch-labs/applied-ai/tree/main/kernels/triton/inference/col_major_moe_gemm ![image](https:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
