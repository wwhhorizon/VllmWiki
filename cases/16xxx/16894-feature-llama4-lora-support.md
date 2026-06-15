# vllm-project/vllm#16894: [Feature]: Llama4 LoRA support

| 字段 | 值 |
| --- | --- |
| Issue | [#16894](https://github.com/vllm-project/vllm/issues/16894) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Llama4 LoRA support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When serving Llama4 (eg scout, maverick), setting --enable-lora causes this Assertion error: AssertionError: Llama4ForConditionalGeneration does not support LoRA yet. I would like to make a request for support; or if there is a nightly release or some other place I can find this working, it would be greatly appreciated!! ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Llama4 LoRA support feature request;stale ### 🚀 The feature, motivation and pitch When serving Llama4 (eg scout, maverick), setting --enable-lora causes this Assertion error: AssertionError: Llama4ForConditio...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: se or some other place I can find this working, it would be greatly appreciated!! ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already sear...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Llama4 LoRA support feature request;stale ### 🚀 The feature, motivation and pitch When serving Llama4 (eg scout, maverick), setting --enable-lora causes this Assertion error: AssertionError: Llama4ForConditio...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
