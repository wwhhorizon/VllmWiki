# vllm-project/vllm#8114: [Bug]: JAMBA 1.5 - Beam Search Returns a few characters then stops early

| 字段 | 值 |
| --- | --- |
| Issue | [#8114](https://github.com/vllm-project/vllm/issues/8114) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: JAMBA 1.5 - Beam Search Returns a few characters then stops early

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I attempt to run beam searches against Jamba 1.5 Mini, I only get a few tokens back before the response stops prematurely. Example - What I get: ``` '''python ``` What I expect: ``` '''python ''' ``` There are no errors even with the log level turned up to debug and tracing enabled. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ` There are no errors even with the log level turned up to debug and tracing enabled. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: JAMBA 1.5 - Beam Search Returns a few characters then stops early bug;stale ### Your current environment ### 🐛 Describe the bug When I attempt to run beam searches against Jamba 1.5 Mini, I only get a few tokens...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ]: JAMBA 1.5 - Beam Search Returns a few characters then stops early bug;stale ### Your current environment ### 🐛 Describe the bug When I attempt to run beam searches against Jamba 1.5 Mini, I only get a few tokens back...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
