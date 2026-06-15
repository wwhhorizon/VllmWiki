# vllm-project/vllm#6378: [RFC]: A Graph Optimization System in vLLM using torch.compile

| 字段 | 值 |
| --- | --- |
| Issue | [#6378](https://github.com/vllm-project/vllm/issues/6378) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: A Graph Optimization System in vLLM using torch.compile

### Issue 正文摘录

### Motivation. At a high level, we at Neural Magic are writing a custom compiler for Torch Dynamo to define a system within vLLM where we can write graph transformations. The main goal is a separation of concerns between high-level model definitions and certain performance-critical low-level decisions. This is especially important for optimizations that are particularly invasive to the model definitions, that break abstractions, that cross boundaries between layers, or that aren't universally valid or useful. If these optimizations are made as part of the model definitions, it becomes much more difficult to add new models. We are working on the following for an initial set of optimizations using this system, described in detail in the Proposed Passes section. * Fusing quantize operations onto LayerNorm kernels (both for fp8 and int8 and both static and dynamic quantization) * Fusing the MLP section containing GEMM, SiLU, Mul, and quantize operations * Rewriting Gemm + AllReduce + Layer Norm + Gemm to a Fused Gemm-ReduceScatter + LayerNorm + Fused AllGather Gemm, in order to take advantage of the Flux kernels from ByteDance Although this system operates as a custom compiler inside...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [RFC]: A Graph Optimization System in vLLM using torch.compile RFC;stale ### Motivation. At a high level, we at Neural Magic are writing a custom compiler for Torch Dynamo to define a system within vLLM where we can wri...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: his system, described in detail in the Proposed Passes section. * Fusing quantize operations onto LayerNorm kernels (both for fp8 and int8 and both static and dynamic quantization) * Fusing the MLP section containing GE...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: orch Dynamo to define a system within vLLM where we can write graph transformations. The main goal is a separation of concerns between high-level model definitions and certain performance-critical low-level decisions. T...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: oth static and dynamic quantization) * Fusing the MLP section containing GEMM, SiLU, Mul, and quantize operations * Rewriting Gemm + AllReduce + Layer Norm + Gemm to a Fused Gemm-ReduceScatter + LayerNorm + Fused AllGat...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [RFC]: A Graph Optimization System in vLLM using torch.compile RFC;stale ### Motivation. At a high level, we at Neural Magic are writing a custom compiler for Torch Dynamo to define a system within vLLM where we can wri...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
