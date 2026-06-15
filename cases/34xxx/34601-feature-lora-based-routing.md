# vllm-project/vllm#34601: [Feature]: LoRA-based Routing

| 字段 | 值 |
| --- | --- |
| Issue | [#34601](https://github.com/vllm-project/vllm/issues/34601) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: LoRA-based Routing

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Good Afternoon Everyone! I was wondering if there is a way to support LoRA hot-swapping on DDP deployments, i.e. if I have 4 separate instances of the same model backbone, and I want to have maybe the first instance running LoRA adaptor A and the third running adaptor B. Then based on some argument in the request specifying which adaptor the request should be handled by, for VLLM to route the request to the respective adaptors. And suppose I now have a request coming in with adaptor C as the argument, the engine can adaptively select maybe instance 1 to swap out the adaptor to C to serve the oncoming request. I guess this would be similar to L7 routing except we route on the adaptor request and we do some additional steps (loading in adaptors that are not already running on a instance) before generating the inference. Not sure if this is a feature that could be / should be supported by VLLM, but just wanted to check with everyone here and see if there's any advice! ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the ch...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: LoRA-based Routing feature request;stale ### 🚀 The feature, motivation and pitch Good Afternoon Everyone! I was wondering if there is a way to support LoRA hot-swapping on DDP deployments, i.e. if I have 4 se...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: LoRA-based Routing feature request;stale ### 🚀 The feature, motivation and pitch Good Afternoon Everyone! I was wondering if there is a way to support LoRA hot-swapping on DDP deployments, i.e. if I have 4 se...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e third running adaptor B. Then based on some argument in the request specifying which adaptor the request should be handled by, for VLLM to route the request to the respective adaptors. And suppose I now have a request...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ping on DDP deployments, i.e. if I have 4 separate instances of the same model backbone, and I want to have maybe the first instance running LoRA adaptor A and the third running adaptor B. Then based on some argument in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
