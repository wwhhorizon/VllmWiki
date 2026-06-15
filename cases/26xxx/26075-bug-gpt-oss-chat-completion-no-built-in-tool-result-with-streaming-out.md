# vllm-project/vllm#26075: [Bug][gpt-oss]: Chat completion no built-in tool result with streaming output

| 字段 | 值 |
| --- | --- |
| Issue | [#26075](https://github.com/vllm-project/vllm/issues/26075) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug][gpt-oss]: Chat completion no built-in tool result with streaming output

### Issue 正文摘录

### Your current environment `` ### 🐛 Describe the bug When I previously tested the Llama Stack Responses API, I found that using the gpt-oss-20b inference with vLLM could not produce proper outputs. Its design converts the Responses request into a Chat Completions request with built-in tools, sent to vLLM in streaming mode. I noticed that the corresponding Chat Completions request places the function call results in the Analysis Channel, but the current streaming implementation for Harmony only handles the Tool parser in the Commentary Channel. As a result, all output ends up in reasoning_content. In the non-streaming case, however, the output differs from streaming because extract_tool_calls does not process based on channels, and instead directly outputs the tool_calls results. The Harmony Cookbook mentions: > “Any function tool call will typically be triggered on the commentary channel while built-in tools will normally be triggered on the analysis channel.” Should the Tool parser also be included in the analysis channel? Test curl command ``` curl http://localhost:5000/v1/chat/completions \ -H "Content-Type: application/json" \ -H "Authorization: Bearer test" \ -d '{ "model":...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug][gpt-oss]: Chat completion no built-in tool result with streaming output bug ### Your current environment `` ### 🐛 Describe the bug When I previously tested the Llama Stack Responses API, I found that using the gpt...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ype": "function", "function": {"name": "open", "description": "Opens the link `id` from the page indicated by `cursor` starting at line number `loc`, showing `num_lines` lines.\nValid link ids are displayed with the for...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: } ], "tools": [{"type": "function", "function": {"name": "search", "description": "Searches for information related to `query` and displays `topn` results.", "parameters": {"type": "object", "properties": {"query": {"ty...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: vLLM could not produce proper outputs. Its design converts the Responses request into a Chat Completions request with built-in tools, sent to vLLM in streaming mode. I noticed that the corresponding Chat Completions req...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: our current environment `` ### 🐛 Describe the bug When I previously tested the Llama Stack Responses API, I found that using the gpt-oss-20b inference with vLLM could not produce proper outputs. Its design converts the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
