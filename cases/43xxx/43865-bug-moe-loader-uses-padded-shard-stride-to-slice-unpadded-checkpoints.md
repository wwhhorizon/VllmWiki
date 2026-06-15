# vllm-project/vllm#43865: [Bug]: MoE loader uses padded shard stride to slice unpadded checkpoints

| 字段 | 值 |
| --- | --- |
| Issue | [#43865](https://github.com/vllm-project/vllm/issues/43865) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | shape_align |
| Operator 关键词 | cuda;kernel;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MoE loader uses padded shard stride to slice unpadded checkpoints

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When starting a vLLM server for some MXFP4 MoE models on ROCm with the AITER MoE backend, vLLM pads the destination MoE weight shapes for backend/kernel alignment, while the checkpoint tensors remain unpadded. The MoE weight loader currently uses the padded destination shard size as the stride for slicing the checkpoint tensor. This can make later tensor-parallel ranks read from the wrong checkpoint offset. For example, with `amd/Qwen3-235B-A22B-Instruct-2507-MXFP4` and TP=4, `w13` has checkpoint dimension 1536, so each TP rank should load 384 checkpoint dimensions. However, the padded destination shard size is 512, so the last TP rank (rank 3) starts at offset `3 * 512 = 1536` and loads zero checkpoint dimensions. The same issue appears for `w2`. The expected behavior is that checkpoint slicing should use the real checkpoint TP stride (`checkpoint dim / TP`) while still preserving the padded destination parameter shape required by the kernel. I have documented the reproduction steps and included an initial fix in the following PR: Related PR: https://github.com/vllm-project/vllm/pull/43863 ### Before submitting a new issue... -...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: When starting a vLLM server for some MXFP4 MoE models on ROCm with the AITER MoE backend, vLLM pads the destination MoE weight shapes for backend/kernel alignment, while the checkpoint tensors remain unpadded. The MoE w...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: er currently uses the padded destination shard size as the stride for slicing the checkpoint tensor. This can make later tensor-parallel ranks read from the wrong checkpoint offset. For example, with `amd/Qwen3-235B-A22...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ronment ### 🐛 Describe the bug When starting a vLLM server for some MXFP4 MoE models on ROCm with the AITER MoE backend, vLLM pads the destination MoE weight shapes for backend/kernel alignment, while the checkpoint ten...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ]: MoE loader uses padded shard stride to slice unpadded checkpoints bug;rocm ### Your current environment ### 🐛 Describe the bug When starting a vLLM server for some MXFP4 MoE models on ROCm with the AITER MoE backend,...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: MoE loader uses padded shard stride to slice unpadded checkpoints bug;rocm ### Your current environment ### 🐛 Describe the bug When starting a vLLM server for some MXFP4 MoE models on ROCm with the AITER MoE back...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
