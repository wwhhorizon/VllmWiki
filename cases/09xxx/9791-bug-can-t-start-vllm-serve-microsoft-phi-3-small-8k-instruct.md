# vllm-project/vllm#9791: [Bug]: Can't start `vllm serve microsoft/Phi-3-small-8k-instruct`

| 字段 | 值 |
| --- | --- |
| Issue | [#9791](https://github.com/vllm-project/vllm/issues/9791) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Can't start `vllm serve microsoft/Phi-3-small-8k-instruct`

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I was trying to serve `microsoft/Phi-3-small-8k-instruct` using below command inside the docker container which installing only vllm==0.6.3 and modelscope, but facing error. `vllm serve ${LLM_MODEL_NAME} --trust-remote-code --dtype=half` ```sh $docker compose run --rm phi_3_api nvidia-smi ========== == CUDA == ========== CUDA Version 12.1.1 Container image Copyright (c) 2016-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved. This container image and its contents are governed by the NVIDIA Deep Learning Container License. By pulling and using the container, you accept the terms and conditions of this license: https://developer.nvidia.com/ngc/nvidia-deep-learning-container-license A copy of this license is made available in this container at /NGC-DL-CONTAINER-LICENSE for your convenience. Tue Oct 29 09:23:11 2024 +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 550.54.15 Driver Version: 550.54.15 CUDA Version: 12.4 | |-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: serve `microsoft/Phi-3-small-8k-instruct` using below command inside the docker container which installing only vllm==0.6.3 and modelscope, but facing error. `vllm serve ${LLM_MODEL_NAME} --trust-remote-code --dtype=hal...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Can't start `vllm serve microsoft/Phi-3-small-8k-instruct` bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I was trying to serve `microsoft/Phi-3-small-8k-instruct` usi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: but facing error. `vllm serve ${LLM_MODEL_NAME} --trust-remote-code --dtype=half` ```sh $docker compose run --rm phi_3_api nvidia-smi ========== == CUDA == ========== CUDA Version 12.1.1 Container image Copyright (c) 20...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rosoft/Phi-3-small-8k-instruct` bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I was trying to serve `microsoft/Phi-3-small-8k-instruct` using below command inside the docker...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ogits;speculative_decoding attention;cuda;operator;quantization;sampling;triton build_error;crash;nan_inf;slowdown dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
