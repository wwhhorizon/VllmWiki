# vllm-project/vllm#23205: [Feature]: Torch.compile support for `olmo2` models?

| 字段 | 值 |
| --- | --- |
| Issue | [#23205](https://github.com/vllm-project/vllm/issues/23205) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Torch.compile support for `olmo2` models?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently I'm using an `olmo-2` model with vllm on the v1 engine, and was curious why it doesn't seem to have `torch.compile` support: ``` [config.py:4846] `torch.compile` is turned on, but the model allenai/OLMo-2-1124-7B-Instruct does not support it. Please open an issue on GitHub if you want it to be supported. ``` Taking the trivial step of adding `@support_torch_compile` to [the model class](https://github.com/vllm-project/vllm/blob/80141bbf2f1b8b0beaac097f94923f95773734ef/vllm/model_executor/models/olmo2.py#L256) _seems_ to give a 20-30% speedup on the tasks I'm working with, but I feel like the devil is in the details and maybe this isn't as easy as I think? ### Alternatives _No response_ ### Additional context Currently benchmarking on an L40 instance ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Torch.compile support for `olmo2` models? feature request ### 🚀 The feature, motivation and pitch Currently I'm using an `olmo-2` model with vllm on the v1 engine, and was curious why it doesn't seem to have...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ink? ### Alternatives _No response_ ### Additional context Currently benchmarking on an L40 instance ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot l...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: Torch.compile support for `olmo2` models? feature request ### 🚀 The feature, motivation and pitch Currently I'm using an `olmo-2` model with vllm on the v1 engine, and was curious why it doesn't seem to have...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nce ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Torch.compile support for `olmo2` models? feature request ### 🚀 The feature, motivation and pitch Currently I'm using an `olmo-2` model with vllm on the v1 engine, and was curious why it doesn't seem to have...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
