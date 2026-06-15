# vllm-project/vllm#38720: [Performance]: FP8 (Fp8OnlineLinearMethod) significantly slower than BF16 for ReplicatedLinear

| 字段 | 值 |
| --- | --- |
| Issue | [#38720](https://github.com/vllm-project/vllm/issues/38720) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: FP8 (Fp8OnlineLinearMethod) significantly slower than BF16 for ReplicatedLinear

### Issue 正文摘录

### Proposal to improve performance I'm not sure how to improve performance yet. ### Report of performance regression ### Description I am observing a severe performance regression when using FP8 quantization compared to BF16. In my use case (OmniGen2 diffusion inference), enabling FP8 causes a dramatic slowdown: - BF16: ~30 denoising steps complete in ~30 seconds - FP8: ~30 seconds per step This is my setup: Hardware / stack: NVIDIA RTX 4090, PyTorch 2.10+cu128, vLLM 0.18.0 with CutlassFP8ScaledMMLinearKernel. I have a reproduce script below. If you run it, you can see FP8 is consistently **much slower** than BF16. Runtime taken : BF16 vs FP8 for a standalone vLLM ReplicatedLinear with random weights | seq_len | in_features | out_features | BF16 ms | FP8 ms | FP8/BF16 | |--------:|------------:|-------------:|--------:|--------:|----------:| | 128 | 256 | 512 | 0.0391 | 0.2363 | 6.04x | | 1104 | 2520 | 4200 | 0.1804 | 11.0370 | 61.17x | ### Misc discussion on performance This may be related to prior reports on quantization performance: - FP8 / quantized models not showing expected speedup: https://github.com/vllm-project/vllm/issues/17487 - FP8 slower than FP16 in some workloads:...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Performance]: FP8 (Fp8OnlineLinearMethod) significantly slower than BF16 for ReplicatedLinear performance ### Proposal to improve performance I'm not sure how to improve performance yet. ### Report of performance regre...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;fp8;g...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: FP8: ~30 seconds per step This is my setup: Hardware / stack: NVIDIA RTX 4090, PyTorch 2.10+cu128, vLLM 0.18.0 with CutlassFP8ScaledMMLinearKernel. I have a reproduce script below. If you run it, you can see FP8 is cons...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: Hardware / stack: NVIDIA RTX 4090, PyTorch 2.10+cu128, vLLM 0.18.0 with CutlassFP8ScaledMMLinearKernel. I have a reproduce script below. If you run it, you can see FP8 is consistently **much slower** than BF16. Runtime...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: I'm not sure how to improve performance yet. ### Report of performance regression ### Description I am observing a severe performance regression when using FP8 quantization compared to BF16. In my use case (OmniGen2 dif...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
