# vllm-project/vllm#29562: [Bug]: "\n\n" content between reasoning and tool_call content when tool_call and stream mode

| 字段 | 值 |
| --- | --- |
| Issue | [#29562](https://github.com/vllm-project/vllm/issues/29562) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: "\n\n" content between reasoning and tool_call content when tool_call and stream mode

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug https://github.com/QwenLM/Qwen3/issues/1755 When stream mode true, the response contains content "\n\n" between reasoning and tool_call; but with stream model false, it didn't generate content "\n\n". Is there some thing different, I don't want the content "\n\n" between reasoning and tool_call. Here is my requests: ``` { "model": "Qwen3-235B-A22B-Thinking-2507", "tools": [ { "type": "function", "function": { "name": "search_law_articles", "parameters": { "type": "object", "properties": { "level": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "description": "搜索条件：法规类型" }, "query": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "description": "查询语句" }, "title": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "description": "法律标题" }, "article": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "description": "法律条款序号，如 第十条" }, "content": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "description": "法律条款及内容，如 第十条 贷款人委托支付" }, "pub_department": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "def...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Your current environment ### 🐛 Describe the bug https://github.com/QwenLM/Qwen3/issues/1755 When stream mode true, the response contains content "\n\n" between reasoning and tool_call; but with stream model false, it di...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: tween reasoning and tool_call content when tool_call and stream mode bug;stale ### Your current environment ### 🐛 Describe the bug https://github.com/QwenLM/Qwen3/issues/1755 When stream mode true, the response contains...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [ { "type": "function", "function": { "name": "search_law_articles", "parameters": { "type": "object", "properties": { "level": { "anyOf": [ { "type": "string" },
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: content "\n\n" between reasoning and tool_call; but with stream model false, it didn't generate content "\n\n". Is there some thing different, I don't want the content "\n\n" between reasoning and tool_call. Here is my...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
