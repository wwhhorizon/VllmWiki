# vllm-project/vllm#1437: Issue setting up server when using multiple GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#1437](https://github.com/vllm-project/vllm/issues/1437) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;kernel;operator;quantization |
| 症状 | crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Issue setting up server when using multiple GPUs

### Issue 正文摘录

I'm trying to setup a vllm server with `CodeLlama-7b-Instruct-hf` on a 4xA10G 24GB GPU machine. I'm able to start it when `tensor-parallel-size=1` (and I can see about 16GB of one GPU being utilized). But when I'm trying to use multiple GPUs (setting `tensor-parallel-size=4`), I'm getting the error shown below. I've tried other models and I'm seeing similar behavior. Any ideas how to resolve this? I'm using `vllm==0.2.1.post1`. ``` ========== == CUDA == ========== CUDA Version 11.8.0 Container image Copyright (c) 2016-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved. This container image and its contents are governed by the NVIDIA Deep Learning Container License. By pulling and using the container, you accept the terms and conditions of this license: https://developer.nvidia.com/ngc/nvidia-deep-learning-container-license A copy of this license is made available in this container at /NGC-DL-CONTAINER-LICENSE for your convenience. 2023-10-20 18:44:15,653 INFO worker.py:1642 -- Started a local Ray instance. INFO 10-20 18:44:16 llm_engine.py:72] Initializing an LLM engine with config: model='/models/CodeLlama-7b-Instruct-hf', tokenizer='/models/CodeLlama-7b-Instruct-hf', tok...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ver when using multiple GPUs I'm trying to setup a vllm server with `CodeLlama-7b-Instruct-hf` on a 4xA10G 24GB GPU machine. I'm able to start it when `tensor-parallel-size=1` (and I can see about 16GB of one GPU being...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: =auto, revision=None, tokenizer_re vision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=24576, download_dir=None, load_format=auto, tensor_parallel_size=4, quantization=None, seed=0) INFO 10-20 18:44:...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 'm using `vllm==0.2.1.post1`. ``` ========== == CUDA == ========== CUDA Version 11.8.0 Container image Copyright (c) 2016-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved. This container image and its contents...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: as how to resolve this? I'm using `vllm==0.2.1.post1`. ``` ========== == CUDA == ========== CUDA Version 11.8.0 Container image Copyright (c) 2016-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved. This contain...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: are some potential root causes. (1) The process is killed by SIGKILL by OOM killer due to high memory usage. (2) ray stop --force is called. (3) The worker is crashed unexpectedly due to SIGSEGV or other unexpected erro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
