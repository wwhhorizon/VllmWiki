# vllm-project/vllm#21014: [Feature]: Add Triton implementation of NVFP4 GEMM

| 字段 | 值 |
| --- | --- |
| Issue | [#21014](https://github.com/vllm-project/vllm/issues/21014) |
| 状态 | open |
| 标签 | good first issue;performance;feature request;unstale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add Triton implementation of NVFP4 GEMM

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently we only have NVFP4 GEMMs written in CUTLASS for SM100, which means we have no support for SM120. While we still expect tuned CUTLASS kernels to provide the best performance, it would be nice to have a reference Triton implementation available as a fallback if no other kernels are available. It seems Triton has supported FP4 formats for several months so we should have a new enough version of Triton https://github.com/triton-lang/triton/blob/620237edd282d3fa275e7f931af2018423108c4a/python/test/unit/language/test_matmul.py#L652 A good starting point would be to add the triton kernel directly to https://github.com/vllm-project/vllm/blob/main/benchmarks/kernels/bench_nvfp4_gemm.py and compare the performance to the CUTLASS kernel, before integrating with vLLM as a whole ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Feature]: Add Triton implementation of NVFP4 GEMM good first issue;performance;feature request;unstale ### 🚀 The feature, motivation and pitch Currently we only have NVFP4 GEMMs written in CUTLASS for SM100, which mean...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Feature]: Add Triton implementation of NVFP4 GEMM good first issue;performance;feature request;unstale ### 🚀 The feature, motivation and pitch Currently we only have NVFP4 GEMMs written in CUTLASS for SM100, which mean...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ion and pitch Currently we only have NVFP4 GEMMs written in CUTLASS for SM100, which means we have no support for SM120. While we still expect tuned CUTLASS kernels to provide the best performance, it would be nice to h...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Triton implementation of NVFP4 GEMM good first issue;performance;feature request;unstale ### 🚀 The feature, motivation and pitch Currently we only have NVFP4 GEMMs written in CUTLASS for SM100, which means we have no su...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: /triton-lang/triton/blob/620237edd282d3fa275e7f931af2018423108c4a/python/test/unit/language/test_matmul.py#L652 A good starting point would be to add the triton kernel directly to https://github.com/vllm-project/vllm/bl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
