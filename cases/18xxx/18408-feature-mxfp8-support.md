# vllm-project/vllm#18408: [Feature]: MXFP8 support

| 字段 | 值 |
| --- | --- |
| Issue | [#18408](https://github.com/vllm-project/vllm/issues/18408) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: MXFP8 support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch New accelerators such as Nvidia's Blackwell support the microscaling formats MXFP{8,6,4}. This is a finer-grained scheme than existing block-wise scaling implementations such as the single fp32 scale per 128 x 128 block used by e.g. DeepSeek, whereas MXFP8 for example uses an e8m0 scale per 32 elements of a tensor. Here's the OCP spec: https://www.opencompute.org/documents/ocp-microscaling-formats-mx-v1-0-spec-final-pdf and PTX docs: https://docs.nvidia.com/cuda/parallel-thread-execution/#warp-level-block-scaling I think vLLM could relatively easily support these formats, both for sm100 (e.g. B200) and sm120 (e.g. 5090). Cutlass has example kernels for both architectures: - https://github.com/NVIDIA/cutlass/tree/main/examples/72_blackwell_narrow_precision_gemm - https://github.com/NVIDIA/cutlass/tree/main/examples/79_blackwell_geforce_gemm I would be interested in contributing, but I would need some help and feedback on a design of the implementation. There is likely also some work to be done outside of vLLM, since e.g. `safetensors` would have to support the format (might exist through `compressed-tensors`?) ### Alternatives _No response_ #...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: # 🚀 The feature, motivation and pitch New accelerators such as Nvidia's Blackwell support the microscaling formats MXFP{8,6,4}. This is a finer-grained scheme than existing block-wise scaling implementations such as the...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Feature]: MXFP8 support feature request;stale ### 🚀 The feature, motivation and pitch New accelerators such as Nvidia's Blackwell support the microscaling formats MXFP{8,6,4}. This is a finer-grained scheme than existi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: MXFP8 support feature request;stale ### 🚀 The feature, motivation and pitch New accelerators such as Nvidia's Blackwell support the microscaling formats MXFP{8,6,4}. This is a finer-grained scheme than existi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: support these formats, both for sm100 (e.g. B200) and sm120 (e.g. 5090). Cutlass has example kernels for both architectures: - https://github.com/NVIDIA/cutlass/tree/main/examples/72_blackwell_narrow_precision_gemm - ht...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: https://github.com/NVIDIA/cutlass/tree/main/examples/72_blackwell_narrow_precision_gemm - https://github.com/NVIDIA/cutlass/tree/main/examples/79_blackwell_geforce_gemm I would be interested in contributing, but I would...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
