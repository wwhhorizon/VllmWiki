# vllm-project/vllm#14470: [Bug]: pythonic tool parser only accepts alphabetical tool names

| 字段 | 值 |
| --- | --- |
| Issue | [#14470](https://github.com/vllm-project/vllm/issues/14470) |
| 状态 | closed |
| 标签 | bug;stale;tool-calling |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: pythonic tool parser only accepts alphabetical tool names

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The `PythonicToolParser` `TOOL_CALL_REGEX` only supports alphanumeric tool names and parameter names. There are a couple of issues with this: 1. `snake_case` is not supported. This is even used in OpenAI's API example `get_weather`. 2. `kebab-case` is not supported. This is not valid Python at all, but the API is all specified in terms of JSON, and it's a perfectly valid string. n8n's builtin Wikipedia tool is named `wikipedia-api` 3. Numbers not supported! Can't believe I didn't see this while staring at that regex These issues are different in difficulty: 1. I think `snake_case `is trivial to fix by changing `TOOL_CALL_REGEX` because `ast.parse` will be happy 2. I can see a few ways to handle `kebab-case`, but none of them are ideal. The easiest thing seems to be to accept invalid Python with the regex, use the regex to remap to valid python variable names, then map back after parsing. All of the other things I can think of (like letting instances of `TooLParser` remap names) leak info to the model. There's still a risk that pythonic models are reluctant to make invalid name function calls (but I have been hitting the exact opp...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: is not supported. This is not valid Python at all, but the API is all specified in terms of JSON, and it's a perfectly valid string. n8n's builtin Wikipedia tool is named `wikipedia-api` 3. Numbers not supported! Can't...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: CL. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: of (like letting instances of `TooLParser` remap names) leak info to the model. There's still a risk that pythonic models are reluctant to make invalid name function calls (but I have been hitting the exact opposite!) 3...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: pythonic tool parser only accepts alphabetical tool names bug;stale;tool-calling ### Your current environment ### 🐛 Describe the bug The `PythonicToolParser` `TOOL_CALL_REGEX` only supports alphanumeric tool name...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
