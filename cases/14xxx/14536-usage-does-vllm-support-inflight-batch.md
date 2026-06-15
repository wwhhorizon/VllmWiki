# vllm-project/vllm#14536: [Usage]: Does vllm support inflight batch?

| 字段 | 值 |
| --- | --- |
| Issue | [#14536](https://github.com/vllm-project/vllm/issues/14536) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Does vllm support inflight batch?

### Issue 正文摘录

### Your current environment ### How would you like to use vllm Does vllm support inflight batch? trtllm supports it but I can't find any information on vllm documentation Could some kind person explain it? Thank you so much in advance ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nce ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: s vllm support inflight batch? trtllm supports it but I can't find any information on vllm documentation Could some kind person explain it? Thank you so much in advance ### Before submitting a new issue... - [x] Make su...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
