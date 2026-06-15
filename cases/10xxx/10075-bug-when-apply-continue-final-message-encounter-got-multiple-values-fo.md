# vllm-project/vllm#10075: [Bug]: When apply continue_final_message, encounter: got multiple values for keyword argument

| 字段 | 值 |
| --- | --- |
| Issue | [#10075](https://github.com/vllm-project/vllm/issues/10075) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: When apply continue_final_message, encounter: got multiple values for keyword argument

### Issue 正文摘录

### Your current environment vLLM Version: 0.6.3.post2.dev256+g4be3a451 ### Model Input Dumps _No response_ ### 🐛 Describe the bug Reproduce using curl ```bash curl -X POST "http://39.105.21.95:12481/v1/chat/completions" \ -H "Content-Type: application/json" \ -d '{ "model": "meta-llama/Meta-Llama-3-8B-Instruct", "messages": [ { "role": "user", "content": "tell me a common saying" }, { "role": "assistant", "content": "Here is a common saying about apple. An apple a day, keeps" } ], "add_generation_prompt": false, "chat_template_kwargs":{"continue_final_message": true} }' Internal Server Error% ``` Error message on server ```bash File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/api_server.py", line 338, in create_chat_completion generator = await handler.create_chat_completion(request, raw_request) File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/serving_chat.py", line 140, in create_chat_completion ) = await self._preprocess_chat( File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/serving_engine.py", line 460, in _preprocess_chat request_prompt = apply_hf_chat_template( TypeError: vllm.entrypoints.chat_utils.apply_hf_cha...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: tiple values for keyword argument bug ### Your current environment vLLM Version: 0.6.3.post2.dev256+g4be3a451 ### Model Input Dumps _No response_ ### 🐛 Describe the bug Reproduce using curl ```bash curl -X POST "http://...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: r current environment vLLM Version: 0.6.3.post2.dev256+g4be3a451 ### Model Input Dumps _No response_ ### 🐛 Describe the bug Reproduce using curl ```bash curl -X POST "http://39.105.21.95:12481/v1/chat/completions" \ -H...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ate_chat_completion generator = await handler.create_chat_completion(request, raw_request) File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/serving_chat.py", line 140, in create_chat_completion ) =...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nd_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
