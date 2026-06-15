# vllm-project/vllm#9224: [Feature]: Build custom_ops for both CPU and CUDA

| 字段 | 值 |
| --- | --- |
| Issue | [#9224](https://github.com/vllm-project/vllm/issues/9224) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api |
| 子分类 |  |
| Operator 关键词 | cuda;operator |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Build custom_ops for both CPU and CUDA

### Issue 正文摘录

### 🚀 The feature, motivation and pitch As the custom ops are registered in torch, we can treat them as torch ops. The torch ops support tensor-driven dispatch, they share the same API by cpu and cuda. So I was wondering if we can build both CPU and CUDA in custom ops and dispatch it by tensor device? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Feature]: Build custom_ops for both CPU and CUDA feature request;stale ### 🚀 The feature, motivation and pitch As the custom ops are registered in torch, we can treat them as torch ops. The torch ops support tensor-dri...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Build custom_ops for both CPU and CUDA feature request;stale ### 🚀 The feature, motivation and pitch As the custom ops are registered in torch, we can treat them as torch ops. The torch ops support tensor-dri...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Build custom_ops for both CPU and CUDA feature request;stale ### 🚀 The feature, motivation and pitch As the custom ops are registered in torch, we can treat them as torch ops. The torch ops support tensor-dri...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ch, we can treat them as torch ops. The torch ops support tensor-driven dispatch, they share the same API by cpu and cuda. So I was wondering if we can build both CPU and CUDA in custom ops and dispatch it by tensor dev...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;frontend_api cuda;operator build_error env_dependency 🚀 The feat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
