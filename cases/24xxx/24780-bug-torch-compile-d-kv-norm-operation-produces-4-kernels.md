# vllm-project/vllm#24780: [Bug]: torch.compile'd kv norm operation produces 4 kernels

| 字段 | 值 |
| --- | --- |
| Issue | [#24780](https://github.com/vllm-project/vllm/issues/24780) |
| 状态 | closed |
| 标签 | bug;torch.compile;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: torch.compile'd kv norm operation produces 4 kernels

### Issue 正文摘录

### Your current environment n/a ### 🐛 Describe the bug Originally reported by @WoosukKwon. https://github.com/vllm-project/vllm/blob/010acc6e1ea1d59ef530459e1078e8fde80f2082/vllm/model_executor/models/qwen3.py#L137-L157 Profiling Qwen3-0.6B ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: com/vllm-project/vllm/blob/010acc6e1ea1d59ef530459e1078e8fde80f2082/vllm/model_executor/models/qwen3.py#L137-L157 Profiling Qwen3-0.6B ### Before submitting a new issue... - [x] Make sure you already searched for releva...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ef530459e1078e8fde80f2082/vllm/model_executor/models/qwen3.py#L137-L157 Profiling Qwen3-0.6B ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: torch.compile'd kv norm operation produces 4 kernels bug;torch.compile;stale ### Your current environment n/a ### 🐛 Describe the bug Originally reported by @WoosukKwon. https://github.com/vllm-project/vllm/blob/0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .6B ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: : torch.compile'd kv norm operation produces 4 kernels bug;torch.compile;stale ### Your current environment n/a ### 🐛 Describe the bug Originally reported by @WoosukKwon. https://github.com/vllm-project/vllm/blob/010acc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
