# vllm-project/vllm#28121: [Bug]: Cannot load llmcompressor 3-bit quantized models but can load AutoGPTQ ones

| 字段 | 值 |
| --- | --- |
| Issue | [#28121](https://github.com/vllm-project/vllm/issues/28121) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Cannot load llmcompressor 3-bit quantized models but can load AutoGPTQ ones

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I quantized `Qwen/Qwen3-4B` to GPTQ/AWQ 3-bit and 4-bit using llmcompressor. 4-bit quants can be loaded, 3-bit cannot and hit a pydantic error: ``` ========== == CUDA == ========== CUDA Version 12.9.1 Container image Copyright (c) 2016-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved. This container image and its contents are governed by the NVIDIA Deep Learning Container License. By pulling and using the container, you accept the terms and conditions of this license: https://developer.nvidia.com/ngc/nvidia-deep-learning-container-license A copy of this license is made available in this container at /NGC-DL-CONTAINER-LICENSE for your convenience. INFO 11-05 10:16:19 [__init__.py:225] Automatically detected platform cuda. ERROR 11-05 10:16:20 [config.py:26] Failed to import Triton kernels. Please make sure your triton version is compatible. ERROR 11-05 10:16:20 [gpt_oss_triton_kernels_moe.py:27] Failed to import Triton kernels. Please make sure your triton version is compatible. Error: No module named 'triton.language.target_info' (APIServer pid=1) INFO 11-05 10:16:21 [api_server.py:1886] vLLM API server version 0.11.1rc...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: Cannot load llmcompressor 3-bit quantized models but can load AutoGPTQ ones bug;stale ### Your current environment ### 🐛 Describe the bug I quantized `Qwen/Qwen3-4B` to GPTQ/AWQ 3-bit and 4-bit using llmcompresso...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Cannot load llmcompressor 3-bit quantized models but can load AutoGPTQ ones bug;stale ### Your current environment ### 🐛 Describe the bug I quantized `Qwen/Qwen3-4B` to GPTQ/AWQ 3-bit and 4-bit using llmcompresso...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ot and hit a pydantic error: ``` ========== == CUDA == ========== CUDA Version 12.9.1 Container image Copyright (c) 2016-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved. This container image and its contents...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: load llmcompressor 3-bit quantized models but can load AutoGPTQ ones bug;stale ### Your current environment ### 🐛 Describe the bug I quantized `Qwen/Qwen3-4B` to GPTQ/AWQ 3-bit and 4-bit using llmcompressor. 4-bit quant...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: can be loaded, 3-bit cannot and hit a pydantic error: ``` ========== == CUDA == ========== CUDA Version 12.9.1 Container image Copyright (c) 2016-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved. This containe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
