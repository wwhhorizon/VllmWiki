# vllm-project/vllm#34054: [Bug]: pd disaggregation on the same host with nixl connector can not use nvlink to transfer kv cache

| 字段 | 值 |
| --- | --- |
| Issue | [#34054](https://github.com/vllm-project/vllm/issues/34054) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: pd disaggregation on the same host with nixl connector can not use nvlink to transfer kv cache

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug refer to https://docs.vllm.ai/en/latest/features/nixl_connector_usage/#basic-usage-on-the-same-host , set up 1p1d on one host, but did not use nvlink to transfer kvcache, leads to additional time cost. ``` KV Transfer metrics: Num successful transfers=80, Avg xfer time (ms)=173.794, P90 xfer time (ms)=235.706, Avg post time (ms)=129.127, P90 post time (ms)=131.126, Avg MB per transfer=313.0, Throughput (MB/s)=1800.983, Avg number of descriptors=40064.0 ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: vironment ### 🐛 Describe the bug refer to https://docs.vllm.ai/en/latest/features/nixl_connector_usage/#basic-usage-on-the-same-host , set up 1p1d on one host, but did not use nvlink to transfer kvcache, leads to additi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: g]: pd disaggregation on the same host with nixl connector can not use nvlink to transfer kv cache bug ### Your current environment ### 🐛 Describe the bug refer to https://docs.vllm.ai/en/latest/features/nixl_connector_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: tion on the same host with nixl connector can not use nvlink to transfer kv cache bug ### Your current environment ### 🐛 Describe the bug refer to https://docs.vllm.ai/en/latest/features/nixl_connector_usage/#basic-usag...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
