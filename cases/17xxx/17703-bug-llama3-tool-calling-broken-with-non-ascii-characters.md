# vllm-project/vllm#17703: [Bug]: Llama3 tool calling broken with non-ascii characters

| 字段 | 值 |
| --- | --- |
| Issue | [#17703](https://github.com/vllm-project/vllm/issues/17703) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Llama3 tool calling broken with non-ascii characters

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using the `llama3_json` tool call parser in streaming mode with non-ascii characters in the tool arguments an additional `DeltaToolMessage` is yielded (containing the full argument dict) after the arguments were already streamed. For brevity I will omit the tool definition. The example uses the example weather tool provided [here](https://docs.vllm.ai/en/latest/features/tool_calling.html). ```python import openai client = openai.OpenAI(...) response = client.chat.completions.create( model="SOME_LLAMA3_MODEL_WITH_LLAMA3_JSON_TOOL_CALL_PARSER, messages=[{"role": "user", "content": "Wie ist das Wetter in Münster?"}], tools=tools, tool_choice="auto", stream=True, ) for chunk in response: print(chunk) ``` The expected output would be something along the lines of ``` ChatCompletionChunk(id='chatcmpl-9fcd4cff278d4cfe8038f985c8088262', choices=[Choice(delta=ChoiceDelta(content='', function_call=None, refusal=None, role='assistant', tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1746517938, model='llama3', object='chat.completion.chunk', service_tier=None, system_fingerprint=None, usage=None) ChatCompletionCh...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Llama3 tool calling broken with non-ascii characters bug ### Your current environment ### 🐛 Describe the bug When using the `llama3_json` tool call parser in streaming mode with non-ascii characters in the tool a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ge. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Llama3 tool calling broken with non-ascii characters bug ### Your current environment ### 🐛 Describe the bug When using the `llama3_json` tool call parser in streaming mode with non-ascii characters in the tool a...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pi;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: OpenAIServingChat` compares already sent arguments using `ensure_ascii=False` (which is compatible with e.g. the `hermes` and `mistral` tool call parsers). This leads to `OpenAIServingChat` erroneously thinking it still...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
