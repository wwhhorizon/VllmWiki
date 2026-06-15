# vllm-project/vllm#27356: [Feature]: Support usage of server_url as a tool parameter to dynamically connect to MCP servers

| 字段 | 值 |
| --- | --- |
| Issue | [#27356](https://github.com/vllm-project/vllm/issues/27356) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support usage of server_url as a tool parameter to dynamically connect to MCP servers

### Issue 正文摘录

### 🚀 The feature, motivation and pitch To fully flesh out the functionality of the responses API and tool calling, I think that this should be supported as well. More info in the additional context section. ### Alternatives _No response_ ### Additional context I've read through #14721, this [comment](https://github.com/vllm-project/vllm/issues/14721#issuecomment-3426399227) points out that additional issues should be raised for further responses api support. This [support thread](https://discuss.vllm.ai/t/mcp-tool-server-openai-responses-api/1665/4) point out that the --tool-server param has to be used on startup for MCP servers. The OpenAPI docs [here](https://platform.openai.com/docs/guides/tools-connectors-mcp#quickstart) mentioned the support of the server_url param for remote MCP servers. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: er_url as a tool parameter to dynamically connect to MCP servers feature request;stale ### 🚀 The feature, motivation and pitch To fully flesh out the functionality of the responses API and tool calling, I think that thi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
