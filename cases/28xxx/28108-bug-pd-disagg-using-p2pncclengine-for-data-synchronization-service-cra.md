# vllm-project/vllm#28108: [Bug]: PD disagg, using P2pNcclEngine for data synchronization, service crashes

| 字段 | 值 |
| --- | --- |
| Issue | [#28108](https://github.com/vllm-project/vllm/issues/28108) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: PD disagg, using P2pNcclEngine for data synchronization, service crashes

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Steps to reproduce the bug： 1、start the P and D nodes using GET mode. 2、The call request instructs the PD node to establish nccl communication. 3、 restart P node 4、The service freezes when the request is made again. note：If it's in PUT mode, restarting node D will also reproduce the problem. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: isagg, using P2pNcclEngine for data synchronization, service crashes bug;stale ### Your current environment ### 🐛 Describe the bug Steps to reproduce the bug： 1、start the P and D nodes using GET mode. 2、The call request...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ;stale ### Your current environment ### 🐛 Describe the bug Steps to reproduce the bug： 1、start the P and D nodes using GET mode. 2、The call request instructs the PD node to establish nccl communication. 3、 restart P nod...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: em. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
