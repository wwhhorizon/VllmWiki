# vllm-project/vllm#9312: [Bug]: api_server.py: error: argument --tool-call-parser: invalid choice: 'llama3_json' (choose from 'mistral', 'hermes')

| 字段 | 值 |
| --- | --- |
| Issue | [#9312](https://github.com/vllm-project/vllm/issues/9312) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: api_server.py: error: argument --tool-call-parser: invalid choice: 'llama3_json' (choose from 'mistral', 'hermes')

### Issue 正文摘录

### Your current environment running on k8s 0.6.2 ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am trying to get Llama3 tools working and according to the docs https://github.com/vllm-project/vllm/blob/main/docs/source/serving/openai_compatible_server.md#tool-calling-in-the-chat-completion-api-1 there is an option for llama3_json which I would guess is for supporting llama 3 models? api_server.py: error: argument --tool-call-parser: invalid choice: 'llama3_json' (choose from 'mistral', 'hermes') if I select hermes I get this error ``` openai.BadRequestError: Error code: 400 - {'object': 'error', 'message': "[{'type': 'extra_forbidden', 'loc': ('body', 'functions'), 'msg': 'Extra inputs are not permitted', 'input': [{'name': 'get_current_weather', 'description': 'Get the current weather in a given location.', 'parameters': {'type': 'object', 'properties': {'location': {'type': 'string', 'description': 'The location for which to get the weather.'}}, 'required': ['location']}}, {'name': 'calculate_factorial', 'description': 'Calculate the factorial of a number.', 'parameters': {'type': 'object', 'properties': {'n': {'type': 'integer', 'description': 'A positive integer...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ug]: api_server.py: error: argument --tool-call-parser: invalid choice: 'llama3_json' (choose from 'mistral', 'hermes') bug ### Your current environment running on k8s 0.6.2 ### Model Input Dumps _No response_ ### 🐛 Des...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ceive, sender) File "/usr/local/lib/python3.12/dist-packages/starlette/routing.py", line 715, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.12/dist-packages/starlette/routing...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ceive, sender) File "/usr/local/lib/python3.12/dist-packages/starlette/routing.py", line 715, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.12/dist-packages/starlette/routing...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 'mistral', 'hermes') if I select hermes I get this error ``` openai.BadRequestError: Error code: 400 - {'object': 'error', 'message': "[{'type': 'extra_forbidden', 'loc': ('body', 'functions'), 'msg': 'Extra inputs are...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
