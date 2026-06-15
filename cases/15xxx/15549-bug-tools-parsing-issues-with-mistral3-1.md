# vllm-project/vllm#15549: [Bug]: Tools parsing issues with mistral3.1

| 字段 | 值 |
| --- | --- |
| Issue | [#15549](https://github.com/vllm-project/vllm/issues/15549) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Tools parsing issues with mistral3.1

### Issue 正文摘录

### Your current environment vllm 0.8.1 ### 🐛 Describe the bug seems there is an issue with mistral for tools parsing? the output is not function calling as expected. - command: `serve mistralai/Mistral-Small-3.1-24B-Base-2503 --max-model-len 4096 --gpu-memory-utilization 0.9 --tensor-parallel-size 4 --served-model-name mistral --tokenizer-mode mistral --config-format mistral --load_format mistral --tool-call-parser mistral --enable-auto-tool-choice ` example: - request: ``` { "model":"mistral", "messages": [ { "content": "What's the weather like in San Francisco?", "role": "user" } ], "max_completion_tokens": 128, "tools": [ { "type": "function", "function": { "name": "get_weather", "description": "Get the current weather in a given location", "parameters": { "type": "object", "properties": { "location": { "type": "string", "description": "City and state, e.g., 'San Francisco, CA'" }, "unit": { "type": "string", "enum": [ "celsius", "fahrenheit" ] } }, "required": [ "location", "unit" ] } } } ], "tool_choice": "auto" } ``` - response: ``` { "id": "chatcmpl-4dccab14c6b64bf7a3a0454346945d26", "object": "chat.completion", "created": 1742994086, "model": "mistral", "choices": [ { "in...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: cted. - command: `serve mistralai/Mistral-Small-3.1-24B-Base-2503 --max-model-len 4096 --gpu-memory-utilization 0.9 --tensor-parallel-size 4 --served-model-name mistral --tokenizer-mode mistral --config-format mistral -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: : [ { "content": "What's the weather like in San Francisco?", "role": "user" } ], "max_completion_tokens": 128, "tools": [ { "type": "function", "function": { "name": "get_weather",
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: s not function calling as expected. - command: `serve mistralai/Mistral-Small-3.1-24B-Base-2503 --max-model-len 4096 --gpu-memory-utilization 0.9 --tensor-parallel-size 4 --served-model-name mistral --tokenizer-mode mis...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Tools parsing issues with mistral3.1 bug;stale ### Your current environment vllm 0.8.1 ### 🐛 Describe the bug seems there is an issue with mistral for tools parsing? the output is not function calling as expected...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
