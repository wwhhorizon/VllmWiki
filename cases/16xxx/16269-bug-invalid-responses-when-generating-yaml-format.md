# vllm-project/vllm#16269: [Bug]: invalid responses when generating yaml format

| 字段 | 值 |
| --- | --- |
| Issue | [#16269](https://github.com/vllm-project/vllm/issues/16269) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: invalid responses when generating yaml format

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am trying to use LLM for generating yaml openapi specification. With vLLM i often get broken responses that start out fine but break at the end (model spams empty lines or random characters). I tried different versions of vLLM (including latest), different parameters, different models (mostly Qwen2.5 Coder Instruct), V0 and V1 engine and problem stays the same. I assumed it was a lack of GPU memory, but the problem persists even on small models like Qwen2.5 Coder 1.5b or 4bit quantized Qwen2.5 Coder 7b. Same models on same hardware deployed with llama.cpp can generate yaml specification fine with no such promlems. What could have caused such behavior? Is this a bug or am I doing something wrong? Prompt example (Not only this prompt causes broken result, almost any generation with yaml does it. Sometimes even responses without any yaml break in a similar way): Write a YAML API specification (OAS 3.0, yaml) implementing CRUD operations on the data model described by the following ERD: ``` @startuml hide circle entity party { *partyId *Idsystem1 *Idsystem2 *partyType } entity partyRole { *partyRoleId *msisdn additionalAtribute1 .....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Describe the bug I am trying to use LLM for generating yaml openapi specification. With vLLM i often get broken responses that start out fine but break at the end (model spams empty lines or random characters). I tried...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: invalid responses when generating yaml format bug;stale ### Your current environment ### 🐛 Describe the bug I am trying to use LLM for generating yaml openapi specification. With vLLM i often get broken responses...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: I assumed it was a lack of GPU memory, but the problem persists even on small models like Qwen2.5 Coder 1.5b or 4bit quantized Qwen2.5 Coder 7b. Same models on same hardware deployed with llama.cpp can generate yaml spe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: invalid responses when generating yaml format bug;stale ### Your current environment ### 🐛 Describe the bug I am trying to use LLM for generating yaml openapi specification. With vLLM i often get broken responses...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: del_support;quantization;speculative_decoding cuda;operator;quantization;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
