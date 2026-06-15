# vllm-project/vllm#19861: [Bug]: max_completion_tokens doesn't work as max

| 字段 | 值 |
| --- | --- |
| Issue | [#19861](https://github.com/vllm-project/vllm/issues/19861) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: max_completion_tokens doesn't work as max

### Issue 正文摘录

### Your current environment "version": "0.8.5.post1" ### 🐛 Describe the bug Request ``` { "model": "Qwen/Qwen2.5-Coder-7B-Instruct-AWQ", "messages": [ { "role": "system", "content": "" }, { "role": "user", "content": "0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ment "version": "0.8.5.post1" ### 🐛 Describe the bug Request ``` { "model": "Qwen/Qwen2.5-Coder-7B-Instruct-AWQ", "messages": [ { "role": "system", "content": "" }, { "role": "user", "content": "0 0 0 1 0 0 0 0 0 0 0 0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: max_completion_tokens doesn't work as max bug;stale ### Your current environment "version": "0.8.5.post1" ### 🐛 Describe the bug Request ``` { "model": "Qwen/Qwen2.5-Coder-7B-Instruct-AWQ", "messages": [ { "role"...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: tion_tokens doesn't work as max bug;stale ### Your current environment "version": "0.8.5.post1" ### 🐛 Describe the bug Request ``` { "model": "Qwen/Qwen2.5-Coder-7B-Instruct-AWQ", "messages": [ { "role": "system", "cont...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: } ], "temperature": 0, "max_completion_tokens":100, "stream": false } ``` vllm refuses to generate a response with such an error. ``` { "object": "error", "message": "This model's maximum context length is 2000 tokens....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
