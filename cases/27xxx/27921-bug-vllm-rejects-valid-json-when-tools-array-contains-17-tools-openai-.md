# vllm-project/vllm#27921: [Bug]: vLLM rejects valid JSON when tools array contains 17+ tools (OpenAI format)

| 字段 | 值 |
| --- | --- |
| Issue | [#27921](https://github.com/vllm-project/vllm/issues/27921) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM rejects valid JSON when tools array contains 17+ tools (OpenAI format)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When sending a valid JSON request with 17 tools in the tools array, vLLM returns: 400 Bad Request {"error": {"message": "1 validation error for list[function-wrap[log_extra_fields()]]\n Invalid JSON: EOF while parsing a string at line 57", "type": "BadRequestError"}} The error location varies (lines 23, 57, 84, 171, 261, 271, 346, 1024 in different requests), but always reports "EOF while parsing" errors. The input_value in the error shows corrupted/truncated data (just newlines/whitespace). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: jects valid JSON when tools array contains 17+ tools (OpenAI format) bug;stale ### Your current environment ### 🐛 Describe the bug When sending a valid JSON request with 17 tools in the tools array, vLLM returns: 400 Ba...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ug]: vLLM rejects valid JSON when tools array contains 17+ tools (OpenAI format) bug;stale ### Your current environment ### 🐛 Describe the bug When sending a valid JSON request with 17 tools in the tools array, vLLM ret...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
