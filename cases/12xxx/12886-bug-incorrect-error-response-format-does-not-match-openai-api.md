# vllm-project/vllm#12886: [Bug]: Incorrect error response: format does not match OpenAI API

| 字段 | 值 |
| --- | --- |
| Issue | [#12886](https://github.com/vllm-project/vllm/issues/12886) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | wrong_output |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Incorrect error response: format does not match OpenAI API

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When sending a request to vllm that should return an error, the error response format does not match the standard format of the OpenAI API. This discrepancy causes issues when integrating vllm with systems that expect the standard OpenAI API error format. E.g. chat-ui is unable to get the error message from the response via [OpenAI official npm package](https://www.npmjs.com/package/openai). Here is an example of the actual error response from vllm: ``` { "object": "error", "message": "This model's maximum context length is 2048 tokens. However, you requested 2723 tokens (1699 in the messages, 1024 in the completion). Please reduce the length of the messages or completion.", "type": "BadRequestError", "param": null, "code": 400 } ``` However, the expected error response format should match the OpenAI API standard: ``` { "object": "error", "error": { "message": "This model's maximum context length is 2048 tokens. However, you requested 2723 tokens (1699 in the messages, 1024 in the completion). Please reduce the length of the messages or completion.", } "type": "BadRequestError", "param": null, "code": 400 } ``` Note an error prop...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: -ui is unable to get the error message from the response via [OpenAI official npm package](https://www.npmjs.com/package/openai). Here is an example of the actual error response from vllm: ``` { "object": "error", "mess...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Incorrect error response: format does not match OpenAI API bug;stale ### Your current environment ### 🐛 Describe the bug When sending a request to vllm that should return an error, the error response format does...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Incorrect error response: format does not match OpenAI API bug;stale ### Your current environment ### 🐛 Describe the bug When sending a request to vllm that should return an error, the error response format does...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;mismatch;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
