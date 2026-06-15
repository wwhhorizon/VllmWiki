# vllm-project/vllm#24629: [torch.compile][Performance]: Unwrap custom ops and improve fusion (Inductor and custom)

| 字段 | 值 |
| --- | --- |
| Issue | [#24629](https://github.com/vllm-project/vllm/issues/24629) |
| 状态 | open |
| 标签 | help wanted;performance;torch.compile |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [torch.compile][Performance]: Unwrap custom ops and improve fusion (Inductor and custom)

### Issue 正文摘录

# Proposal to improve performance This issue tracks work on unwrapping custom ops and enabling additional fusions inside the model forward pass. ## Motivation While profiling Deepseek, GPT-OSS, and LLaMa (in-progress), we noticed a lot of overhead from elementwise & unfused ops. In most cases, those ops could be fused or eliminated by torch.compile but they happen inside a custom-op, hidden from torch.compile. There are some fusion opportunities across a current custom op boundary and some under-utilized fusion opportunities completely unrelated to custom ops. ### Example trace (Deepseek): How to read this trace: - `nvjet_...` are unquantized `torch.mm` calls - `native::elementwise` are elementwise ops not visible to `torch.compile` - `triton_red_fused_...` are (fused) elementwise ops visible to `torch.compile` and lowered into fused Triton kernels - all other kernels are custom kernels (attn, GEMM, MoE, allreduce, quant, etc.) The fusion opportunities are below: ### Action items - RMSNorm + quant (fusions 1 & 2): 1. Unwrap `apply_w8a8_block_fp8_linear` 2. use QuantFP8 for block quantization and rely on Inductor fusion 3. (bonus) add support for group quantization to the fused rms...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: tive::elementwise` are elementwise ops not visible to `torch.compile` - `triton_red_fused_...` are (fused) elementwise ops visible to `torch.compile` and lowered into fused Triton kernels - all other kernels are custom...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: into fused Triton kernels - all other kernels are custom kernels (attn, GEMM, MoE, allreduce, quant, etc.) The fusion opportunities are below: ### Action items - RMSNorm + quant (fusions 1 & 2): 1. Unwrap `apply_w8a8_bl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: work on unwrapping custom ops and enabling additional fusions inside the model forward pass. ## Motivation While profiling Deepseek, GPT-OSS, and LLaMa (in-progress), we noticed a lot of overhead from elementwise & unfu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: xample trace (Deepseek): How to read this trace: - `nvjet_...` are unquantized `torch.mm` calls - `native::elementwise` are elementwise ops not visible to `torch.compile` - `triton_red_fused_...` are (fused) elementwise...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ld extract prefill-decode split from op? - what happens to piecewise cudagraphs - attn + quant (fusion 4): 1. Kernel support for group output quant for flash attn (MLA prefill, also MQA) 2. Kernel support for group outp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
