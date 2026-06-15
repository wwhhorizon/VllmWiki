# vllm-project/vllm#13900: [Misc]: is paged attention an exact attention

| 字段 | 值 |
| --- | --- |
| Issue | [#13900](https://github.com/vllm-project/vllm/issues/13900) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: is paged attention an exact attention

### Issue 正文摘录

### Anything you want to discuss about vllm. For the blockwise computation of paged attention as in the above equation, it is not an exact attention. In an exact attention, all the attention scores sum up to 1. Here the attention scores in each block sum up to 1. So is it correct to say that paged attention is not an exact attention? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: exact attention ### Anything you want to discuss about vllm. For the blockwise computation of paged attention as in the above equation, it is not an exact attention. In an exact attention, all the attention scores sum u...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
