# vllm-project/vllm#10111: [Bug]: When apply continue_final_message for OpenAI server, the `"echo":false` is ignored.

| 字段 | 值 |
| --- | --- |
| Issue | [#10111](https://github.com/vllm-project/vllm/issues/10111) |
| 状态 | closed |
| 标签 | bug;help wanted;good first issue |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When apply continue_final_message for OpenAI server, the `"echo":false` is ignored.

### Issue 正文摘录

### Your current environment vLLM Version: 0.6.3.post2.dev256+g4be3a451 ### Model Input Dumps _No response_ ### 🐛 Describe the bug According to the documentation, the `echo` parameter is false by default, but with `continue_final_message` set, the new message will always be prepended with the last message. Reproduction Code: ```bash curl -X POST "http://39.105.21.95:12481/v1/chat/completions" \ -H "Content-Type: application/json" \ -d '{ "model": "meta-llama/Meta-Llama-3-8B-Instruct", "messages": [ { "role": "user", "content": "tell me a common saying" }, { "role": "assistant", "content": "Here is a common saying about apple. An apple a day, keeps" } ], "add_generation_prompt": false, "continue_final_message": true, "echo":false }' {"id":"chatcmpl-c49a327f6edd48ed9993668771d5589f","object":"chat.completion","created":1730963591,"model":"meta-llama/Meta-Llama-3-8B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"Here is a common saying about apple. An apple a day, keeps the doctor away!","tool_calls":[]},"logprobs":null,"finish_reason":"stop","stop_reason":null}],"usage":{"prompt_tokens":29,"total_tokens":34,"completion_tokens":5},"prompt_logprobs":null}% ``...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: red. bug;help wanted;good first issue ### Your current environment vLLM Version: 0.6.3.post2.dev256+g4be3a451 ### Model Input Dumps _No response_ ### 🐛 Describe the bug According to the documentation, the `echo` paramet...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: r current environment vLLM Version: 0.6.3.post2.dev256+g4be3a451 ### Model Input Dumps _No response_ ### 🐛 Describe the bug According to the documentation, the `echo` parameter is false by default, but with `continue_fi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nd_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: Bug]: When apply continue_final_message for OpenAI server, the `"echo":false` is ignored. bug;help wanted;good first issue ### Your current environment vLLM Version: 0.6.3.post2.dev256+g4be3a451 ### Model Input Dumps _N...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
