# vllm-project/vllm#26187: [Feature][UX]: Wide EP Engine Compatibility

| 字段 | 值 |
| --- | --- |
| Issue | [#26187](https://github.com/vllm-project/vllm/issues/26187) |
| 状态 | closed |
| 标签 | help wanted;good first issue;feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][UX]: Wide EP Engine Compatibility

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I was recently debugging an hang in vllm. It turns out that the root cause was that the leader rank enabled `--enable-eplb-log-balancedness` and the workers did not. This manifested as a hang in vLLM, because only the head worker was doing an AR call. We should not allow vLLM to startup if the Workers are not all compatible in DP mode. ### Alternatives _No response_ ### Additional context We should fix this in the handshake with the DP Coordinator at startup ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: tup ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ][UX]: Wide EP Engine Compatibility help wanted;good first issue;feature request ### 🚀 The feature, motivation and pitch I was recently debugging an hang in vllm. It turns out that the root cause was that the leader ran...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
