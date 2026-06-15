# vllm-project/vllm#14403: [Bug]:  Error when Run Image Docker Vllm v0.7.3 -  Unexpected error from cudaGetDeviceCount().  ....

| 字段 | 值 |
| --- | --- |
| Issue | [#14403](https://github.com/vllm-project/vllm/issues/14403) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  Error when Run Image Docker Vllm v0.7.3 -  Unexpected error from cudaGetDeviceCount().  ....

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ![Image](https://github.com/user-attachments/assets/d09ea20e-d3ae-49a9-8f47-3a3fe7b91d6c) ### Before submitting a new issue... - [ ] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Error when Run Image Docker Vllm v0.7.3 - Unexpected error from cudaGetDeviceCount(). .... bug;stale ### Your current environment ### 🐛 Describe the bug ![Image](https://github.com/user-attachments/assets/d09ea20...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Error when Run Image Docker Vllm v0.7.3 - Unexpected error from cudaGetDeviceCount(). .... bug;stale ### Your current environment ### 🐛 Describe the bug ![Image](https://github.com/user-attachments/assets/d09ea20...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: hich can answer lots of frequently asked questions. development ci_build;model_support cuda build_error env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ker Vllm v0.7.3 - Unexpected error from cudaGetDeviceCount(). .... bug;stale ### Your current environment ### 🐛 Describe the bug ![Image](https://github.com/user-attachments/assets/d09ea20e-d3ae-49a9-8f47-3a3fe7b91d6c)...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;model_support cuda build_error env_dependency Your current envir...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
