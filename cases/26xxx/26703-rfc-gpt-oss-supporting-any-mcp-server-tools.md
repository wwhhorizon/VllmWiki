# vllm-project/vllm#26703: [RFC]: [gpt-oss] Supporting Any MCP Server Tools

| 字段 | 值 |
| --- | --- |
| Issue | [#26703](https://github.com/vllm-project/vllm/issues/26703) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: [gpt-oss] Supporting Any MCP Server Tools

### Issue 正文摘录

### Motivation. There are three main motivations: - vLLM should support integrating with all MCP servers - TODO: Test with enterprise ones like Github - Clean up gpt-oss tool specific code paths in vLLM - Tools and models change, but MCP is a protocol meant to support all models - Sets the stage for full MCP integration for all tool calling models - Avoid losing information due to lossy OpenAI types for output - An example below ``` # What you can return to the user on the ResponsesAPI for this tool call with the OpenAI types. class ActionOpenPage(TypedDict, total=False): type: Required[Literal["open_page"]] url: Required[str] # The interface for the actual tool call the model does open_link(ctx: Context, id: Union[int, str] = -1, cursor: int = -1, loc: int = -1, num_lines: int = -1, view_source: bool = False, source: Optional[str] = None) ``` This feature is similar to the concept of “connectors” because we still don’t support users specifying arbitrary MCP servers by URL yet, the list is static and owned by the server, which is more similar to the concept of [OpenAI MCP Connectors](https://platform.openai.com/docs/guides/tools-connectors-mcp#quickstart). ### Proposed Change. ###...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [RFC]: [gpt-oss] Supporting Any MCP Server Tools RFC;stale ### Motivation. There are three main motivations: - vLLM should support integrating with all MCP servers - TODO: Test with enterprise ones like Github - Clean u...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: - TODO: Test with enterprise ones like Github - Clean up gpt-oss tool specific code paths in vLLM - Tools and models change, but MCP is a protocol meant to support all models - Sets the stage for full MCP integration fo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: port ``` Then register it with your vLLM responses API server with: ``` CUDA_VISIBLE_DEVICES=6 vllm serve openai/gpt-oss-20b --tool-server=localhost:8765 ``` And then try it out with something like: ``` curl http://loca...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: tool call with the OpenAI types. class ActionOpenPage(TypedDict, total=False): type: Required[Literal["open_page"]] url: Required[str] # The interface for the actual tool call the model does open_link(ctx: Context, id:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [RFC]: [gpt-oss] Supporting Any MCP Server Tools RFC;stale ### Motivation. There are three main motivations: - vLLM should support integrating with all MCP servers - TODO: Test with enterprise ones like Github - Clean u...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
