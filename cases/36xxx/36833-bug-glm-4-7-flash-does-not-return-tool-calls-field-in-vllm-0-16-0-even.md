# vllm-project/vllm#36833: [Bug]: GLM-4.7-Flash does not return tool_calls field in vLLM 0.16.0 even with --tool-call-parser glm47

| 字段 | 值 |
| --- | --- |
| Issue | [#36833](https://github.com/vllm-project/vllm/issues/36833) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GLM-4.7-Flash does not return tool_calls field in vLLM 0.16.0 even with --tool-call-parser glm47

### Issue 正文摘录

### Your current environment Hi, I am trying to deploy GLM-4.7-Flash using vLLM 0.16.0 and enable tool calling. However, the response does not include the `tool_calls` field even though the tool parser is configured. Environment: - vLLM version: 0.16.0 - Model: GLM-4.7-Flash - GPU: NVIDIA RTX A6000 - CUDA version: 12.4 Startup command: vllm serve /path/to/GLM-4.7-Flash \ --port 8000 \ --tool-call-parser glm47 \ --enable-auto-tool-choice Request example: POST /v1/chat/completions ``` { "model": "GLM-4.7-Flash", "messages": [ {"role": "user", "content": "What is the weather in Beijing today?"} ], "tools": [ { "type": "function", "function": { "name": "get_weather", "description": "Get the current weather", "parameters": { "type": "object", "properties": { "location": {"type": "string"} }, "required": ["location"] } } } ] } ``` Expected behavior: The response should include a `tool_calls` field indicating that the model wants to call the function. Actual behavior: The response only returns normal text and does not contain the `tool_calls` field. Is there any additional configuration required for GLM-4.7-Flash to enable tool calling in vLLM? Thanks!

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Environment: - vLLM version: 0.16.0 - Model: GLM-4.7-Flash - GPU: NVIDIA RTX A6000 - CUDA version: 12.4 Startup command: vllm serve /path/to/GLM-4.7-Flash \ --port 8000 \ --tool-call-parser glm47 \ --enable-auto-tool-ch...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: e does not include the `tool_calls` field even though the tool parser is configured. Environment: - vLLM version: 0.16.0 - Model: GLM-4.7-Flash - GPU: NVIDIA RTX A6000 - CUDA version: 12.4 Startup command: vllm serve /p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s` field even though the tool parser is configured. Environment: - vLLM version: 0.16.0 - Model: GLM-4.7-Flash - GPU: NVIDIA RTX A6000 - CUDA version: 12.4 Startup command: vllm serve /path/to/GLM-4.7-Flash \ --port 800...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: --port 8000 \ --tool-call-parser glm47 \ --enable-auto-tool-choice Request example: POST /v1/chat/completions ``` { "model": "GLM-4.7-Flash", "messages": [ {"role": "user", "content": "What is the weather in Beijing tod...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
