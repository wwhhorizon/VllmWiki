# vllm-project/vllm#9991: [Bug]: Llama3.2 tool calling OpenAI API not working

| 字段 | 值 |
| --- | --- |
| Issue | [#9991](https://github.com/vllm-project/vllm/issues/9991) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: Llama3.2 tool calling OpenAI API not working

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When trying to run Llama3.2 tool calling via `python -m vllm.entrypoints.openai.api_server --model meta-llama/Llama-3.2-1B-Instruct --enable-auto-tool-choice --tool-call-parser llama3_json` I do not get the OpenAI API function calling functionality but rather just get the tool call string: ``` ❯ current time? {"type": "function", "function": "get_time", "parameters": {"timezone": "America/New_York"}} ``` Using the official OpenAI API with 4o and Ollama works with my code ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: time", "parameters": {"timezone": "America/New_York"}} ``` Using the official OpenAI API with 4o and Ollama works with my code ### Before submitting a new issue... - [X] Make sure you already searched for relevant issue...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ode ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Llama3.2 tool calling OpenAI API not working bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When trying to run Llama3.2 tool calling via `python -m vllm.entrypoints.ope
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ted_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
