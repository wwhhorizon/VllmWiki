# vllm-project/vllm#14463: [Bugfix]: Suggesting an update in the vllm source code to fix the error "Unable to assign 256 multimodal tokens to 0 placeholders"

| 字段 | 值 |
| --- | --- |
| Issue | [#14463](https://github.com/vllm-project/vllm/issues/14463) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bugfix]: Suggesting an update in the vllm source code to fix the error "Unable to assign 256 multimodal tokens to 0 placeholders"

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug To reproduce the bug, try running inference on a multimodal input in which the image has an aspect ratio close to 1 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: s" bug;stale ### Your current environment ### 🐛 Describe the bug To reproduce the bug, try running inference on a multimodal input in which the image has an aspect ratio close to 1 ### Before submitting a new issue... -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: o 1 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: an update in the vllm source code to fix the error "Unable to assign 256 multimodal tokens to 0 placeholders" bug;stale ### Your current environment ### 🐛 Describe the bug To reproduce the bug, try running inference on...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: the error "Unable to assign 256 multimodal tokens to 0 placeholders" bug;stale ### Your current environment ### 🐛 Describe the bug To reproduce the bug, try running inference on a multimodal input in which the image has...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
