# vllm-project/vllm#10625: [Doc]: docker+lmdeploy deploys multimodal large model and reports an error：AssertionError: failed to match chat template, please explicit set chat_template_config（docker+lmdeploy部署多模态大模型）

| 字段 | 值 |
| --- | --- |
| Issue | [#10625](https://github.com/vllm-project/vllm/issues/10625) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support;multimodal_vlm |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Doc]: docker+lmdeploy deploys multimodal large model and reports an error：AssertionError: failed to match chat template, please explicit set chat_template_config（docker+lmdeploy部署多模态大模型）

### Issue 正文摘录

### 📚 The doc issue The deployment process is as follows： pip install qwen_vl_utils git clone https://github.com/InternLM/lmdeploy.git cd lmdeploy docker build --build-arg CUDA_VERSION=cu12 -t openmmlab/lmdeploy:qwen2vl . -f ./docker/Qwen2VL_Dockerfile docker run --runtime nvidia --gpus all \ -v ~/Qwen2-VL-7B-Instruct:/lmdeploy/models \ -p 8000:8000 \ --ipc=host \ openmmlab/lmdeploy:latest \ lmdeploy serve api_server /lmdeploy/models (base) root@lxing:~/lmdeploy# docker run --runtime nvidia --gpus all \ -v ~/Qwen2-VL-7B-Instruct:/lmdeploy/models \ -v ~/Qwen2-VL-7B-Instruct/chat_template.json:/opt/lmdeploy/config/chat_template.json \ -p 8000:8000 \ --ipc=host \ openmmlab/lmdeploy:qwen2vl-v0.5.1 \ lmdeploy serve api_server /lmdeploy/models ========== == CUDA == ========== CUDA Version 12.4.1 Container image Copyright (c) 2016-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved. This container image and its contents are governed by the NVIDIA Deep Learning Container License. By pulling and using the container, you accept the terms and conditions of this license: https://developer.nvidia.com/ngc/nvidia-deep-learning-container-license A copy of this license is made available in...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Doc]: docker+lmdeploy deploys multimodal large model and reports an error：AssertionError: failed to match chat template, please explicit set chat_template_config（docker+lmdeploy部署多模态大模型） documentation ### 📚 The doc iss...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Doc]: docker+lmdeploy deploys multimodal large model and reports an error：AssertionError: failed to match chat template, please explicit set chat_template_config（docker+lmdeploy部署多模态大模型） documentation ### 📚 The doc iss...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ://github.com/InternLM/lmdeploy.git cd lmdeploy docker build --build-arg CUDA_VERSION=cu12 -t openmmlab/lmdeploy:qwen2vl . -f ./docker/Qwen2VL_Dockerfile docker run --runtime nvidia --gpus all \ -v ~/Qwen2-VL-7B-Instruc...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nvenience. 2024-11-25 03:36:47,633 - lmdeploy - WARNING - archs.py:53 - Fallback to pytorch engine because /lmdeploy/models not supported by turbomind engine. Qwen2VLRotaryEmbedding can now be fully parameterized by pas...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: oy/models \ -p 8000:8000 \ --ipc=host \ openmmlab/lmdeploy:latest \ lmdeploy serve api_server /lmdeploy/models (base) root@lxing:~/lmdeploy# docker run --runtime nvidia --gpus all \ -v ~/Qwen2-VL-7B-Instruct:/lmdeploy/m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
