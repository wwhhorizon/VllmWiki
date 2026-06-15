# vllm-project/vllm#16190: [Bug]: Mistral tool parser failed to parse function calling

| 字段 | 值 |
| --- | --- |
| Issue | [#16190](https://github.com/vllm-project/vllm/issues/16190) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Mistral tool parser failed to parse function calling

### Issue 正文摘录

### Your current environment vllm version `0.8.3` ### 🐛 Describe the bug I used mistral parser to get the function calling from mistral3.1 -AWQ model. The output looks good as content text but vllm mistral parser failed to parse it as function calling output. - command: ``` VLLM_USE_V1=0 vllm serve OPEA/Mistral-Small-3.1-24B-Instruct-2503-int4-AutoRound-awq-sym \ --max-model-len 4096 --gpu-memory-utilization 0.8 --distributed-executor-backend ray --dtype float16 \ --tool-call-parser mistral --enable-auto-tool-choice --chat-template tool_chat_template_mistral3.1_json.jinja ``` - Request: ``` { "model": "OPEA/Mistral-Small-3.1-24B-Instruct-2503-int4-AutoRound-awq-sym", "messages": [ { "content": "What's the weather like in San Francisco in Celsius?", "role": "user" } ], "max_completion_tokens": 128, "tools": [ { "type": "function", "function": { "name": "get_weather", "description": "Get the current weather in a given location", "parameters": { "type": "object", "properties": { "location": { "type": "string", "description": "City and state, e.g., 'San Francisco, CA'" }, "unit": { "type": "string", "enum": [ "celsius", "fahrenheit" ] } }, "required": [ "location", "unit" ] } } } ], "...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ``` VLLM_USE_V1=0 vllm serve OPEA/Mistral-Small-3.1-24B-Instruct-2503-int4-AutoRound-awq-sym \ --max-model-len 4096 --gpu-memory-utilization 0.8 --distributed-executor-backend ray --dtype float16 \ --tool-call-parser mi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: I used mistral parser to get the function calling from mistral3.1 -AWQ model. The output looks good as content text but vllm mistral parser failed to parse it as function calling output. - command: ``` VLLM_USE_V1=0 vll...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: d to parse function calling bug;stale ### Your current environment vllm version `0.8.3` ### 🐛 Describe the bug I used mistral parser to get the function calling from mistral3.1 -AWQ model. The output looks good as conte...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: calling output. - command: ``` VLLM_USE_V1=0 vllm serve OPEA/Mistral-Small-3.1-24B-Instruct-2503-int4-AutoRound-awq-sym \ --max-model-len 4096 --gpu-memory-utilization 0.8 --distributed-executor-backend ray --dtype floa...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ssages[0]['content'] %} {%- set loop_messages = messages[1:] %} {%- else %} {%- set system_message = default_system_message %} {%- set loop_messages = messages %} {%- endif %} {%- set user_messages = loop_messages | sel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
