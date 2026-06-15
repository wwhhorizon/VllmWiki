# vllm-project/vllm#32631: [Tracker]: Initialize MM components in context managers

| 字段 | 值 |
| --- | --- |
| Issue | [#32631](https://github.com/vllm-project/vllm/issues/32631) |
| 状态 | closed |
| 标签 | multi-modality |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Tracker]: Initialize MM components in context managers

### Issue 正文摘录

### Purpose Apply #32605 to all applicable models to enable encoder-only and LM-only mode.. - [x] #32632 - [x] #32641 - [x] #32650 - [x] #32663 - [x] #32695 - [x] #32691 - [x] #32757 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 757 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: text managers multi-modality ### Purpose Apply #32605 to all applicable models to enable encoder-only and LM-only mode.. - [x] #32632 - [x] #32641 - [x] #32650 - [x] #32663 - [x] #32695 - [x] #32691 - [x] #32757 ### Bef...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
