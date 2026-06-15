# vllm-project/vllm#24921: [Bug]: v0.10.2, Qwen3-30B-A3B-NVFP4 MOE model on 5090, sm_120 hardware, `no cutlass_scaled_mm kernel`

| 字段 | 值 |
| --- | --- |
| Issue | [#24921](https://github.com/vllm-project/vllm/issues/24921) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;gemm_linear;model_support;moe;quantization;sampling_logits |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;gemm;kernel;moe;operator;quantization;sampling |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.10.2, Qwen3-30B-A3B-NVFP4 MOE model on 5090, sm_120 hardware, `no cutlass_scaled_mm kernel`

### Issue 正文摘录

### Your current environment CUDA: 12.8.1 Base image: nvidia/cuda:12.8.1-devel-ubuntu22.04 vLLM: v0.10.2 GPU: RTX 5090 using sm_120 ### 🐛 Describe the bug I'm attempting to run an NVFP4 quant of `MrVolts/Qwen3-30B-A3B-Thinking-2507-NVFP4` because I understand that the sm_120 5090 has native support for the NVFP4 format, which was added to the vLLM engine here: https://github.com/vllm-project/vllm/pull/21309. However, I am encountering issues with Cutlass and the MOE architecture. I would appreciate it if someone could investigate this or correct me if I have misconfigured something. Using the sm_120's in-built support for this quant would greatly improve inference performance and hopefully adoption. Notes: - this model runs fine with: FP8 W8A8, another natively supported quant on the 5090 - I tried following this guide: https://www.reddit.com/r/LocalLLaMA/comments/1my3why/rtx_pro_6000_maxq_blackwell_for_llm/ However, he mentioned similar issues: ``` DeepSeek-R1-0528-Qwen3-8B-FP4 : could not start GEMM FP4 kernels, i'll investigate Qwen3-32B-FP4 : could not start GEMM FP4 kernels, i'll investigate ``` - I also tried following this: https://github.com/vllm-project/vllm/issues/23826...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ncountering issues with Cutlass and the MOE architecture. I would appreciate it if someone could investigate this or correct me if I have misconfigured something. Using the sm_120's in-built support for this quant would...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: v0.10.2, Qwen3-30B-A3B-NVFP4 MOE model on 5090, sm_120 hardware, `no cutlass_scaled_mm kernel` bug;stale ### Your current environment CUDA: 12.8.1 Base image: nvidia/cuda:12.8.1-devel-ubuntu22.04 vLLM: v0.10.2 GP...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: v0.10.2, Qwen3-30B-A3B-NVFP4 MOE model on 5090, sm_120 hardware, `no cutlass_scaled_mm kernel` bug;stale ### Your current environment CUDA: 12.8.1 Base image: nvidia/cuda:12.8.1-devel-ubuntu22.04 vLLM: v0.10.2 GP...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: v0.10.2, Qwen3-30B-A3B-NVFP4 MOE model on 5090, sm_120 hardware, `no cutlass_scaled_mm kernel` bug;stale ### Your current environment CUDA: 12.8.1 Base image: nvidia/cuda:12.8.1-devel-ubuntu22.04 vLLM: v0.10.2 GP...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [Bug]: v0.10.2, Qwen3-30B-A3B-NVFP4 MOE model on 5090, sm_120 hardware, `no cutlass_scaled_mm kernel` bug;stale ### Your current environment CUDA: 12.8.1 Base image: nvidia/cuda:12.8.1-devel-ubuntu22.04 vLLM: v0.10.2 GP...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
