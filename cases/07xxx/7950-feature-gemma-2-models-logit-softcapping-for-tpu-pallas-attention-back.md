# vllm-project/vllm#7950: [Feature]: Gemma 2 models logit softcapping for TPU pallas attention backend

| 字段 | 值 |
| --- | --- |
| Issue | [#7950](https://github.com/vllm-project/vllm/issues/7950) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Gemma 2 models logit softcapping for TPU pallas attention backend

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Trying to run a Gemma 2 model on VLLM TPU gets the error not implemented for pallas backend But searching on pallas kernel they do have support for logit softcapping for paged attention. I wonder if it could be implement in VLLM also. @WoosukKwon @lsy323 ### Alternatives _No response_ ### Additional context [PR for attention soft capping in pallas kernels Pytorch xla](https://github.com/pytorch/xla/pull/7704) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Gemma 2 models logit softcapping for TPU pallas attention backend feature request;stale ### 🚀 The feature, motivation and pitch Trying to run a Gemma 2 model on VLLM TPU gets the error not implemented for pal...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: emma 2 models logit softcapping for TPU pallas attention backend feature request;stale ### 🚀 The feature, motivation and pitch Trying to run a Gemma 2 model on VLLM TPU gets the error not implemented for pallas backend...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: Gemma 2 models logit softcapping for TPU pallas attention backend feature request;stale ### 🚀 The feature, motivation and pitch Trying to run a Gemma 2 model on VLLM TPU gets the error not implemented for pal...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: l on VLLM TPU gets the error not implemented for pallas backend But searching on pallas kernel they do have support for logit softcapping for paged attention. I wonder if it could be implement in VLLM also. @WoosukKwon...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Feature]: Gemma 2 models logit softcapping for TPU pallas attention backend feature request;stale ### 🚀 The feature, motivation and pitch Trying to run a Gemma 2 model on VLLM TPU gets the error not implemented for pal...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
