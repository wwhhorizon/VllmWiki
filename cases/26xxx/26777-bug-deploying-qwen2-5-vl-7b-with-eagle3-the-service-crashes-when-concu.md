# vllm-project/vllm#26777: [Bug]: Deploying Qwen2.5-VL-7B with Eagle3, the service crashes when concurrency increases.

| 字段 | 值 |
| --- | --- |
| Issue | [#26777](https://github.com/vllm-project/vllm/issues/26777) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Deploying Qwen2.5-VL-7B with Eagle3, the service crashes when concurrency increases.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When deploying the Qwen2.5-VL model with Eagle3, initial stress testing shows "OK" in the logs. However, as QPS increases, the service eventually fails with the following error logs. Interestingly, when setting CUDA_LAUNCH_BLOCKING=1 to debug the issue, the stress test completes successfully without errors. [eagle.log](https://github.com/user-attachments/files/22899153/eagle.log) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash env_dependen...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ntually fails with the following error logs. Interestingly, when setting CUDA_LAUNCH_BLOCKING=1 to debug the issue, the stress test completes successfully without errors. [eagle.log](https://github.com/user-attachments/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Deploying Qwen2.5-VL-7B with Eagle3, the service crashes when concurrency increases. bug;stale ### Your current environment ### 🐛 Describe the bug When deploying the Qwen2.5-VL model with Eagle3, initial stress t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 5-VL-7B with Eagle3, the service crashes when concurrency increases. bug;stale ### Your current environment ### 🐛 Describe the bug When deploying the Qwen2.5-VL model with Eagle3, initial stress testing shows "OK" in th...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nd_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
