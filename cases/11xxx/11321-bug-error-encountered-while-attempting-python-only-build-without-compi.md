# vllm-project/vllm#11321: [Bug]: Error Encountered While Attempting Python-only Build (Without Compilation) for vLLM v0.6.5

| 字段 | 值 |
| --- | --- |
| Issue | [#11321](https://github.com/vllm-project/vllm/issues/11321) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: Error Encountered While Attempting Python-only Build (Without Compilation) for vLLM v0.6.5

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Here are my steps for Python only build (without compilation)： ![image](https://github.com/user-attachments/assets/89a2c0ff-1939-4433-bcd6-879bf8417609) Then the following error was reported: ![image](https://github.com/user-attachments/assets/e755cfe0-1208-44e5-8d51-579d51909950) How should I solve this, or can I only deploy vllm through Full build (with compilation)? But this will take a lot of time, my goal is to quickly deploy from the source code ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: Error Encountered While Attempting Python-only Build (Without Compilation) for vLLM v0.6.5 bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Here are my steps for Python...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ode ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rallel;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ut Compilation) for vLLM v0.6.5 bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Here are my steps for Python only build (without compilation)： ![image](https://github.com/user...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: development ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
