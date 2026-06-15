# vllm-project/vllm#22337: [Usage]: gpt-oss-120b tool calls

| 字段 | 值 |
| --- | --- |
| Issue | [#22337](https://github.com/vllm-project/vllm/issues/22337) |
| 状态 | closed |
| 标签 | usage;stale;gpt-oss |
| 评论 | 33; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: gpt-oss-120b tool calls

### Issue 正文摘录

### Your current environment first, lanuch an OpenAI server: ```sh vllm serve /mnt/model/gpt-oss-120b \ --port 8120 \ --tensor-parallel-size 8 \ --api-key "gpt_oss" ``` testing code: ```py from openai import OpenAI client = OpenAI( base_url="http://localhost:8120/v1", api_key="gpt_oss" ) tools = [ { "type": "function", "function": { "name": "get_weather", "description": "Get current weather in a given city", "parameters": { "type": "object", "properties": {"city": {"type": "string"}}, "required": ["city"] }, }, } ] response = client.chat.completions.create( model="/mnt/model/gpt-oss-120b", messages=[{"role": "user", "content": "What's the weather in Berlin right now?"}], tools=tools, tool_choice="required" ) print(response.choices[0].message) ``` but I get the message without `tool_calls` parsed. ```text ChatCompletionMessage(content='[{ "name": "get_weather", "parameters": { "city": "Berlin" } }]', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=[], reasoning_content="The user asks current weather in Berlin. As AI, we don't have real-time data. We must say we can't retrieve real-time info, suggest checking a weather site or app. Follow...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: gpt-oss-120b tool calls usage;stale;gpt-oss ### Your current environment first, lanuch an OpenAI server: ```sh vllm serve /mnt/model/gpt-oss-120b \ --port 8120 \ --tensor-parallel-size 8 \ --api-key "gpt_oss
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: lel-size 8 \ --api-key "gpt_oss" ``` testing code: ```py from openai import OpenAI client = OpenAI( base_url="http://localhost:8120/v1", api_key="gpt_oss" ) tools = [ { "type": "function", "function": { "name": "get_wea...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: gpt-oss-120b tool calls usage;stale;gpt-oss ### Your current environment first, lanuch an OpenAI server: ```sh vllm serve /mnt/model/gpt-oss-120b \ --port 8120 \ --tensor-parallel-size 8 \ --api-key "gpt_oss" `...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: --port 8120 \ --tensor-parallel-size 8 \ --api-key "gpt_oss" ``` testing code: ```py from openai import OpenAI client = OpenAI( base_url="http://localhost:8120/v1", api_key="gpt_oss" ) tools = [ { "type": "function", "f...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
