# vllm-project/vllm#16958: [Bug]: AssertionError: skip_special_tokens=False is not supported for Mistral tokenizers

| 字段 | 值 |
| --- | --- |
| Issue | [#16958](https://github.com/vllm-project/vllm/issues/16958) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AssertionError: skip_special_tokens=False is not supported for Mistral tokenizers

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` bash vllm serve stelterlab/Mistral-Small-24B-Instruct-2501-AWQ --tool-call-parser mistral --enable-auto-tool-choice --tokenizer-mode mistral --guided-decoding-backend xgrammar ``` ``` python from lmformatenforcer.external.jsonschemaobject import JsonSchemaObject from openai import OpenAI openai_api_key = "EMPTY" openai_api_base = "http://localhost:8000/v1" client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) tools = [ { "type": "function", "function": { "name": "get_current_weather", "description": "Get the current weather in a given location", "parameters": { "type": "object", "properties": { "city": { "type": "string", "description": "The city to find the weather for, e.g. 'Vienna'", "default": "Vienna", }, "country": { "type": "string", "description": "The country that the city is in, e.g. 'Austria'", }, "unit": { "type": "string", "description": "The unit to fetch the temperature in", "enum": ["celsius", "fahrenheit"], }, }, "required": ["country", "unit"], }, }, }, { "type": "function", "function": { "name": "get_forecast", "description": "Get the weather forecast for a given location", "parameters": { "t...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: er-mode mistral --guided-decoding-backend xgrammar ``` ``` python from lmformatenforcer.external.jsonschemaobject import JsonSchemaObject from openai import OpenAI openai_api_key = "EMPTY" openai_api_base = "http://loca...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: AssertionError: skip_special_tokens=False is not supported for Mistral tokenizers bug ### Your current environment ### 🐛 Describe the bug ``` bash vllm serve stelterlab/Mistral-Small-24B-Instruct-2501-AWQ --tool-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nment ### 🐛 Describe the bug ``` bash vllm serve stelterlab/Mistral-Small-24B-Instruct-2501-AWQ --tool-call-parser mistral --enable-auto-tool-choice --tokenizer-mode mistral --guided-decoding-backend xgrammar ``` ``` py...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: lm/v1/engine/async_llm.py", line 277, in generate q = await self.add_request( ^^^^^^^^^^^^^^^^^^^^^^^ File "/root/vllm/vllm/v1/engine/async_llm.py", line 215, in add_request await self._add_request(request, None, 0, que...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: --enable-auto-tool-choice --tokenizer-mode mistral --guided-decoding-backend xgrammar ``` ``` python from lmformatenforcer.external.jsonschemaobject import JsonSchemaObject from openai import OpenAI openai_api_key = "EM...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
