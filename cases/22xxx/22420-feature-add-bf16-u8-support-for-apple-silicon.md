# vllm-project/vllm#22420: [Feature]: Add BF16/U8 support for Apple silicon.

| 字段 | 值 |
| --- | --- |
| Issue | [#22420](https://github.com/vllm-project/vllm/issues/22420) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add BF16/U8 support for Apple silicon.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently “the CPU implementation for macOS supports FP32 and FP16 datatypes.” For GPT-OSS to run, if BF16 or U8 was supported, that would be great! ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add BF16/U8 support for Apple silicon. feature request;stale ### 🚀 The feature, motivation and pitch Currently “the CPU implementation for macOS supports FP32 and FP16 datatypes.” For GPT-OSS to run, if BF16...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature]: Add BF16/U8 support for Apple silicon. feature request;stale ### 🚀 The feature, motivation and pitch Currently “the CPU implementation for macOS supports FP32 and FP16 datatypes.” For GPT-OSS to run, if BF16...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: “the CPU implementation for macOS supports FP32 and FP16 datatypes.” For GPT-OSS to run, if BF16 or U8 was supported, that would be great! ### Alternatives _No response_ ### Additional context _No response_ ### Before s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
