# vllm-project/vllm#37832: [Performance]: Deepseek performance regressing with norm fusion enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#37832](https://github.com/vllm-project/vllm/issues/37832) |
| 状态 | open |
| 标签 | performance;torch.compile |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;ci_build;distributed_parallel;gemm_linear;model_support;moe;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | activation;cuda;fp8;gemm;kernel;moe;operator;quantization;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Deepseek performance regressing with norm fusion enabled

### Issue 正文摘录

### Proposal to improve performance ## Summary While profiling DeepSeek-R1 671B FP8 with Inductor compilation (O2), we observed that the default fuse_norm_quant=true configuration is slower than fuse_norm_quant=false. Disabling the norm fusion pass consistently recovers ~1 ms/step TPOT across TP=4 and TP=8 configurations. The root cause is enable_norm_fusion() in vllm/config/vllm.py, which activates RMSNormQuantFusionPass for FP8 models where rms_norm is native (decomposed by Inductor). The pass replaces Inductor-decomposed norm ops with an opaque CUDA extern rms_norm_per_block_quant, which introduces a redundant no-op kernel that Inductor cannot eliminate. ## Environment - Model: DeepSeek-R1 671B FP8 (`deepseek-ai/DeepSeek-R1`) - Hardware: 8x NVIDIA B200 (TP=8), Driver 580.82.07 - vLLM: 0.16.0 - PyTorch: 2.12.0a0+gitb05b2d3 (local build) - CUDA: 12.9, Triton: 3.5.1 - Python: 3.12.12 - Optimization level: O2 (default) ### Why the opaque extern hurts performance Inductor + norm fusion true (dafault) 38us Inductor + norm fusion false 28 us The fusion pass replacement creates a no-op identity kernel(~5-10us per no-op). The `RMSNormQuantFusionPass` replacement function does `input = i...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: osal to improve performance ## Summary While profiling DeepSeek-R1 671B FP8 with Inductor compilation (O2), we observed that the default fuse_norm_quant=true configuration is slower than fuse_norm_quant=false. Disabling...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: ance;torch.compile ### Proposal to improve performance ## Summary While profiling DeepSeek-R1 671B FP8 with Inductor compilation (O2), we observed that the default fuse_norm_quant=true configuration is slower than fuse_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: epseek performance regressing with norm fusion enabled performance;torch.compile ### Proposal to improve performance ## Summary While profiling DeepSeek-R1 671B FP8 with Inductor compilation (O2), we observed that the d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Inductor). The pass replaces Inductor-decomposed norm ops with an opaque CUDA extern rms_norm_per_block_quant, which introduces a redundant no-op kernel that Inductor cannot eliminate. ## Environment - Model: DeepSeek-R...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: l body (from Inductor codegen): def triton_poi_fused__to_copy_empty_like_permute_to_2(in_out_ptr0, xnumel, XBLOCK): tmp0 = tl.load(in_out_ptr0 + (x0), xmask).to(tl.float32) # load bf16 -> f32 tmp1 = tmp0.to(tl.float32)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
