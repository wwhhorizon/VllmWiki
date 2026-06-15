# vllm-project/vllm#26631: [Bug]: vllm使用多gpu推理Qwen2.5-VL-32B-Instruct，无法进行进程间通信

| 字段 | 值 |
| --- | --- |
| Issue | [#26631](https://github.com/vllm-project/vllm/issues/26631) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: vllm使用多gpu推理Qwen2.5-VL-32B-Instruct，无法进行进程间通信

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 使用 pipeline_parallel_size = 8进行推理，报错。 [rank3]:[W1011 19:02:33.795524232 ProcessGroupNCCL.cpp:1783] [PG ID 0 PG GUID 0 Rank 3] Failed to check the "should dump" flag on TCPStore, (maybe TCPStore server has shut down too early), with error: Failed to recv, got 0 bytes. Connection was likely closed. Did the remote server shutdown or crash? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash env_dependen...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: sh? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: vllm使用多gpu推理Qwen2.5-VL-32B-Instruct，无法进行进程间通信 bug ### Your current environment ### 🐛 Describe the bug 使用 pipeline_parallel_size = 8进行推理，报错。 [rank3]:[W1011 19:02:33.795524232 ProcessGroupNCCL.cpp:1783] [PG ID 0 PG...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nd_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
