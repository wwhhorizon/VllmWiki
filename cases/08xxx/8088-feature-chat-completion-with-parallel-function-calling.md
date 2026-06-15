# vllm-project/vllm#8088: [Feature]: Chat Completion with Parallel Function Calling

| 字段 | 值 |
| --- | --- |
| Issue | [#8088](https://github.com/vllm-project/vllm/issues/8088) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Chat Completion with Parallel Function Calling

### Issue 正文摘录

### Your current environment vLLM 0.5.5 openai 1.43.0 ### 🐛 Describe the bug First, launch an OpenAI compatible server: `vllm serve meta-llama/Meta-Llama-3.1-8B-Instruct --dtype auto --max_model_len 20480`. Then try to request this server with the following payload for function calling ```json { "messages": [ { "content": "\\nYou are a grader assessing whether an LLM generation is grounded in / supported by a set of retrieved facts.\\nGive a binary score \'yes\' or \'no\', where \'yes\' means that the answer is grounded in / supported by the set of facts.\\n\\nIF the generation includes code examples, make sure those examples are FULLY present in the set of facts, otherwise always return score \'no\'.\\n", "role": "system" }, { "content": "Set of facts: Provided Documents.", "role": "user" } ], "model": "meta-llama/Meta-Llama-3.1-8B-Instruct", "stream": false, "n": 1, "temperature": 0, "max_tokens": 2048, "tools": [ { "type": "function", "function": { "name": "GradeHallucinations", "description": "Binary score for hallucination present in generation answer.", "parameters": { "type": "object", "properties": { "binary_score": { "description": "Answer is grounded in the facts, \'yes\...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: "function", "function": { "name": "GradeHallucinations", "description": "Binary score for hallucination present in generation answer.", "parameters": { "type": "object", "properties": {
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: LM? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ibe the bug First, launch an OpenAI compatible server: `vllm serve meta-llama/Meta-Llama-3.1-8B-Instruct --dtype auto --max_model_len 20480`. Then try to request this server with the following payload for function calli...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Chat Completion with Parallel Function Calling feature request ### Your current environment vLLM 0.5.5 openai 1.43.0 ### 🐛 Describe the bug First, launch an OpenAI compatible server: `vllm serve meta-llama/Me...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
