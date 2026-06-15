# vllm-project/vllm#25179: [Performance]: Custom fused kernel tracking

| 字段 | 值 |
| --- | --- |
| Issue | [#25179](https://github.com/vllm-project/vllm/issues/25179) |
| 状态 | open |
| 标签 | performance;torch.compile |
| 评论 | 47; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;gemm_linear;hardware_porting;quantization;sampling_logits |
| 子分类 |  |
| Operator 关键词 | attention;cache;cuda;fp8;gemm;kernel;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Custom fused kernel tracking

### Issue 正文摘录

We need various additional fused kernels so we can allow fusion to happen orthogonally of other features. E.g. we want to support more kinds of quantization with existing passes, as well as allow for quantized kv cache to be orthogonal to fusion. Some of these kernels will require new passes, and most will require new patterns in existing passes. ### Flashinfer (B200) Currently available (and integrated): - silu_mul + nvfp4 - fp8 attention (decode) + static fp8 quant - fp8 attention (prefill) + static fp8 quant - fp8 attention (decode) + nvfp4 quant - fp8 attention (prefill) + nvfp4 quant - all_reduce + rms_norm - all_reduce + rms_norm + static fp8 quant - all_reduce + rms_norm + nvfp4 quant Currently available (and not integrated): - ? bf16 attention (decode) + static fp8 quant - ? bf16 attention (decode) + nvfp4 quant - rope + static fp8 quant - rope + kvcache - rope + static fp8 quant + kvcache - ? mla attention (prefill) + static fp8 quant - ? mla attention (prefill) + nvfp4 quant I don't remember if bf16-attn with fused output quant was supported in prefill or decode but I think it was just one of the two. @pavanimajety is already working on integrating RoPE fusion. I also re...

## 现有链接修复摘要

#36689 [Feature]: Fused CUTLASS GEMM + static FP8 output quant in epilogue | #38211 [Feature]: fused RMSNorm + fp8 block quantized kernel in Helion

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: en orthogonally of other features. E.g. we want to support more kinds of quantization with existing passes, as well as allow for quantized kv cache to be orthogonal to fusion. Some of these kernels will require new pass...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: new passes, and most will require new patterns in existing passes. ### Flashinfer (B200) Currently available (and integrated): - silu_mul + nvfp4 - fp8 attention (decode) + static fp8 quant - fp8 attention (prefill) + s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: and most will require new patterns in existing passes. ### Flashinfer (B200) Currently available (and integrated): - silu_mul + nvfp4 - fp8 attention (decode) + static fp8 quant - fp8 attention (prefill) + static fp8 qu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Performance]: Custom fused kernel tracking performance;torch.compile We need various additional fused kernels so we can allow fusion to happen orthogonally of other features. E.g. we want to support more kinds of quant...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: urrently available (and integrated): - silu_mul + nvfp4 - fp8 attention (decode) + static fp8 quant - fp8 attention (prefill) + static fp8 quant - fp8 attention (decode) + nvfp4 quant - fp8 attention (prefill) + nvfp4 q...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36689](https://github.com/vllm-project/vllm/pull/36689) | mentioned | 0.6 | [Feature]: Fused CUTLASS GEMM + static FP8 output quant in epilogue | ed CUTLASS GEMM + static FP8 output quant in epilogue ## Purpose Ref: #25179 Adding a fused kernel that packs scaled GEMM with static FP8 quant in the existing CUTLASS epilogue. T… |
| [#38211](https://github.com/vllm-project/vllm/pull/38211) | mentioned | 0.6 | [Feature]: fused RMSNorm + fp8 block quantized kernel in Helion | ing CUDA kernel (`rms_norm_per_block_quant`) this is a sub-task of #25179 and closes #38071 unlike the existing CUDA kernel, this Helion kernel improves portability across hardwar |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
