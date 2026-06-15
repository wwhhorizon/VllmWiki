# vllm-project/vllm#19137: [Bug]: Error occurred while performing model inference using 0.8 H20s from the virtualized computing pool.

| 字段 | 值 |
| --- | --- |
| Issue | [#19137](https://github.com/vllm-project/vllm/issues/19137) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Error occurred while performing model inference using 0.8 H20s from the virtualized computing pool.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug After GPU virtualization, using VLLM inference large models results in computational graph errors. adding --enforce-eager during inference, the following error occurs: Engine core initialization failed. See root cause above. Failed core proc(s):{} ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: :{} ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Error occurred while performing model inference using 0.8 H20s from the virtualized computing pool. bug;stale ### Your current environment ### 🐛 Describe the bug After GPU virtualization, using VLLM inference lar...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: model inference using 0.8 H20s from the virtualized computing pool. bug;stale ### Your current environment ### 🐛 Describe the bug After GPU virtualization, using VLLM inference large models results in computational grap...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
