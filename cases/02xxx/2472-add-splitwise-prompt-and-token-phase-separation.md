# vllm-project/vllm#2472: Add Splitwise: prompt and token phase separation

| 字段 | 值 |
| --- | --- |
| Issue | [#2472](https://github.com/vllm-project/vllm/issues/2472) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Add Splitwise: prompt and token phase separation

### Issue 正文摘录

We have built the system described in [http://aka.ms/splitwise](http://aka.ms/splitwise) Splitwise splits the prompt and token phases to run in different servers. This leverages the differences between these two phases to improve throughput. We have an internal prototype on top of an internal vLLM branch. This issue tracks the effort to open source this prototype and make it part of the official vLLM. This includes: * Add MSCCL++ support [https://github.com/microsoft/mscclpp](https://github.com/microsoft/mscclpp) * Add per-layer KV-cache transfer * Coordination across prompt and token servers * Documentation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: cks the effort to open source this prototype and make it part of the official vLLM. This includes: * Add MSCCL++ support [https://github.com/microsoft/mscclpp](https://github.com/microsoft/mscclpp) * Add per-layer KV-ca...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: microsoft/mscclpp](https://github.com/microsoft/mscclpp) * Add per-layer KV-cache transfer * Coordination across prompt and token servers * Documentation
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: vers. This leverages the differences between these two phases to improve throughput. We have an internal prototype on top of an internal vLLM branch. This issue tracks the effort to open source this prototype and make i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
