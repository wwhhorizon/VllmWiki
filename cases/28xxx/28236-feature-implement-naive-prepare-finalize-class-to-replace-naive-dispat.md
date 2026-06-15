# vllm-project/vllm#28236: [Feature]: Implement naive prepare/finalize class to replace naive dispatching in fused_moe/layer.py

| 字段 | 值 |
| --- | --- |
| Issue | [#28236](https://github.com/vllm-project/vllm/issues/28236) |
| 状态 | closed |
| 标签 | help wanted;good first issue;feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Implement naive prepare/finalize class to replace naive dispatching in fused_moe/layer.py

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The `FusedMoE` layer has a special case dispatch/combine for EP+DP when there is no specific all2all backend specified. This makes the code in `layer.py` a bit confusing and hard to follow. One way to simplify this is to implement a proper `FusedMoEPrepareAndFinalize` subclass for naive dispatch/combine. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Feature]: Implement naive prepare/finalize class to replace naive dispatching in fused_moe/layer.py help wanted;good first issue;feature request;stale ### 🚀 The feature, motivation and pitch The `FusedMoE` layer has a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e dispatching in fused_moe/layer.py help wanted;good first issue;feature request;stale ### 🚀 The feature, motivation and pitch The `FusedMoE` layer has a special case dispatch/combine for EP+DP when there is no specific...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e ### 🚀 The feature, motivation and pitch The `FusedMoE` layer has a special case dispatch/combine for EP+DP when there is no specific all2all backend specified. This makes the code in `layer.py` a bit confusing and har...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ement naive prepare/finalize class to replace naive dispatching in fused_moe/layer.py help wanted;good first issue;feature request;stale ### 🚀 The feature, motivation and pitch The `FusedMoE` layer has a special case di...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
