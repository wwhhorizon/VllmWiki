# vllm-project/vllm#25059: [Bug]: default nixl side channel port conflicts with kv-event zmq port

| 字段 | 值 |
| --- | --- |
| Issue | [#25059](https://github.com/vllm-project/vllm/issues/25059) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: default nixl side channel port conflicts with kv-event zmq port

### Issue 正文摘录

### Your current environment main branch ### 🐛 Describe the bug vLLM provides ports for kv-event zmq subscriber, default starts from 5557, with lots of code/example/tests https://github.com/vllm-project/vllm/blob/main/vllm/distributed/kv_events.py#L139 https://github.com/vllm-project/vllm/blob/main/examples/online_serving/kv_events_subscriber.py#L62 https://github.com/vllm-project/vllm/blob/main/tests/distributed/test_events.py#L212 so here `VLLM_NIXL_SIDE_CHANNEL_PORT` default value as 5557 should be an obvious conflict. taken there will be TP/DP and 5557 will increase , so use a safer range starting from 5600 for VLLM_NIXL_SIDE_CHANNEL_PORT ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ORT ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: vent zmq subscriber, default starts from 5557, with lots of code/example/tests https://github.com/vllm-project/vllm/blob/main/vllm/distributed/kv_events.py#L139 https://github.com/vllm-project/vllm/blob/main/examples/on...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
