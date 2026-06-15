# vllm-project/vllm#20028: [Bug]: Streaming tool call is not working for Mistral Small 3.2

| 字段 | 值 |
| --- | --- |
| Issue | [#20028](https://github.com/vllm-project/vllm/issues/20028) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: Streaming tool call is not working for Mistral Small 3.2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm using runpods with vllm v0.9.1 (latest). The command to start the container is ``` --host 0.0.0.0 --port 8000 --model mistralai/Mistral-Small-3.2-24B-Instruct-2506 --tokenizer_mode mistral --config_format mistral --load_format mistral --tool-call-parser mistral --enable-auto-tool-choice --tensor-parallel-size 2 ``` I'm posting my request on the /v1/chat/completions API, with stream=true, temperature=0.15, max_tokens=131072. Messages include the system prompt privided by Mistral for that model, and a user request that triggers tool calling. Tools are in the OpenAI format. When I execute the request, vllm is failing with ``` INFO 06-24 08:31:04 [async_llm.py:271] Added request chatcmpl-XXX. INFO: 100.64.0.29:52808 - "POST /v1/chat/completions HTTP/1.1" 200 OK ERROR 06-24 08:31:07 [mistral_tool_parser.py:365] Error trying to handle streaming tool call. ERROR 06-24 08:31:07 [mistral_tool_parser.py:365] Traceback (most recent call last): ERROR 06-24 08:31:07 [mistral_tool_parser.py:365] File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/tool_parsers/mistral_tool_parser.py", line 220, in extract_tool_calls_stream...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: aming tool call. ``` The documentation chatbot suggested to add skip_special_tokens=False to the request, without success: ```ValueError: skip_special_tokens=False is not supported for Mistral tokenizers. INFO: 100.64.0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Streaming tool call is not working for Mistral Small 3.2 bug ### Your current environment ### 🐛 Describe the bug I'm using runpods with vllm v0.9.1 (latest). The command to start the container is ``` --host 0.0.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: The command to start the container is ``` --host 0.0.0.0 --port 8000 --model mistralai/Mistral-Small-3.2-24B-Instruct-2506 --tokenizer_mode mistral --config_format mistral --load_format mistral --tool-call-parser mistra...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: --enable-auto-tool-choice --tensor-parallel-size 2 ``` I'm posting my request on the /v1/chat/completions API, with stream=true, temperature=0.15, max_tokens=131072. Messages include the system prompt privided by Mistra...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
