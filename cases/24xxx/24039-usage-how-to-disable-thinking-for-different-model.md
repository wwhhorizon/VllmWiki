# vllm-project/vllm#24039: [Usage]: how to disable thinking for different model

| 字段 | 值 |
| --- | --- |
| Issue | [#24039](https://github.com/vllm-project/vllm/issues/24039) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to disable thinking for different model

### Issue 正文摘录

### Your current environment vllm 0.10.1 ### How would you like to use vllm I want to call model without thinking using v1/chat/completions interface: For glm4.5 model, the body is: { "model": "glm-4.5", "messages": message, "thinking": { "type": "disabled" }, "temperature": 0.6, "tools": tools } But for qwen3-8b model, the body is: payload = { "model": "qwen3-8b", "messages": message, "enable_thinking": False, "temperature": 0.6, "tools": tools } I found the body is different(glm4.5 using thinking key, qwen3 using enable_thinking key) for different. Is there no way to unify? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: how to disable thinking for different model usage;stale ### Your current environment vllm 0.10.1 ### How would you like to use vllm I want to call model without thinking using v1/chat/completions interface: For...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: fy? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ": "qwen3-8b", "messages": message, "enable_thinking": False, "temperature": 0.6, "tools": tools } I found the body is different(glm4.5 using thinking key, qwen3 using enable_thinking key) for different. Is there no way...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: how to disable thinking for different model usage;stale ### Your current environment vllm 0.10.1 ### How would you like to use vllm I want to call model without thinking using v1/chat/completions interface: For...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
