# vllm-project/vllm#4987: [Bug]: benchmarking serving returns index -1 is out of bounds

| 字段 | 值 |
| --- | --- |
| Issue | [#4987](https://github.com/vllm-project/vllm/issues/4987) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 |  |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: benchmarking serving returns index -1 is out of bounds

### Issue 正文摘录

### Your current environment ```text vLLM Version: 0.4.2 vLLM Build Flags: [pip3] numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] triton==2.3.0 [pip3] vllm-nccl-cu12==2.18.1.0.4.0 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-6.1.75+-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L4 GPU 1: NVIDIA L4 GPU 2: NVIDIA L4 GPU 3: NVIDIA L4 GPU 4: NVIDIA L4 GPU 5: NVIDIA L4 GPU 6: NVIDIA L4 GPU 7: NVIDIA L4 OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.35 Nvidia driver version: 535.161.07 PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A ``` ### 🐛 Describe the bug Steps to reproduce: ``` python3 benchmarks/benchmark_serving.py \ --backend openai \ --model meta-llama/Meta-Llama-3-70B-Instruct \ --dataset-name sharegpt \ --dataset-path ShareGPT_V3_unfiltered_cleaned_split.json \ --request-rate 100 \ --num-pr...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: index -1 is out of bounds bug ### Your current environment ```text vLLM Version: 0.4.2 vLLM Build Flags: [pip3] numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] triton==2.3.0 [pip3] vllm-nccl-cu1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L4 GPU 1: NVIDIA L4 GPU 2: NVIDIA L4 GPU 3: NVIDIA L4 GPU 4: NVIDIA L4 GPU 5: NVIDIA L4 GPU 6: NVIDIA L4 GP...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] triton==2.3.0 [pip3] vllm-nccl-cu12==2.18.1.0.4.0 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platf...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ckages/numpy/lib/function_base.py", line 4283, in percentile return _quantile_unchecked( File "/usr/local/lib/python3.10/dist-packages/numpy/lib/function_base.py", line 4555, in _quantile_unchecked return _ureduce(a, Fi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: (64-bit runtime) Python platform: Linux-6.1.75+-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L4 GPU 1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
