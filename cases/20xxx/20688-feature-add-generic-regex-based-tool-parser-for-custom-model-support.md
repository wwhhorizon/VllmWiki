# vllm-project/vllm#20688: [Feature] Add Generic Regex-based Tool Parser for Custom Model Support

| 字段 | 值 |
| --- | --- |
| Issue | [#20688](https://github.com/vllm-project/vllm/issues/20688) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature] Add Generic Regex-based Tool Parser for Custom Model Support

### Issue 正文摘录

## Motivation Currently, vLLM requires a dedicated tool parser implementation for each model that supports tool/function calling. When using a new model that doesn't have a specific parser implementation, users cannot leverage the tool calling functionality even if the model supports it with a predictable output format. Many models follow similar patterns for tool calls (e.g., JSON within specific delimiters), making it possible to create a configurable parser that uses regex patterns to extract tool calls. This would significantly improve the flexibility of vLLM's tool calling support. ## Proposed Change Add a new `RegexToolParser` class that can be configured with custom regex patterns during engine initialization. This parser would: 1. Accept regex patterns as configuration parameters 2. Use these patterns to detect and extract tool calls from model outputs 3. Support both streaming and non-streaming modes 4. Handle multiple tool calls in a single response ### Example Usage ```python # When starting vLLM with a custom model vllm serve my-custom-model \ --enable-auto-tool-choice \ --tool-call-parser regex \ --tool-parser-config '{ "tool_call_pattern": " (.*?) ", "function_patter...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature] Add Generic Regex-based Tool Parser for Custom Model Support ## Motivation Currently, vLLM requires a dedicated tool parser implementation for each model that supports tool/function calling. When using a new m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: rts tool/function calling. When using a new model that doesn't have a specific parser implementation, users cannot leverage the tool calling functionality even if the model supports it with a predictable output format....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: terns internally - This would not replace existing parsers but provide a fallback option for unsupported models - The configuration could be extended to support different formats (JSON, XML-like, custom delimiters) - Ba...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: mplementation for each model**: This is the current approach but doesn't scale well as new models are released frequently. 2. **Heuristic-based parsing**: Using common patterns without configuration would be less flexib...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: egex to extract tool calls tool_match = self.tool_call_pattern.search(model_output) if not tool_match: return ExtractedToolCallInformation(tools_called=False, tool_calls=[],

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
