# vllm-project/vllm#26264: [Bug]: KV events subscriber expecting `BlockHash` but receives `ExternalBlockHash`

| 字段 | 值 |
| --- | --- |
| Issue | [#26264](https://github.com/vllm-project/vllm/issues/26264) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: KV events subscriber expecting `BlockHash` but receives `ExternalBlockHash`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug KV events subscriber expecting `BlockHash` but receives `ExternalBlockHash` The current kv_event_subscriber.py [https://github.com/vllm-project/vllm/blob/main/examples/online_serving/kv_events_subscriber.py](url) is listening to KV block events as ExternalBlockHash, but the current implementation assumes it to be of the latter type, hence causing this error. Current BlockHash used references `byte type`, and this causes a decoding error. ``` from vllm.v1.core.kv_cache_utils import BlockHash ``` I did explore the codebase for changes that would lead to the optimal and feasible solution. I believe changing the current subscriber to `ExternalBlockHash` seems like a well-lit path, considering that it would be backward compatible with the previous type. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: , and this causes a decoding error. ``` from vllm.v1.core.kv_cache_utils import BlockHash ``` I did explore the codebase for changes that would lead to the optimal and feasible solution. I believe changing the current s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: KV events subscriber expecting `BlockHash` but receives `ExternalBlockHash` bug ### Your current environment ### 🐛 Describe the bug KV events subscriber expecting `BlockHash` but receives `ExternalBlockHash` The...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
