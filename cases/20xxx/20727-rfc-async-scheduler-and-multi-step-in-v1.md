# vllm-project/vllm#20727: [RFC]: Async scheduler and Multi-step in v1

| 字段 | 值 |
| --- | --- |
| Issue | [#20727](https://github.com/vllm-project/vllm/issues/20727) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Async scheduler and Multi-step in v1

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We propose reducing the framework’s overhead by introducing two key improvements—an asynchronous scheduler and a multi-step approach—all with minimal code modifications. 1. Asynchronous Scheduler For the async scheduler, we suggest the following design: This solution requires changes only in EngineCore without modifying other modules. By incorporating an update_schedule module, the framework can also seamlessly support speculative decoding. 2. Multi-Step Approach Although v1’s preprocessing and postprocessing are lighter compared to v0, we still observe notable inefficiencies on some platforms (e.g., ARM + XPU). In particular, there exists a significant gap between input preparation and launching the forward model, and the device-to-host (D2H) communication for each model output further increases overall latency. To address these issues, we introduce a multi-step strategy that differs from v0 in several key ways: • We propose a simple_prepare_input function to reduce unnecessary CPU operations. • We defer the D2H communication to avoid excessive stream synchronizations. • We integrate the multi-step process with the asynchronous scheduler, t...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [RFC]: Async scheduler and Multi-step in v1 feature request;stale ### 🚀 The feature, motivation and pitch We propose reducing the framework’s overhead by introducing two key improvements—an asynchronous scheduler and a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: host (D2H) communication for each model output further increases overall latency. To address these issues, we introduce a multi-step strategy that differs from v0 in several key ways: • We propose a simple_prepare_input...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: re request;stale ### 🚀 The feature, motivation and pitch We propose reducing the framework’s overhead by introducing two key improvements—an asynchronous scheduler and a multi-step approach—all with minimal code modific...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ts a significant gap between input preparation and launching the forward model, and the device-to-host (D2H) communication for each model output further increases overall latency. To address these issues, we introduce a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
