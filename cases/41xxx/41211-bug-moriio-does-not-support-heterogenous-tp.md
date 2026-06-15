# vllm-project/vllm#41211: [Bug]: MoRIIO does not support heterogenous TP

| 字段 | 值 |
| --- | --- |
| Issue | [#41211](https://github.com/vllm-project/vllm/issues/41211) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: MoRIIO does not support heterogenous TP

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The MoRI-IO connector currently notifies remote ranks by iterating over its _local tp size_, not the remote tp size. This means if TP of the D instance != TP of the P instance, some ranks might not get notified or some notifications might go to ports that are not listened to (depending on READ or WRITE mode). Since the connectors already sends their TP sizes in the registration messages we just have to 1. update vllm-router to store this TP size for each instance in its service registry, and pass it along in the kv_transfer_params 2. update the connector to iterate over the remote TP size rather than the local tp size when sending notifications ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ns ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: eir TP sizes in the registration messages we just have to 1. update vllm-router to store this TP size for each instance in its service registry, and pass it along in the kv_transfer_params 2. update the connector to ite...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
