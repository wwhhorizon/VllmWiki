# vllm-project/vllm#5493: [Usage]: How do I get the FP8 scaling factors for KV cache?

| 字段 | 值 |
| --- | --- |
| Issue | [#5493](https://github.com/vllm-project/vllm/issues/5493) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How do I get the FP8 scaling factors for KV cache?

### Issue 正文摘录

### Your current environment Ubuntu 22 NVIDIA GeForce RTX 4090 ### How would you like to use vllm Guys, It's great to know that FP8 support is ready for testing in the latest version (v0.5.0). Using AutoFP8 to quantize a model is handy and fast. However, I noticed that scaling factors for the KV cache were not included in the quantized checkpoints. The documentation (https://docs.vllm.ai/en/stable/quantization/fp8.html and https://docs.vllm.ai/en/stable/quantization/fp8_e4m3_kvcache.html) mentions that we can specify a `kv_cache_scales.json` file or have the information contained within the quantized checkpoints. However, it does not explain how to get the scaling factors for the KV cache. My question is: Is it possible to obtain the scaling factors using AutoFP8, and if so, how?

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Usage]: How do I get the FP8 scaling factors for KV cache? usage ### Your current environment Ubuntu 22 NVIDIA GeForce RTX 4090 ### How would you like to use vllm Guys, It's great to know that FP8 support is ready for...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: It's great to know that FP8 support is ready for testing in the latest version (v0.5.0). Using AutoFP8 to quantize a model is handy and fast. However, I noticed that scaling factors for the KV cache were not included in...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: for testing in the latest version (v0.5.0). Using AutoFP8 to quantize a model is handy and fast. However, I noticed that scaling factors for the KV cache were not included in the quantized checkpoints. The documentation...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: r KV cache? usage ### Your current environment Ubuntu 22 NVIDIA GeForce RTX 4090 ### How would you like to use vllm Guys, It's great to know that FP8 support is ready for testing in the latest version (v0.5.0). Using Au...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Usage]: How do I get the FP8 scaling factors for KV cache? usage ### Your current environment Ubuntu 22 NVIDIA GeForce RTX 4090 ### How would you like to use vllm Guys, It's great to know that FP8 support is ready for...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
