# vllm-project/vllm#43763: [RFC]: Does SimpleCPUOffloadConnector have plans to support disk/ssd？

| 字段 | 值 |
| --- | --- |
| Issue | [#43763](https://github.com/vllm-project/vllm/issues/43763) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Does SimpleCPUOffloadConnector have plans to support disk/ssd？

### Issue 正文摘录

### Motivation. At present, the native OffloadingConnector already supports multi-level caching (disk, SSD) and cross instance kvcache offloading features. Does SimpleCPUOffloadConnector have plans to support multi-level caching and cross instance kvcache offloading? ### Proposed Change. Refer to: https://github.com/vllm-project/vllm/pull/37160 . SimpleCPUOffloadConnector seems to be designed only for offloading kvcache to CPU memory, and will not consider developing functions such as offloading kvcache to disk/ssd in the future. Is that correct? @ivanium ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [RFC]: Does SimpleCPUOffloadConnector have plans to support disk/ssd？ RFC ### Motivation. At present, the native OffloadingConnector already supports multi-level caching (disk, SSD) and cross instance kvcache offloading...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
