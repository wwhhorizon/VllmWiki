# vllm-project/vllm#7827: [Bug]: tool_calls parsing error with CPU 

| 字段 | 值 |
| --- | --- |
| Issue | [#7827](https://github.com/vllm-project/vllm/issues/7827) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: tool_calls parsing error with CPU 

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python from openai import OpenAI if __name__ == "__main__": model = "mistralai/Mistral-7B-Instruct-v0.3" llm = OpenAI(base_url="http://100.83.111.250:8000/v1", api_key="EMPTY") input = [{"role": "user", "content": "What's the weather like in Boston today?"}] tools = [{ "type": "function", "function": { "name": "get_current_weather", "description": "Get the current weather in a given location", "parameters": { "type": "object", "properties": { "location": { "type": "string", "description": "The city and state, e.g. San Francisco, CA", }, "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}, }, "required": ["location"], }, } }] tool_choice = {'function': {'name': 'get_current_weather'}} output = llm.chat.completions.create( model=model, messages=input, tools=tools, tool_choice=tool_choice, stream=False, ) if content := output.choices[0].message.content: print('content:', content) elif tool_calls := output.choices[0].message.tool_calls: print('tool_calls:', tool_calls) ``` received output: ``` bash python test_openai_sdk.py tool_calls: [ChatCompletionMessageToolCall(id='chatcmpl-tool-a081c6fb632c4d7bbfd3ed00ac5a4399', fu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ur current environment ### 🐛 Describe the bug ```python from openai import OpenAI if __name__ == "__main__": model = "mistralai/Mistral-7B-Instruct-v0.3" llm = OpenAI(base_url="http://100.83.111.250:8000/v1", api_key="E...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: , tools=tools, tool_choice=tool_choice, stream=False, ) if content := output.choices[0].message.content: print('content:', content) elif tool_calls := output.choices[0].message.tool_calls: print('tool_calls:', tool_call...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ```python from openai import OpenAI if __name__ == "__main__": model = "mistralai/Mistral-7B-Instruct-v0.3" llm = OpenAI(base_url="http://100.83.111.250:8000/v1", api_key="EMPTY") input = [{"role": "user", "content": "W...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: tool_calls parsing error with CPU bug;stale ### Your current environment ### 🐛 Describe the bug ```python from openai import OpenAI if __name__ == "__main__": model = "mistralai/Mistral-7B-Instruct-v0.3" llm = Op...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
