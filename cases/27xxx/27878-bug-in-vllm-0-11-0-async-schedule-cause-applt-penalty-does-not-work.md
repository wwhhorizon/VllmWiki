# vllm-project/vllm#27878: [Bug]: In vllm 0.11.0 async schedule cause applt penalty does not work

| 字段 | 值 |
| --- | --- |
| Issue | [#27878](https://github.com/vllm-project/vllm/issues/27878) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: In vllm 0.11.0 async schedule cause applt penalty does not work

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Enabling asynchronous scheduling will disable the apply penalty.Because the `output_token_ids` value in `sampling_metadata` will always be empty. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding cuda;operator;trit...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ted_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: port;sampling_logits;scheduler_memory;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: able the apply penalty.Because the `output_token_ids` value in `sampling_metadata` will always be empty. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatb...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
