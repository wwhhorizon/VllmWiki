# vllm-project/vllm#42051: [Feature]: Output prompt text when enable `--enable-log-requests`

| 字段 | 值 |
| --- | --- |
| Issue | [#42051](https://github.com/vllm-project/vllm/issues/42051) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Output prompt text when enable `--enable-log-requests`

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Now, when we use sglang, it will get the prompt text after chat template processed: But vLLM can only output prompt token id with `--enable-log-requests`, This feature is so import when we trying to debug our model: ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: output prompt token id with `--enable-log-requests`, This feature is so import when we trying to debug our model: ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue......
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ble-log-requests`, This feature is so import when we trying to debug our model: ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already search...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Output prompt text when enable `--enable-log-requests` feature request ### 🚀 The feature, motivation and pitch Now, when we use sglang, it will get the prompt text after chat template processed: But vLLM can...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
