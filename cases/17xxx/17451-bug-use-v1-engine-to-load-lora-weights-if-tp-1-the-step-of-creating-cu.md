# vllm-project/vllm#17451: [Bug]: Use v1 engine to load lora weights. If tp=1, the step of creating cudagraph will only use cpu. This causes this process to take a very long time. If tp>1, the gpu will be used normally for processing.

| 字段 | 值 |
| --- | --- |
| Issue | [#17451](https://github.com/vllm-project/vllm/issues/17451) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Use v1 engine to load lora weights. If tp=1, the step of creating cudagraph will only use cpu. This causes this process to take a very long time. If tp>1, the gpu will be used normally for processing.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug See this issue for details: [https://github.com/vllm-project/vllm/issues/16961](url) Why does v1 engine only use cpu to create cudagraph when only one gpu is used? Is there something wrong with my graphics card or driver? This phenomenon always exists from 0.8.3 to 0.8.5. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency Your current env...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Use v1 engine to load lora weights. If tp=1, the step of creating cudagraph will only use cpu. This causes this process to take a very long time. If tp>1, the gpu will be used normally for processing. bug ### You...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rallel;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ed questions. development ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: development ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
