# vllm-project/vllm#16037: [RFC]: Data Parallel Attention and Expert Parallel MoEs

| 字段 | 值 |
| --- | --- |
| Issue | [#16037](https://github.com/vllm-project/vllm/issues/16037) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe |
| 子分类 | throughput |
| Operator 关键词 | attention;cache;cuda;gemm;kernel;moe;operator |
| 症状 | slowdown |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [RFC]: Data Parallel Attention and Expert Parallel MoEs

### Issue 正文摘录

### Motivation. This RFC tracks both DP and EP together, since these is a strong intersection between these features. A key motivation for DP attention is reduced memory footprint in MLA models like DeepSeek V2, V3, and R1. If Tensor Parallelism is used in an MLA model, we duplicate the KV cache across GPUs, wasting memory. This reduces our batch size for throughput and high-QPS serving use cases, which kills our performance. To solve this, we need to parallelize attention across GPUs differently. In this RFC we are talking about _request-level parallelism_ for this. EP is Expert Parallelism for MoEs, where experts are distributed across EP ranks, and tokens are dispatched to the GPUs holding the experts that the token is routed to. This is in contrast to Tensor Parallel, which shards each expert. The main advantage is lower data movement, especially for large numbers of GPUs, where each token only needs to be sent to a subset of EP ranks. This also can be helpful so that the underlying grouped GEMM kernels operate on tensors with a better aspect ratio. ### Proposed Change. [DP attention design doc](https://docs.google.com/document/d/1I5gmPFdjOvsvgNSvTAuA_h0x7zn3M-5v5AWGLev9M9I/ed...

## 现有链接修复摘要

#19885 [EP+DP] Optimize the little operations in the DeepGEMM + DeepEP low latency case

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: [RFC]: Data Parallel Attention and Expert Parallel MoEs RFC ### Motivation. This RFC tracks both DP and EP together, since these is a strong intersection between these features. A key motivation for DP attention is redu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: footprint in MLA models like DeepSeek V2, V3, and R1. If Tensor Parallelism is used in an MLA model, we duplicate the KV cache across GPUs, wasting memory. This reduces our batch size for throughput and high-QPS serving...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: which shards each expert. The main advantage is lower data movement, especially for large numbers of GPUs, where each token only needs to be sent to a subset of EP ranks. This also can be helpful so that the underlying...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ize attention across GPUs differently. In this RFC we are talking about _request-level parallelism_ for this. EP is Expert Parallelism for MoEs, where experts are distributed across EP ranks, and tokens are dispatched t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: he KV cache across GPUs, wasting memory. This reduces our batch size for throughput and high-QPS serving use cases, which kills our performance. To solve this, we need to parallelize attention across GPUs differently. I...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#19885](https://github.com/vllm-project/vllm/pull/19885) | mentioned | 0.45 | [EP+DP] Optimize the little operations in the DeepGEMM + DeepEP low latency case | pep prefill case - [x] optimizations for deepep+deepgemm - [x] #19885 - [x] https://github.com/vllm-project/vllm/pull/21311 - [x] https://github.com/vllm-project/vllm/pull |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
