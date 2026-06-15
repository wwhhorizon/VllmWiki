# vllm-project/vllm#30999: [Feature] GLM45 tool parser: Stream tool name before full arguments

| 字段 | 值 |
| --- | --- |
| Issue | [#30999](https://github.com/vllm-project/vllm/issues/30999) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature] GLM45 tool parser: Stream tool name before full arguments

### Issue 正文摘录

## Feature Request ### Problem Description When using GLM-4.5 with tool calling (`--tool-call-parser glm45`), the current parser waits for the complete tool call structure before returning anything to the client. For long-running tool calls (e.g., generating articles with a `write_article` tool), this creates poor user experience: - Users see nothing during generation - Users don't know what the model is doing - No way to provide early feedback about which tool was selected ### Proposed Solution Stream the tool name as soon as it's available, before the arguments are complete. This follows the pattern used by other parsers like Hermes (used by Qwen), which incrementally outputs tool call information. **Current behavior:** ``` wait... wait... wait... -> complete tool_call with name + arguments ``` **Desired behavior:** ``` -> DeltaMessage with tool name -> DeltaMessage with partial arguments -> DeltaMessage with more arguments -> ... ``` ### Use Case When a user asks the model to write a long article, the model might call a tool like: ```json {"name": "write_article", "parameters": {"topic": "...", "content": "very long content..."}} ``` With incremental streaming, the user would i...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ience: - Users see nothing during generation - Users don't know what the model is doing - No way to provide early feedback about which tool was selected ### Proposed Solution Stream the tool name as soon as it's availab...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: oring tool parsers for better streaming support ### Environment - vLLM version: latest - Model: GLM-4.5 series (GLM-4.5-Air, etc.) - Parser: `--tool-call-parser glm45`
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: re] GLM45 tool parser: Stream tool name before full arguments ## Feature Request ### Problem Description When using GLM-4.5 with tool calling (`--tool-call-parser glm45`), the current parser waits for the complete tool...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: parsers for better streaming support ### Environment - vLLM version: latest - Model: GLM-4.5 series (GLM-4.5-Air, etc.) - Parser: `--tool-call-parser glm45`

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
