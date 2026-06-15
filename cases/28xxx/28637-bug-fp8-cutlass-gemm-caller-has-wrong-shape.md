# vllm-project/vllm#28637: [Bug]: fp8 cutlass_gemm_caller has wrong shape

| 字段 | 值 |
| --- | --- |
| Issue | [#28637](https://github.com/vllm-project/vllm/issues/28637) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: fp8 cutlass_gemm_caller has wrong shape

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug in csrc/quantization/w8a8/cutlass/c3x/scaled_mm_blockwise_sm120_fp8_dispatch.cuh, line 130: int32_t m = a.size(0), n = b.size(1), k = a.size(1); b is not [k,n], b is expected to be [n,k] in the other part in this file. So when I run with this code, it generates nan. I replaced it with n = b.size(0),then everything goes well. Hope you can repair it. Thank you. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: fp8 cutlass_gemm_caller has wrong shape bug ### Your current environment ### 🐛 Describe the bug in csrc/quantization/w8a8/cutlass/c3x/scaled_mm_blockwise_sm120_fp8_dispatch.cuh, line 130: int32_t m = a.size(0), n...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: fp8 cutlass_gemm_caller has wrong shape bug ### Your current environment ### 🐛 Describe the bug in csrc/quantization/w8a8/cutlass/c3x/scaled_mm_blockwise_sm120_fp8_dispatch.cuh, line 130: int32_t m = a.size(0), n...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: cribe the bug in csrc/quantization/w8a8/cutlass/c3x/scaled_mm_blockwise_sm120_fp8_dispatch.cuh, line 130: int32_t m = a.size(0), n = b.size(1), k = a.size(1); b is not [k,n], b is expected to be [n,k] in the other part...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ### 🐛 Describe the bug in csrc/quantization/w8a8/cutlass/c3x/scaled_mm_blockwise_sm120_fp8_dispatch.cuh, line 130: int32_t m = a.size(0), n = b.size(1), k = a.size(1); b is not [k,n], b is expected to be [n,k] in the ot...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: fp8 cutlass_gemm_caller has wrong shape bug ### Your current environment ### 🐛 Describe the bug in csrc/quantization/w8a8/cutlass/c3x/scaled_mm_blockwise_sm120_fp8_dispatch.cuh, line 130: int32_t m = a.size(0), n...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
