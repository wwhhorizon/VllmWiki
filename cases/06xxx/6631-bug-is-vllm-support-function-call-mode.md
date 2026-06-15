# vllm-project/vllm#6631: [Bug]: Is vllm support function call mode?

| 字段 | 值 |
| --- | --- |
| Issue | [#6631](https://github.com/vllm-project/vllm/issues/6631) |
| 状态 | closed |
| 标签 | bug;unstale;tool-calling |
| 评论 | 33; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Is vllm support function call mode?

### Issue 正文摘录

### Your current environment Device: Nvidia GeForce 4090 software: vllm 0.5.2 + openai 1.30.5 + transformes 4.42.4 ### 🐛 Describe the bug I use OpenAI api and vllm to deploy local Qwen2 llm, But vllm function call mode does not work. The OpenAI interface correctly passed the tools info parameters to vllm, but vllm did not use it. If I enable ' tool_choice="auto" 'parameter, I will encounter with 400 error code. ---------------------------------------------------------------------server script------------------------------------------------------------- python entrypoints/openai/api_server.py --model="xxx/Qwen2-1.5B-Instruct" --trust-remote-code --host "localhost" --port 8000 --dtype auto -------------------------------------------------------------client code ------------------------------------------------------------------ from openai import OpenAI tools = [ { "type": "function", "function": { "name": "get_current_weather", "description": "Get the current weather in a given location", "parameters": { "type": "object", "properties": { "location": { "type": "string", "description": "The city and state, e.g. San Francisco, CA", }, "unit": {"type": "string", "enum": ["celsius", "fah...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ----------------------------------------------------------- from openai import OpenAI tools = [ { "type": "function", "function": { "name": "get_current_weather", "description": "Get the current weather in a given locat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: .42.4 ### 🐛 Describe the bug I use OpenAI api and vllm to deploy local Qwen2 llm, But vllm function call mode does not work. The OpenAI interface correctly passed the tools info parameters to vllm, but vllm did not use...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Is vllm support function call mode? bug;unstale;tool-calling ### Your current environment Device: Nvidia GeForce 4090 software: vllm 0.5.2 + openai 1.30.5 + transformes 4.42.4 ### 🐛 Describe the bug I use OpenAI...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: wen2-1.5B-Instruct" --trust-remote-code --host "localhost" --port 8000 --dtype auto -------------------------------------------------------------client code --------------------------------------------------------------...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
