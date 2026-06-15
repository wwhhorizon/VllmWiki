# vllm-project/vllm#23433: [Feature]: shared_experts overlap with DeepEP low latency dispatch

| 字段 | 值 |
| --- | --- |
| Issue | [#23433](https://github.com/vllm-project/vllm/issues/23433) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: shared_experts overlap with DeepEP low latency dispatch

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hello! I'm trying to work out a solution to overlap the execution of shared expert forward and DeepEP dispatch during decoding. The current implementation of fused MoE classes in vLLM has a few nested layers of abstraction. I'm considering two options to achieve this - ### Approach 1: Pass shared_experts torch module all the way down There are a couple of layers from the `DeepseekV2MoE` where `shared_experts` module is created, to `DeepEPLLPrepareAndFinalize` where DeepEP `low_latency_dispatch` is called. To overlap the two, we can pass the `shared_experts` module down: ``` layer.py::FusedMoE.process_chunk(..., self.shared_experts, ...) | fp8.py::Fp8MoEMethod.apply(..., self.shared_experts, ...) | fused_moe.py::fused_experts(..., self.shared_experts, ...) | deep_gemm_moe.py::deep_gemm_moe_fp8(..., self.shared_experts, ...) | modular_kernel.py::mk.FusedMoEModularKernel.forward(..., self.shared_experts, ...) ``` `FusedMoEModularKernel.forward` will take the dispatch receive hook and overlap the two. Downside: shared_experts will be a member of `FusedMoE` class because `FusedMoE.forward()` is registered as a custom op, and cannot take torch mod...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Feature]: shared_experts overlap with DeepEP low latency dispatch feature request;stale ### 🚀 The feature, motivation and pitch Hello! I'm trying to work out a solution to overlap the execution of shared expert forward...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: eature]: shared_experts overlap with DeepEP low latency dispatch feature request;stale ### 🚀 The feature, motivation and pitch Hello! I'm trying to work out a solution to overlap the execution of shared expert forward a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Feature]: shared_experts overlap with DeepEP low latency dispatch feature request;stale ### 🚀 The feature, motivation and pitch Hello! I'm trying to work out a solution to overlap the execution of shared expert forward...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: shared_experts overlap with DeepEP low latency dispatch feature request;stale ### 🚀 The feature, motivation and pitch Hello! I'm trying to work out a solution to overlap the execution of shared expert forward...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: edMoE.process_chunk(..., self.shared_experts, ...) | fp8.py::Fp8MoEMethod.apply(..., self.shared_experts, ...) | fused_moe.py::fused_experts(..., self.shared_experts, ...) | deep_gemm_moe.py::deep_gemm_moe_fp8(..., self...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
