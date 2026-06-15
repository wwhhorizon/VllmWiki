# vllm-project/vllm#20678: [Bug]: Streaming Inference Truncates Tool Arguments in Qwen3 Models

| 字段 | 值 |
| --- | --- |
| Issue | [#20678](https://github.com/vllm-project/vllm/issues/20678) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Streaming Inference Truncates Tool Arguments in Qwen3 Models

### Issue 正文摘录

### Your current environment vllm 0.9.2 and so on ### 🐛 Describe the bug When running inference on Qwen3-related models, whether the thinking mode is enabled or not, it is impossible to obtain accurate and complete arguments in tool_call with stream=True enabled, as there is a certain degree of data truncation. Issues like #18220 and #19056 have encountered similar problems. Although #18220 submitted a related fix, the corresponding code changes were not merged into hermstools for some unknown reason. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Streaming Inference Truncates Tool Arguments in Qwen3 Models bug;stale ### Your current environment vllm 0.9.2 and so on ### 🐛 Describe the bug When running inference on Qwen3-related models, whether the thinking...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Streaming Inference Truncates Tool Arguments in Qwen3 Models bug;stale ### Your current environment vllm 0.9.2 and so on ### 🐛 Describe the bug When running inference on Qwen3-related models, whether the thinking...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
