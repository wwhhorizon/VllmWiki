# vllm-project/vllm#17585: [Bug]: Mistral tool parser & streaming: corrupt tool_calls completions

| 字段 | 值 |
| --- | --- |
| Issue | [#17585](https://github.com/vllm-project/vllm/issues/17585) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Mistral tool parser & streaming: corrupt tool_calls completions

### Issue 正文摘录

With some tools & inputs, the streamed `tool_calls` content is missing some "punctuation" chars like `"` and `}`, and then in the last delta repeats already streamed chars. Example which reproduces with `mistralai/Ministral-8B-Instruct-2410` (and also with mistral-large 2411): start vLLM with: ``` vllm serve mistralai/Ministral-8B-Instruct-2410 --tokenizer_mode mistral --config_format mistral --load_format mistral --max-model-len 4096 --enable-auto-tool-choice --tool-call-parser mistral ``` ```python from openai import OpenAI client = OpenAI(base_url="http://localhost:8000/v1", api_key="dummy") tools = [{ "type": "function", "function": { "name": "mcp_confluence", "description": "Search Confluence", "parameters": { "type": "object", "properties": { "query": {"type": "string", "description": "Search query"}, "limit": {"type": "number", "description": "max results"} }, "required": ["query", "limit"] } } }] stream = client.chat.completions.create( model=client.models.list().data[0].id, messages=[ {"role": "user", "content": "Where is the coffee in the office?"} ], tools=tools, stream=True, temperature=0, ) for chunk in stream: for tool_call in chunk.choices[0].delta.tool_calls or []:...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: lm serve mistralai/Ministral-8B-Instruct-2410 --tokenizer_mode mistral --config_format mistral --load_format mistral --max-model-len 4096 --enable-auto-tool-choice --tool-call-parser mistral ``` ```python from openai im...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: nd then in the last delta repeats already streamed chars. Example which reproduces with `mistralai/Ministral-8B-Instruct-2410` (and also with mistral-large 2411): start vLLM with: ``` vllm serve mistralai/Ministral-8B-I...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e-auto-tool-choice --tool-call-parser mistral ``` ```python from openai import OpenAI client = OpenAI(base_url="http://localhost:8000/v1", api_key="dummy") tools = [{ "type": "function", "function": { "name": "mcp_confl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: function": { "name": "mcp_confluence", "description": "Search Confluence", "parameters": { "type": "object", "properties": { "query": {"type": "string", "description": "Search query"}, "limit": {"type": "number",
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ug]: Mistral tool parser & streaming: corrupt tool_calls completions bug;stale With some tools & inputs, the streamed `tool_calls` content is missing some "punctuation" chars like `"` and `}`, and then in the last delta...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
