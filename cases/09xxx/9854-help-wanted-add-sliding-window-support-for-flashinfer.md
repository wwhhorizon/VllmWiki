# vllm-project/vllm#9854: [help wanted]: add sliding window support for flashinfer 

| 字段 | 值 |
| --- | --- |
| Issue | [#9854](https://github.com/vllm-project/vllm/issues/9854) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [help wanted]: add sliding window support for flashinfer 

### Issue 正文摘录

### Anything you want to discuss about vllm. flashinfer already supports sliding window in https://github.com/flashinfer-ai/flashinfer/issues/159 , and we should update our code and pass sliding window to flashinfer , to remove this restriction: https://github.com/vllm-project/vllm/blob/5f8d8075f957d5376b2f1cc451e35a2a757e95a5/vllm/attention/backends/flashinfer.py#L739-L740 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [help wanted]: add sliding window support for flashinfer ### Anything you want to discuss about vllm. flashinfer already supports sliding window in https://github.com/flashinfer-ai/flashinfer/issues/159 , and we should...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 740 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
