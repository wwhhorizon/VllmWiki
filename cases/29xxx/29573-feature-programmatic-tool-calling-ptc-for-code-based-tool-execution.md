# vllm-project/vllm#29573: [Feature]:  Programmatic Tool Calling (PTC) for code based tool execution

| 字段 | 值 |
| --- | --- |
| Issue | [#29573](https://github.com/vllm-project/vllm/issues/29573) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]:  Programmatic Tool Calling (PTC) for code based tool execution

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When using tool calling with LLMs, each tool invocation requires a separate model turn, leading to: - High latency for multi-tool workflows - Increased token consumption from repeated context - Limited ability to perform complex logic (filtering, aggregation, conditionals) across tool results xref: - Anthropic's https://www.anthropic.com/engineering/advanced-tool-use - Anthropic's https://www.anthropic.com/engineering/code-execution-with-mcp - MCP Server with Code Execution https://github.com/harche/ProDisco **Proposed Feature**: Programmatic Tool Calling (PTC) allows models to write Python code that orchestrates multiple tool calls within a secure sandbox. Instead of returning individual tool calls, the model generates code that: - Calls multiple tools programmatically - Processes results with Python logic (loops, filters, aggregations) - Returns only the final result to the model context ### Alternatives Multiple sequential tool calls, current approach, works but incurs high latency and token cost for complex workflows ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevan...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: : Programmatic Tool Calling (PTC) for code based tool execution feature request;stale ### 🚀 The feature, motivation and pitch When using tool calling with LLMs, each tool invocation requires a separate model turn, leadi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ach tool invocation requires a separate model turn, leading to: - High latency for multi-tool workflows - Increased token consumption from repeated context - Limited ability to perform complex logic (filtering, aggregat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ecution-with-mcp - MCP Server with Code Execution https://github.com/harche/ProDisco **Proposed Feature**: Programmatic Tool Calling (PTC) allows models to write Python code that orchestrates multiple tool calls within...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: n using tool calling with LLMs, each tool invocation requires a separate model turn, leading to: - High latency for multi-tool workflows - Increased token consumption from repeated context - Limited ability to perform c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
