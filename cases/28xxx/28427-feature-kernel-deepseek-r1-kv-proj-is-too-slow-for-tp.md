# vllm-project/vllm#28427: [Feature][Kernel]: DeepSeek-R1 KV Proj is Too Slow for TP

| 字段 | 值 |
| --- | --- |
| Issue | [#28427](https://github.com/vllm-project/vllm/issues/28427) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][Kernel]: DeepSeek-R1 KV Proj is Too Slow for TP

### Issue 正文摘录

### 🚀 The feature, motivation and pitch TRT-LLM has a SwapAB kernel for KV proj for DSR1. We should integrate this by collaborating with the FlashInfer team Current situation: we run CUTLASS Block Fp8 for KV proj because DeepGEMM upstream does not support it - the CUTLASS Block Fp8 kernels are ~1/2 the speed of DeepGEMM for other Linear layers - the CUTLASS Block Fp8 kernels have padding overhead Example Trace: > note: in this example, we are using DeepGEMM for the Routed Expert. This will run with Triton / DeepGEMM Swap AB TEP in the final implementation ### Alternatives - improve cutlass impl. IUUC in recent versions there is swap AB and an option for no padding ### Additional context cc @mgoin @yewentao256 @LucasWilkinson @MatthewBonanni @alexm-redhat ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: for KV proj for DSR1. We should integrate this by collaborating with the FlashInfer team Current situation: we run CUTLASS Block Fp8 for KV proj because DeepGEMM upstream does not support it - the CUTLASS Block Fp8 kern...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: eam Current situation: we run CUTLASS Block Fp8 for KV proj because DeepGEMM upstream does not support it - the CUTLASS Block Fp8 kernels are ~1/2 the speed of DeepGEMM for other Linear layers - the CUTLASS Block Fp8 ke...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: implementation ### Alternatives - improve cutlass impl. IUUC in recent versions there is swap AB and an option for no padding ### Additional context cc @mgoin @yewentao256 @LucasWilkinson @MatthewBonanni @alexm-redhat #...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: rating with the FlashInfer team Current situation: we run CUTLASS Block Fp8 for KV proj because DeepGEMM upstream does not support it - the CUTLASS Block Fp8 kernels are ~1/2 the speed of DeepGEMM for other Linear layer...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: at ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
