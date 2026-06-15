# vllm-project/vllm#40592: [Performance]: DeepSeek-V3.2 performance on 8xH20 is not match with official data

| 字段 | 值 |
| --- | --- |
| Issue | [#40592](https://github.com/vllm-project/vllm/issues/40592) |
| 状态 | open |
| 标签 | performance |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: DeepSeek-V3.2 performance on 8xH20 is not match with official data

### Issue 正文摘录

### my env vllm0.19.1， Deep_gemm2.1.1+local，8xH20（96G） My device is 8xH20(96G), I use the scripts from https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-V3_2.html#benchmarking but it's can't running because of OOM. It's the official performance tested on 8xH200？https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-V3_2.html#tp8-benchmark-output

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: (96G), I use the scripts from https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-V3_2.html#benchmarking but it's can't running because of OOM. It's the official performance tested on 8xH200？https://docs.v...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Performance]: DeepSeek-V3.2 performance on 8xH20 is not match with official data performance ### my env vllm0.19.1， Deep_gemm2.1.1+local，8xH20（96G） My device is 8xH20(96G), I use the scripts from https://docs.vllm.ai/p...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: epSeek/DeepSeek-V3_2.html#benchmarking but it's can't running because of OOM. It's the official performance tested on 8xH200？https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-V3_2.html#tp8-benchmark-outp...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: is not match with official data performance ### my env vllm0.19.1， Deep_gemm2.1.1+local，8xH20（96G） My device is 8xH20(96G), I use the scripts from https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-V3_2.h...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
