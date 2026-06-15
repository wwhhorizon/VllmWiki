# vllm-project/vllm#16397: [Feature]: co-exist of multiply kv connector

| 字段 | 值 |
| --- | --- |
| Issue | [#16397](https://github.com/vllm-project/vllm/issues/16397) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: co-exist of multiply kv connector

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Now, there are two kind of kv connector. 1. Offload kv cache to kv connector for reuse purpose 2. Transfer KVCache from P to D But we could only specific one kv connector, this make the two above kv connectors cannot co-exist, i propose to do an abstract or use a `type`, maybe {p2p, offload} to support to find the needed kv connector. In my view, the ideal way is 1. `P` check for partial cache hit and do prefill for the uncache hit part. 2. `P` transfer the minimal necessary kv cache(which mean Decode instance cannot obtain it from offload kv connector) 3. `D` receive KV cache from `offload connector` and `P` and update the kvcache 4. `D` execute the decode step by step until finish. 5. `D` save the kv cache into offload kv connector for reuse purpose 6. Goto 1. Any idea about this? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: co-exist of multiply kv connector feature request;stale ### 🚀 The feature, motivation and pitch Now, there are two kind of kv connector. 1. Offload kv cache to kv connector for reuse purpose 2. Transfer KVCac...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: re, motivation and pitch Now, there are two kind of kv connector. 1. Offload kv cache to kv connector for reuse purpose 2. Transfer KVCache from P to D But we could only specific one kv connector, this make the two abov...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ed kv connector. In my view, the ideal way is 1. `P` check for partial cache hit and do prefill for the uncache hit part. 2. `P` transfer the minimal necessary kv cache(which mean Decode instance cannot obtain it from o...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: for reuse purpose 2. Transfer KVCache from P to D But we could only specific one kv connector, this make the two above kv connectors cannot co-exist, i propose to do an abstract or use a `type`, maybe {p2p, offload} to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
