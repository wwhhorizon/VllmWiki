# vllm-project/vllm#21727: [Bug]: DeepSeek-V3-0324 tool-call: fail to get tool_calls from response occationally

| 字段 | 值 |
| --- | --- |
| Issue | [#21727](https://github.com/vllm-project/vllm/issues/21727) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek-V3-0324 tool-call: fail to get tool_calls from response occationally

### Issue 正文摘录

### Your current environment image: vllm/vllm-openai:v0.9.0 ### 🐛 Describe the bug For a DeepSeek-V3-0324 OpenAI service with tool-calls enabled as described in https://github.com/vllm-project/vllm/pull/17784, The tool_call functionality is **not stable enough** under default sampling parameters. Sometimes the tool_calls[] field in response json is empty, with some tool-call content present in the "content" field. serving command: ``` python3 -m vllm.entrypoints.openai.api_server --served-model-name deepseek_v3 \ --max-model-len 65536 \ --enable-chunked-prefill --enable-prefix-caching --trust-remote-code \ --max-num-seqs 1024 \ --model /path/to/DeepSeek-V3-0324 --tensor-parallel-size 8 \ --enable-auto-tool-choice --tool-call-parser deepseek_v3 \ --chat-template examples/tool_chat_template_deepseekv3.jinja ``` scripts to chat with model: ``` from openai import OpenAI def send_messages(messages, model_name): response = client.chat.completions.create( model=model_name, messages=messages, tools=tools ) return response.choices[0].message tools = [ { "type": "function", "function": { "name": "get_weather", "description": "Get weather of an location, the user shoud supply a location firs...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: mplate_deepseekv3.jinja ``` scripts to chat with model: ``` from openai import OpenAI def send_messages(messages, model_name): response = client.chat.completions.create( model=model_name, messages=messages, tools=tools...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: V3-0324 tool-call: fail to get tool_calls from response occationally bug;stale ### Your current environment image: vllm/vllm-openai:v0.9.0 ### 🐛 Describe the bug For a DeepSeek-V3-0324 OpenAI service with tool-calls ena...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ving command: ``` python3 -m vllm.entrypoints.openai.api_server --served-model-name deepseek_v3 \ --max-model-len 65536 \ --enable-chunked-prefill --enable-prefix-caching --trust-remote-code \ --max-num-seqs 1024 \ --mo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
