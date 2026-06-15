# vllm-project/vllm#22885: [Bug]: tool_calls content loss } when use hermes_tool_parser

| 字段 | 值 |
| --- | --- |
| Issue | [#22885](https://github.com/vllm-project/vllm/issues/22885) |
| 状态 | closed |
| 标签 | bug;stale;tool-calling |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: tool_calls content loss } when use hermes_tool_parser

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When use qwen3-30b-a3b-instruct-2507,the generated tool_calls args content all loss '}' ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: '}' ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: alling ### Your current environment ### 🐛 Describe the bug When use qwen3-30b-a3b-instruct-2507,the generated tool_calls args content all loss '}' ### Before submitting a new issue... - [x] Make sure you already searche...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: tool_calls content loss } when use hermes_tool_parser bug;stale;tool-calling ### Your current environment ### 🐛 Describe the bug When use qwen3-30b-a3b-instruct-2507,the generated tool_calls args content all loss...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
