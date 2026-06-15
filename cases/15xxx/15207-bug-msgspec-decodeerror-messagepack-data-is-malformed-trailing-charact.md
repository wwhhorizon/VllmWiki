# vllm-project/vllm#15207: [Bug]: msgspec.DecodeError: MessagePack data is malformed: trailing characters (byte 13)

| 字段 | 值 |
| --- | --- |
| Issue | [#15207](https://github.com/vllm-project/vllm/issues/15207) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: msgspec.DecodeError: MessagePack data is malformed: trailing characters (byte 13)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I keep having this decode error when using vllm=0.8.0 for qwen-2.5 inference, I have the same error on both 1.5B and 7B model once I use apply-chat-template. `msgspec.DecodeError: MessagePack data is malformed: trailing characters (byte 13)` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: cribe the bug I keep having this decode error when using vllm=0.8.0 for qwen-2.5 inference, I have the same error on both 1.5B and 7B model once I use apply-chat-template. `msgspec.DecodeError: MessagePack data is malfo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 3)` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: msgspec.DecodeError: MessagePack data is malformed: trailing characters (byte 13) bug ### Your current environment ### 🐛 Describe the bug I keep having this decode error when using vllm=0.8.0 for qwen-2.5 inferen...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
