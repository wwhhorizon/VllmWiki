# vllm-project/vllm#40047: [Bug][Tracking Issue]: NaNs in CUDA Graph padding regions corrupt activations in some per-token kernels

| 字段 | 值 |
| --- | --- |
| Issue | [#40047](https://github.com/vllm-project/vllm/issues/40047) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;moe;quantization |
| 症状 | nan_inf |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][Tracking Issue]: NaNs in CUDA Graph padding regions corrupt activations in some per-token kernels

### Issue 正文摘录

### Summary While debugging NaNs found during WideEP GB200 deployments of DeepSeek-R1-0528-NVFP4-v2 https://github.com/vllm-project/vllm/issues/37890, we have identified several kernels that leak NaNs from the CUDA Graph padding region into activation tokens. Even though each of these kernels is supposed to operate on each token independently, NaNs in some tokens can affect the others. In some cases this happens due to warp reductions used to compute scales for group quantization. Collecting the issues here to avoid filing a separate issue for each. We've landed a band-aid fix for (1) and have identified a somewhat intrusive band-aid fix for (2), (3), and likely (4). #### (1) FlashInfer: Padding NaNs corrupts activation scales in TRT-LLM `mm_fp4` See FlashInfer issue: https://github.com/flashinfer-ai/flashinfer/issues/2861 We landed a band-aid fix in https://github.com/vllm-project/vllm/pull/38148, which resolves the issues by zeroing out the scale padding. This could be removed once the `mm_fp4` bug is fixed. #### (2) FlashInfer Bug: Padding NaNs corrupts activation scales in `silu_and_mul_scaled_nvfp4_experts_quantize` and `scaled_fp4_grouped_quantize` See FlashInfer issue: http...

## 现有链接修复摘要

#42984 Resolve silu mul quant padded NaN corruption correctness

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: debugging NaNs found during WideEP GB200 deployments of DeepSeek-R1-0528-NVFP4-v2 https://github.com/vllm-project/vllm/issues/37890, we have identified several kernels that leak NaNs from the CUDA Graph padding region i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug][Tracking Issue]: NaNs in CUDA Graph padding regions corrupt activations in some per-token kernels ### Summary While debugging NaNs found during WideEP GB200 deployments of DeepSeek-R1-0528-NVFP4-v2 https://github....
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: g: Padding NaNs corrupts activation scales in `silu_and_mul_scaled_nvfp4_experts_quantize` and `scaled_fp4_grouped_quantize` See FlashInfer issue: https://github.com/flashinfer-ai/flashinfer/issues/3057 See failing test...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: somewhat intrusive band-aid fix for (2), (3), and likely (4). #### (1) FlashInfer: Padding NaNs corrupts activation scales in TRT-LLM `mm_fp4` See FlashInfer issue: https://github.com/flashinfer-ai/flashinfer/issues/286...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ue: https://github.com/flashinfer-ai/flashinfer/issues/3057 See failing test in vLLM Bug Hunt: https://github.com/tlrmchlsmth/vllm/pull/33 A bandaid fix is to zero out padding at the beginning of MoE layer: https://gith...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42984](https://github.com/vllm-project/vllm/pull/42984) | closes_keyword | 0.95 | Resolve silu mul quant padded NaN corruption correctness | fixed version of that test which passes even without this PR. Note, the above tests were included as part of #40047. ## Test Plan Add two tests: * `test_fp4_experts_qu |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
