# vllm-project/vllm#35303: [Bug] CompressedTensorsWNA16MarlinMoEMethod registers g_idx params unconditionally, crashes with actorder=null AWQ MoE models

| 字段 | 值 |
| --- | --- |
| Issue | [#35303](https://github.com/vllm-project/vllm/issues/35303) |
| 状态 | open |
| 标签 | stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;ci_build;hardware_porting;model_support;moe;multimodal_vlm;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;moe;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] CompressedTensorsWNA16MarlinMoEMethod registers g_idx params unconditionally, crashes with actorder=null AWQ MoE models

### Issue 正文摘录

## Your current environment - vLLM version: `0.16.0rc2.dev472+gee59a7c61` (nightly wheel from `wheels.vllm.ai`) - PyTorch version: `2.10.0+cu130` - GPU: NVIDIA GeForce RTX 5090 (Blackwell, sm_120) - NVIDIA driver: 590.48 - CUDA (container): 13.0 - OS: Ubuntu (Docker container based on `vllm/vllm-openai:latest-cu130`) ## Model `cpatonn/Qwen3-VL-30B-A3B-Instruct-AWQ-4bit` — a Qwen3-VL 30B MoE vision-language model quantized with AWQ 4-bit using compressed-tensors format. Quantization config from `config.json`: ```json { "quant_method": "compressed-tensors", "format": "pack-quantized", "actorder": null, "group_size": 32, "num_bits": 4, "strategy": "group", "symmetric": true } ``` ## Bug description `CompressedTensorsWNA16MarlinMoEMethod.create_weights()` unconditionally registers `w13_weight_g_idx`, `w2_weight_g_idx`, `w13_g_idx_sort_indices`, and `w2_g_idx_sort_indices` as `nn.Parameter` via `layer.register_parameter()`. When `actorder` is `null` (no activation ordering), the model checkpoint does not contain these tensors. The uninitialized params tracking in `DefaultModelLoader.track_weights_loading()` then raises a hard `ValueError` because these registered parameters were never...

## 现有链接修复摘要

#35305 [BugFix] Fix MoE g_idx params causing ValueError with actorder=null AWQ models | #35611 [Bugfix] Fix CompressedTensors MoE g_idx registration when actorder is null

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: gisters g_idx params unconditionally, crashes with actorder=null AWQ MoE models stale ## Your current environment - vLLM version: `0.16.0rc2.dev472+gee59a7c61` (nightly wheel from `wheels.vllm.ai`) - PyTorch version: `2...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: h actorder=null AWQ MoE models stale ## Your current environment - vLLM version: `0.16.0rc2.dev472+gee59a7c61` (nightly wheel from `wheels.vllm.ai`) - PyTorch version: `2.10.0+cu130` - GPU: NVIDIA GeForce RTX 5090 (Blac...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: wheels.vllm.ai`) - PyTorch version: `2.10.0+cu130` - GPU: NVIDIA GeForce RTX 5090 (Blackwell, sm_120) - NVIDIA driver: 590.48 - CUDA (container): 13.0 - OS: Ubuntu (Docker container based on `vllm/vllm-openai:latest-cu1...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: VL-30B-A3B-Instruct-AWQ-4bit` — a Qwen3-VL 30B MoE vision-language model quantized with AWQ 4-bit using compressed-tensors format. Quantization config from `config.json`: ```json { "quant_method": "compressed-tensors",...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug] CompressedTensorsWNA16MarlinMoEMethod registers g_idx params unconditionally, crashes with actorder=null AWQ MoE models stale ## Your current environment - vLLM version: `0.16.0rc2.dev472+gee59a7c61` (nightly whee...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35305](https://github.com/vllm-project/vllm/pull/35305) | closes_keyword | 0.95 | [BugFix] Fix MoE g_idx params causing ValueError with actorder=null AWQ models | Fixes #35303 ## Motivation `CompressedTensorsWNA16MarlinMoEMethod.create_weights()` unconditionally registers `w13_weight_g_idx`, `w2_weight_g_idx`, `w13_g_idx_sort_indices`, and |
| [#35611](https://github.com/vllm-project/vllm/pull/35611) | closes_keyword | 0.95 | [Bugfix] Fix CompressedTensors MoE g_idx registration when actorder is null | Fixes #35303 ## Root Cause `CompressedTensorsWNA16MarlinMoEMethod.create_weights()` unconditionally registers `g_idx` and `sort_indices` parameters even when `actorder` is `None` |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
