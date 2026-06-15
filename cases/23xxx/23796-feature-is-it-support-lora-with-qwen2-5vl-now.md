# vllm-project/vllm#23796: [Feature]: is it support lora with Qwen2.5vl now ?

| 字段 | 值 |
| --- | --- |
| Issue | [#23796](https://github.com/vllm-project/vllm/issues/23796) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: is it support lora with Qwen2.5vl now ?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I use vllm v0.10.1.1 to deploy Qwen2.5vl with lora, my command is: python3 -m vllm.entrypoints.openai.api_server \ --model=${model_path} \ --served-model-name=qwenvl \ --dtype=bfloat16 \ --tensor-parallel-size=1 \ --trust-remote-code \ --disable-custom-all-reduce \ --gpu-memory-utilization=0.5 \ --host=0.0.0.0 \ --port=50019 \ --max-model-len=1024 \ --max-num-seqs=32 \ --disable-log-requests \ --swap-space 16 \ --enable-lora \ --lora-modules test_lora=${lora_dir_docker}/${lora_sub_dir_name1} and I get error: 2025-08-28 13:21:08 2025-08-28 13:21:08 ========== 2025-08-28 13:21:08 == CUDA == 2025-08-28 13:21:08 ========== 2025-08-28 13:21:08 2025-08-28 13:21:08 CUDA Version 12.4.1 2025-08-28 13:21:08 2025-08-28 13:21:08 Container image Copyright (c) 2016-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved. 2025-08-28 13:21:08 2025-08-28 13:21:08 This container image and its contents are governed by the NVIDIA Deep Learning Container License. 2025-08-28 13:21:08 By pulling and using the container, you accept the terms and conditions of this license: 2025-08-28 13:21:08 https://developer.nvidia.com/ngc/nvidia-deep-learning-container-licens...

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: p-space 16 \ --enable-lora \ --lora-modules test_lora=${lora_dir_docker}/${lora_sub_dir_name1} and I get error: 2025-08-28 13:21:08 2025-08-28 13:21:08 ========== 2025-08-28 13:21:08 == CUDA == 2025-08-28 13:21:08 =====...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Feature]: is it support lora with Qwen2.5vl now ? feature request ### 🚀 The feature, motivation and pitch I use vllm v0.10.1.1 to deploy Qwen2.5vl with lora, my command is: python3 -m vllm.entrypoints.openai.api_server...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Feature]: is it support lora with Qwen2.5vl now ? feature request ### 🚀 The feature, motivation and pitch I use vllm v0.10.1.1 to deploy Qwen2.5vl with lora, my command is: python3 -m vllm.entrypoints.openai.api_server...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ver \ --model=${model_path} \ --served-model-name=qwenvl \ --dtype=bfloat16 \ --tensor-parallel-size=1 \ --trust-remote-code \ --disable-custom-all-reduce \ --gpu-memory-utilization=0.5 \ --host=0.0.0.0 \ --port=50019 \...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23797: Should have ROCm label: NO (0 matches) #23796: Should have ROCm label: NO (0 matches) #23794: Should have ROCm label: NO (0 matches) #23793: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
