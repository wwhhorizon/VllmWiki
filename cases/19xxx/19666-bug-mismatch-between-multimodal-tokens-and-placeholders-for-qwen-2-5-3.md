# vllm-project/vllm#19666: [Bug]: mismatch between multimodal tokens and placeholders for Qwen_2.5-3B (4 GPUs*24G)

| 字段 | 值 |
| --- | --- |
| Issue | [#19666](https://github.com/vllm-project/vllm/issues/19666) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: mismatch between multimodal tokens and placeholders for Qwen_2.5-3B (4 GPUs*24G)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running the Seg - Zero project with 4×24G GPUs, we encountered the aforementioned problem. We have already tried the method mentioned in #8421, yet it still doesn’t work. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: mismatch between multimodal tokens and placeholders for Qwen_2.5-3B (4 GPUs*24G) bug;stale ### Your current environment ### 🐛 Describe the bug When running the Seg - Zero project with 4×24G GPUs, we encountered t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: mismatch between multimodal tokens and placeholders for Qwen_2.5-3B (4 GPUs*24G) bug;stale ### Your current environment ### 🐛 Describe the bug When running the Seg - Zero project with 4×24G GPUs, we encountered t...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: mismatch between multimodal tokens and placeholders for Qwen_2.5-3B (4 GPUs*24G) bug;stale ### Your current environment ### 🐛 Describe the bug When running the Seg - Zero project with 4×24G GPUs, we encountered t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ween multimodal tokens and placeholders for Qwen_2.5-3B (4 GPUs*24G) bug;stale ### Your current environment ### 🐛 Describe the bug When running the Seg - Zero project with 4×24G GPUs, we encountered the aforementioned p...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
