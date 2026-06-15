# vllm-project/vllm#4969: [Usage]: Is it possible to start 8 tp=1 LLMEngine on a 8-GPU machine?

| 字段 | 值 |
| --- | --- |
| Issue | [#4969](https://github.com/vllm-project/vllm/issues/4969) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Is it possible to start 8 tp=1 LLMEngine on a 8-GPU machine?

### Issue 正文摘录

### Your current environment ```text Collecting environment information... /home/corvo/.local/lib/python3.10/site-packages/transformers/utils/hub.py:124: FutureWarning: Using `TRANSFORMERS_CACHE` is deprecated and will be removed in v5 of Transformers. Use `HF_HOME` instead. warnings.warn( PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.28.3 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.10.213-201.855.amzn2.x86_64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.4.99 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-40GB GPU 1: NVIDIA A100-SXM4-40GB GPU 2: NVIDIA A100-SXM4-40GB GPU 3: NVIDIA A100-SXM4-40GB GPU 4: NVIDIA A100-SXM4-40GB GPU 5: NVIDIA A100-SXM4-40GB GPU 6: NVIDIA A100-SXM4-40GB GPU 7: NVIDIA A100-SXM4-40GB Nvidia driver version: 535.161.08 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudn...

## 现有链接修复摘要

#5473 Add `cuda_device_count_stateless`

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: d in v5 of Transformers. Use `HF_HOME` instead. warnings.warn( PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ead. warnings.warn( PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ne? usage ### Your current environment ```text Collecting environment information... /home/corvo/.local/lib/python3.10/site-packages/transformers/utils/hub.py:124: FutureWarning: Using `TRANSFORMERS_CACHE` is deprecated...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [pip3] optree==0.10.0 [pip3] pytorch-quantization==2.1.2 [pip3] pytorch-triton==2.2.0+e28a256d7 [pip3] torch==2.3.0 [pip3] torch-tensorrt==2.3.0a0 [pip3] torchdata==0.7.1a0 [pip3] torchtext==0.17.0a0 [pip3] torchvision=...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: cu12==2.20.5 [pip3] onnx==1.15.0rc2 [pip3] optree==0.10.0 [pip3] pytorch-quantization==2.1.2 [pip3] pytorch-triton==2.2.0+e28a256d7 [pip3] torch==2.3.0 [pip3] torch-tensorrt==2.3.0a0 [pip3] torchdata==0.7.1a0 [pip3] tor...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#5473](https://github.com/vllm-project/vllm/pull/5473) | closes_keyword | 0.95 | Add `cuda_device_count_stateless` | FIX #4969 FIX #4981 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
