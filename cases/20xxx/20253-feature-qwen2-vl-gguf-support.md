# vllm-project/vllm#20253: [Feature]: Qwen2-VL GGUF support

| 字段 | 值 |
| --- | --- |
| Issue | [#20253](https://github.com/vllm-project/vllm/issues/20253) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Qwen2-VL GGUF support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hello! Can you implement Qwen2-VL GGUF support? `Value error, GGUF model with architecture qwen2vl is not supported yet. [type=value_error, input_value=ArgsKwargs((), {'model': ..., 'model_impl': 'auto'}), input_type=ArgsKwargs]` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Qwen2-VL GGUF support feature request;stale ### 🚀 The feature, motivation and pitch Hello! Can you implement Qwen2-VL GGUF support? `Value error, GGUF model with architecture qwen2vl is not supported yet. [ty...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Qwen2-VL GGUF support feature request;stale ### 🚀 The feature, motivation and pitch Hello! Can you implement Qwen2-VL GGUF support? `Value error, GGUF model with architecture qwen2vl is not supported yet. [ty...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Can you implement Qwen2-VL GGUF support? `Value error, GGUF model with architecture qwen2vl is not supported yet. [type=value_error, input_value=ArgsKwargs((), {'model': ..., 'model_impl': 'auto'}), input_type=ArgsKwarg...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
