# vllm-project/vllm#8666: [Bug]: Dockerfile has a hardcoded dependency for flashinfer with cuda 12.1

| 字段 | 值 |
| --- | --- |
| Issue | [#8666](https://github.com/vllm-project/vllm/issues/8666) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Dockerfile has a hardcoded dependency for flashinfer with cuda 12.1

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I haven't downloaded vllm on my system as I just wanted to build the docker and later use it on our GPU. Hence, in the above logs there is no python or conda environment set. Anyways, the issue: When trying to build docker from source, there seems to be a hardcoded dependency for cuda 12.1 on flash-infer. Not sure if it is intended as all the other places, build arguments have been used. https://github.com/vllm-project/vllm/blob/260d40b5ea48df9421325388abcc8d907a560fc5/Dockerfile#L173 Feel free to resolve the bug if it is intended. Thanks ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Dockerfile has a hardcoded dependency for flashinfer with cuda 12.1 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I haven't downloaded vllm on my system as I jus
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Dockerfile has a hardcoded dependency for flashinfer with cuda 12.1 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I haven't downloaded vllm on my system as I ju...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: Dockerfile has a hardcoded dependency for flashinfer with cuda 12.1 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I haven't downloaded vllm on my system as I ju...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: flashinfer with cuda 12.1 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I haven't downloaded vllm on my system as I just wanted to build the docker and later use it on...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Dockerfile has a hardcoded dependency for flashinfer with cuda 12.1 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I haven't downloaded vllm on my system as I just want...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
