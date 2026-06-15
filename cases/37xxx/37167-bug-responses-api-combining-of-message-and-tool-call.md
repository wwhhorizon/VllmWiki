# vllm-project/vllm#37167: [Bug]: responses API, combining of message and tool call

| 字段 | 值 |
| --- | --- |
| Issue | [#37167](https://github.com/vllm-project/vllm/issues/37167) |
| 状态 | open |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: responses API, combining of message and tool call

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In the responses API, non-harmony code path, we currently generate from the `input` list (`ResponseInputOutputItem` items) corresponding chat messages. This is mostly straight forward with the exception of tool calls, as in the responses API they are represented by individual response items, while in the chat completions API one or more tool calls are part of content and/or reasoning messages. Most/all(?) non-harmony chat templates (e.g., Qwen3, Qwen3.5 model families) depend on rendered messages that combine reasoning or content with tool calls, similar to the chat completions API. Keeping reasoning/content messages separate from tool calls (and thus individually rendered) leads to subtle issues: Most often, e.g., after 5 to 15 successful tool calls, a final message is generated that ends the agent turn prematurely (see https://github.com/ggml-org/llama.cpp/issues/19513 ). Note that by convention of most harnesses (codex, qwen-coder, ...) an agent turn is considered finished, if a model response does not contain at least one further tool call. Now we already do some combining in `vllm/entrypoints/openai/responses/utils.py`, `_ma...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: frequently asked questions. /edit: improved bug description development ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support cuda;triton build_error env_dependency Your current environme...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nd/or reasoning messages. Most/all(?) non-harmony chat templates (e.g., Qwen3, Qwen3.5 model families) depend on rendered messages that combine reasoning or content with tool calls, similar to the chat completions API....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ng ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ed_parallel;frontend_api;gemm_linear;hardware_porting;model_support cuda;triton build_error env_dependency Your current environment
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: d bug description development ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support cuda;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
