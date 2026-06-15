# vllm-project/vllm#6248: [Feature]: Set tensor_parallel_size to -1, to use all available cuda devices

| 字段 | 值 |
| --- | --- |
| Issue | [#6248](https://github.com/vllm-project/vllm/issues/6248) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Set tensor_parallel_size to -1, to use all available cuda devices

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Deploying a model with vLLM to Vertex AI Online Prediction directly requires to first build the container, register the container in the Model Registry and then deploy to Online Prediction. If we want to have the flexibility to use different setups in terms of number of GPU, we need to build one container for every possible setup, or if we work with environment variables, we need to register one model for every possible setup. In the deployment step on GCP, there is no option to set environment variables. This is why I'd like to propose a feature that takes just all the GPUs available. I went through the code and saw an easy option to use tensor_parallel_size -1 and add two lines to vllm/config.py: https://github.com/vllm-project/vllm/commit/8f484fc33d8af7d67d51ca9cbc192ac57b1509ad If that would be an option, I could further work on the PR above and add documentation. ### Alternatives What we are doing already today like described above. ### Additional context I'm not sure if this would also touch more complex ray setups or other accelerators like TPUs.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: odel with vLLM to Vertex AI Online Prediction directly requires to first build the container, register the container in the Model Registry and then deploy to Online Prediction. If we want to have the flexibility to use...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ature request;stale ### 🚀 The feature, motivation and pitch Deploying a model with vLLM to Vertex AI Online Prediction directly requires to first build the container, register the container in the Model Registry and the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: et tensor_parallel_size to -1, to use all available cuda devices feature request;stale ### 🚀 The feature, motivation and pitch Deploying a model with vLLM to Vertex AI Online Prediction directly requires to first build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Feature]: Set tensor_parallel_size to -1, to use all available cuda devices feature request;stale ### 🚀 The feature, motivation and pitch Deploying a model with vLLM to Vertex AI Online Prediction directly requires to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
