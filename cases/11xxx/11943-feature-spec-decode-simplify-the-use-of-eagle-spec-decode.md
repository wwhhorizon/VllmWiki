# vllm-project/vllm#11943: [Feature] [Spec Decode]: Simplify the Use of Eagle Spec Decode

| 字段 | 值 |
| --- | --- |
| Issue | [#11943](https://github.com/vllm-project/vllm/issues/11943) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature] [Spec Decode]: Simplify the Use of Eagle Spec Decode

### Issue 正文摘录

### 🚀 The feature, motivation and pitch As documented [here](https://docs.vllm.ai/en/latest/features/spec_decode.html#speculating-using-eagle-based-draft-models), currently, users need to change the config and checkpoint using the [script](https://gist.github.com/abhigoyal1997/1e7a4109ccb7704fbc67f625e86b2d6d), which is tedious. In the ideal case, vllm should load the eagle head automatically from huggingface or locally without extra conversion. This can be achieved by: 1. Identify this is a eagle head from the model name. 2. Identify the LM head from the original base model. After 1 and 2, vllm should be able to use eagle speculative decoding without user conversion. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Feature] [Spec Decode]: Simplify the Use of Eagle Spec Decode feature request;stale ### 🚀 The feature, motivation and pitch As documented [here](https://docs.vllm.ai/en/latest/features/spec_decode.html#speculating-usin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: /en/latest/features/spec_decode.html#speculating-using-eagle-based-draft-models), currently, users need to change the config and checkpoint using the [script](https://gist.github.com/abhigoyal1997/1e7a4109ccb7704fbc67f6...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: he eagle head automatically from huggingface or locally without extra conversion. This can be achieved by: 1. Identify this is a eagle head from the model name. 2. Identify the LM head from the original base model. Afte...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: re, motivation and pitch As documented [here](https://docs.vllm.ai/en/latest/features/spec_decode.html#speculating-using-eagle-based-draft-models), currently, users need to change the config and checkpoint using the [sc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
