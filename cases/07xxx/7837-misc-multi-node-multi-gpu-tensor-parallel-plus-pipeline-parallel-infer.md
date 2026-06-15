# vllm-project/vllm#7837: [Misc]: Multi-Node Multi-GPU (tensor parallel plus pipeline parallel inference)

| 字段 | 值 |
| --- | --- |
| Issue | [#7837](https://github.com/vllm-project/vllm/issues/7837) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Multi-Node Multi-GPU (tensor parallel plus pipeline parallel inference)

### Issue 正文摘录

### Anything you want to discuss about vllm. I have 2 nodes and each of them has 2 v100. According to the guide, i can use tensor parallel in each node and crossing the 2 nodes i can use pipline parallel. My question is which card or cards will communicate with the other card or cards in the other node. Thanks ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nks ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
