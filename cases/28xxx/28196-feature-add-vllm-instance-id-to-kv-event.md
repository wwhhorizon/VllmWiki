# vllm-project/vllm#28196: [Feature]: Add VLLM_INSTANCE_ID to KV Event

| 字段 | 值 |
| --- | --- |
| Issue | [#28196](https://github.com/vllm-project/vllm/issues/28196) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add VLLM_INSTANCE_ID to KV Event

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I need to subscribe to KV events from multiple vllm instances, the recommended way to do is subscribing all the publishers by one single ZMQ SUB socket, however, there is no ZMQ official way to identify the publisher from the received message, the recommended way to do it is adding publisher's identifier in the message. The current KVCacheEvent and KVEventBatch messages contain no vllm instance identifer, so it is impossible to distinguish the vllm instance. ### Alternatives I suggest to add one attribute in KVEventBatch with the value of the envirnoment variable VLLM_INSTANCE_ID ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add VLLM_INSTANCE_ID to KV Event feature request;stale ### 🚀 The feature, motivation and pitch I need to subscribe to KV events from multiple vllm instances, the recommended way to do is subscribing all the p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: he publishers by one single ZMQ SUB socket, however, there is no ZMQ official way to identify the publisher from the received message, the recommended way to do it is adding publisher's identifier in the message. The cu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
