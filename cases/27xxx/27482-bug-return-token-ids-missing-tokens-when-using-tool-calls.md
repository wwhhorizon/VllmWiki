# vllm-project/vllm#27482: [Bug]: `return_token_ids` missing tokens when using tool calls

| 字段 | 值 |
| --- | --- |
| Issue | [#27482](https://github.com/vllm-project/vllm/issues/27482) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `return_token_ids` missing tokens when using tool calls

### Issue 正文摘录

### Your current environment Testing with latest vLLM builds from main, as of Fri Oct 24th 2025 (when this bug was opened). ### 🐛 Describe the bug The `return_token_ids` parameter that is supposed to return all generated token ids back to the client is missing quite a few tokens for Chat Completion streaming requests that result in tool calls being generated. Exactly how many and where they are missing in the request will depend on the tool call parser in use as well as the exact request format. Here's a minimal reproducer. First, run vLLM with a tool call parser and model. I use a Granite model for testing here, but it should be roughly the same for any model with a tool call parser. ``` vllm serve ibm-granite/granite-3.3-8b-instruct \ --enable-auto-tool-choice \ --tool-call-parser granite ``` Then, send a streaming tool call request to the server and check the response for missing tokens: ```python from openai import OpenAI client = OpenAI(base_url="http://localhost:8000/v1", api_key="fake") tools = [ { "type": "function", "function": { "name": "get_current_weather", "description": "Get the current weather in a given location", "parameters": { "type": "object", "properties": { "...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ng tool calls bug ### Your current environment Testing with latest vLLM builds from main, as of Fri Oct 24th 2025 (when this bug was opened). ### 🐛 Describe the bug The `return_token_ids` parameter that is supposed to r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: will depend on the tool call parser in use as well as the exact request format. Here's a minimal reproducer. First, run vLLM with a tool call parser and model. I use a Granite model for testing here, but it should be ro...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: all parser in use as well as the exact request format. Here's a minimal reproducer. First, run vLLM with a tool call parser and model. I use a Granite model for testing here, but it should be roughly the same for any mo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 063 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: end(choice.token_ids) num_token_ids = len(choice.token_ids) else: num_token_ids = 0 elapsed_completion_tokens = usage.completion_tokens - last_completion_tokens if elapsed_completion_tokens != num_token_ids: raise Value...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
