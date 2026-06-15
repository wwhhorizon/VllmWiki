# vllm-project/vllm#10781: [Bug]: Streaming w/ tool choice auto often truncates the final delta in the streamed arguments

| 字段 | 值 |
| --- | --- |
| Issue | [#10781](https://github.com/vllm-project/vllm/issues/10781) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Streaming w/ tool choice auto often truncates the final delta in the streamed arguments

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The current streaming implementation when using "auto" tool choice has multiple issues. I have validated that these issues exist with both the Hermes and Mistral tool parsers and have prepared a PR that I'll be submitting shortly to fix these issues. 1. With all parsers, when a Delta is created in serving_chat.py, it is not sent until the end of the chat_completion_stream_generator function is reached. However, when the end of a tool is detected, a new delta that doesn't include the already-constructed delta is created and the original delta is not submitted. For example: if arguments is ```{"arguments": "{\"prompt\":\"Wicked Movie 2024\"}"``` it is possible that depending on token return from the model, perhaps "2024" or even "vie 2024" would be dropped. 2. Hermes parser has a similar issue where it doesn't even return the delta when it detects that the tool end token is detected. This is because when it detects that the tool end token is provided, it may still have part of an unset delta that it has not yet returned. 3. Mistral parser may match the wrong part of the initial token if the argum...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ed. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: delta in the streamed arguments bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The current streaming implementation when using "auto" tool choice has multiple issues. I have...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ted_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
