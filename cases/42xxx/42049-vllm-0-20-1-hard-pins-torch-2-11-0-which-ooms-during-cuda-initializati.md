# vllm-project/vllm#42049: vLLM 0.20.1 hard-pins torch 2.11.0, which OOMs during CUDA initialization on RTX 4090 / cu130

| 字段 | 值 |
| --- | --- |
| Issue | [#42049](https://github.com/vllm-project/vllm/issues/42049) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 | build_error;oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> vLLM 0.20.1 hard-pins torch 2.11.0, which OOMs during CUDA initialization on RTX 4090 / cu130

### Issue 正文摘录

# vLLM 0.20.1 hard-pins torch 2.11.0, which OOMs during CUDA initialization on RTX 4090 / cu130 ## Summary `vllm==0.20.1` hard-pins `torch==2.11.0`. On our 3x RTX 4090 Ubuntu server, this dependency stack appears to consume ~22-23 GiB VRAM per 24 GB GPU before model weights are loaded, causing vLLM to fail with CUDA OOM for any model. The same machine works with `torch==2.10.0+cu130`, but vLLM 0.20.1 cannot be used with torch 2.10.0 because of dependency and ABI incompatibility. Related upstream PyTorch issue: https://github.com/pytorch/pytorch/issues/182941 ## Environment - OS: Ubuntu - Python: 3.11 - GPU: 3x NVIDIA RTX 4090 24 GB - Driver: R580 - CUDA: 13.0.3 - vLLM: 0.20.1 - torch: 2.11.0+cu130 - NCCL: 2.30.4, from torch environment ## Actual behavior vLLM fails before model weights are loaded: ```text torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 23.04 GiB (GPU 0; 23.52 GiB total; 0 bytes free) ``` Before vLLM reaches the model loading phase, the torch environment already reports about 23 GiB GPU memory consumed. ## Reproduction ```python from vllm import LLM llm = LLM( model="/home/sinoma/models/google/gemma-4-31B-it", tensor_parallel_size=1, ) ``` The sa...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: .20.1` hard-pins `torch==2.11.0`. On our 3x RTX 4090 Ubuntu server, this dependency stack appears to consume ~22-23 GiB VRAM per 24 GB GPU before model weights are loaded, causing vLLM to fail with CUDA OOM for any mode...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: vLLM 0.20.1 hard-pins torch 2.11.0, which OOMs during CUDA initialization on RTX 4090 / cu130 # vLLM 0.20.1 hard-pins torch 2.11.0, which OOMs during CUDA initialization on RTX 4090 / cu130 ## Summary `vllm==0.20.1` har...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: dependency stack appears to consume ~22-23 GiB VRAM per 24 GB GPU before model weights are loaded, causing vLLM to fail with CUDA OOM for any model. The same machine works with `torch==2.10.0+cu130`, but vLLM 0.20.1 can...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: vLLM 0.20.1 hard-pins torch 2.11.0, which OOMs during CUDA initialization on RTX 4090 / cu130 # vLLM 0.20.1 hard-pins torch 2.11.0, which OOMs during CUDA initialization on RTX 4090 / cu130 ## Summary `vllm==0.20.1` har...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: =1, ) ``` The same issue happens with different models and with smaller/quantized models because almost no VRAM remains before model load starts. ## Minimal torch-level check ```python import torch print("torch:", torch...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
