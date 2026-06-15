# vllm-project/vllm#31668: [Bug]: TorchAO quantization is broken in vLLM v1 engine (v0.13.0)

| 字段 | 值 |
| --- | --- |
| Issue | [#31668](https://github.com/vllm-project/vllm/issues/31668) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TorchAO quantization is broken in vLLM v1 engine (v0.13.0)

### Issue 正文摘录

### Your current environment Collecting environment information... uv is set ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 3.31.6 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.9.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Feb 4 2025, 14:48:35) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-5.15.0-94-generic-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.9.86 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA H200 Nvidia driver version : 550.127.08 cuDNN version : Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.10.2 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.10.2 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9.10.2 /usr/l...

## 现有链接修复摘要

#31813 [Bugfix] Add TorchAO CLI Support and Fix Tensor Metadata Preservation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 3.31.6 Libc version : glibc-2.39 =================
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.5.3 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.9.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: 0.13.0) bug;stale ### Your current environment Collecting environment information... uv is set ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ub...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: TorchAO quantization is broken in vLLM v1 engine (v0.13.0) bug;stale ### Your current environment Collecting environment information... uv is set ============================== System Info =======================...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31813](https://github.com/vllm-project/vllm/pull/31813) | closes_keyword | 0.95 | [Bugfix] Add TorchAO CLI Support and Fix Tensor Metadata Preservation | Fixes #31668 ## Test Plan Unit Tests Added - `tests/engine/test_arg_utils.py` - `test_torchao_config_engine_args`: Basic attribute assignment - `test_torchao_config_adds_to_hf_ |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
