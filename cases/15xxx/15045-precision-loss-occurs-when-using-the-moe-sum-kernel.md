# vllm-project/vllm#15045: Precision loss occurs when using the MoE sum kernel.

| 字段 | 值 |
| --- | --- |
| Issue | [#15045](https://github.com/vllm-project/vllm/issues/15045) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Precision loss occurs when using the MoE sum kernel.

### Issue 正文摘录

### Your current environment I'm seeing significant precision loss for bfloat16 when topk is 8. ### 🐛 Describe the bug ```C template __global__ void moe_sum_kernel( scalar_t* __restrict__ out, // [..., d] const scalar_t* __restrict__ input, // [..., topk, d] const int d) { const int64_t token_idx = blockIdx.x; for (int64_t idx = threadIdx.x; idx < d; idx += blockDim.x) { scalar_t x = 0.0; #pragma unroll for (int k = 0; k < TOPK; ++k) { x += VLLM_LDG(&input[token_idx * TOPK * d + k * d + idx]); } out[token_idx * d + idx] = x; } } ``` ### Before submitting a new issue... - [ ] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ### Your current environment I'm seeing significant precision loss for bfloat16 when topk is 8. ### 🐛 Describe the bug ```C template __global__ void moe_sum_kernel( scalar_t* __restrict__ out, // [..., d] const scalar_t...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: Precision loss occurs when using the MoE sum kernel. bug;stale ### Your current environment I'm seeing significant precision loss for bfloat16 when topk is 8. ### 🐛 Describe the bug ```C template __global__ void moe_sum...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: Precision loss occurs when using the MoE sum kernel. bug;stale ### Your current environment I'm seeing significant precision loss for bfloat16 when topk is 8. ### 🐛 Describe the bug ```C template __global__ void moe
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Precision loss occurs when using the MoE sum kernel. bug;stale ### Your current environment I'm seeing significant precision loss for bfloat16 when topk is 8. ### 🐛 Describe the bug ```C template __global__ void moe_su
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [ ] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
