# vllm-project/vllm#25080: [Bug]: Torch.compile issues on Hopper when unwrapping operations in apply_w8a8_block_fp8_linear()

| 字段 | 值 |
| --- | --- |
| Issue | [#25080](https://github.com/vllm-project/vllm/issues/25080) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Torch.compile issues on Hopper when unwrapping operations in apply_w8a8_block_fp8_linear()

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Our goal is to be able to unwrap the operations called from `apply_w8a8_block_fp8_linear()` in `vllm/model_executor/layers/quantization/utils/fp8_utils.py` as much as possible such that they can be fused with preceding operations for better performance (as part of https://github.com/vllm-project/vllm/issues/24629). Currently, the block (1) ``` if cutlass_block_fp8_supported: num_pad = 0 if current_platform.is_device_capability(90): # pad first dimension to be divisible by 4 due to # cutlass blockwise gemm limitation for hopper num_pad = 4 - (input_2d.shape[0] % 4) if num_pad > 0: input_2d = torch.nn.functional.pad(input_2d, (0, 0, 0, num_pad), "constant", 0) q_input, x_scale = per_token_group_quant_fp8(input_2d, block_size[1], column_major_scales=True) output = w8a8_blockscale_func(q_input, weight, x_scale, weight_scale, block_size, input.dtype) if num_pad > 0: output = output[:-num_pad] ``` causes problems with torch.compile due to `input_2d.shape[0]` being a dynamic shape. [This PR](https://github.com/vllm-project/vllm/pull/24666) wraps the padding together with CUTLASS operation (which is called via `w8a8_blockscale_func` in t...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: .compile issues on Hopper when unwrapping operations in apply_w8a8_block_fp8_linear() bug;torch.compile ### Your current environment ### 🐛 Describe the bug Our goal is to be able to unwrap the operations called from `ap...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Torch.compile issues on Hopper when unwrapping operations in apply_w8a8_block_fp8_linear() bug;torch.compile ### Your current environment ### 🐛 Describe the bug Our goal is to be able to unwrap the operations cal...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Torch.compile issues on Hopper when unwrapping operations in apply_w8a8_block_fp8_linear() bug;torch.compile ### Your current environment ### 🐛 Describe the bug Our goal is to be able to unwrap the operations cal...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: hub.com/vllm-project/vllm/issues/24629). Currently, the block (1) ``` if cutlass_block_fp8_supported: num_pad = 0 if current_platform.is_device_capability(90): # pad first dimension to be divisible by 4 due to # cutlass...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: Torch.compile issues on Hopper when unwrapping operations in apply_w8a8_block_fp8_linear() bug;torch.compile ### Your current environment ### 🐛 Describe the bug Our goal is to be able to unwrap the operations called fro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
