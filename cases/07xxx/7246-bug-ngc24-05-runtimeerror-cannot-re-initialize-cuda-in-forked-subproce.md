# vllm-project/vllm#7246: [Bug]: ngc24.05 "RuntimeError: Cannot re-initialize CUDA in forked subprocess."

| 字段 | 值 |
| --- | --- |
| Issue | [#7246](https://github.com/vllm-project/vllm/issues/7246) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ngc24.05 "RuntimeError: Cannot re-initialize CUDA in forked subprocess."

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-3.10.0-1062.9.1.el7.x86_64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A30 GPU 1: NVIDIA A30 GPU 2: NVIDIA A30 GPU 3: NVIDIA A30 Nvidia driver version: 525.85.12 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_precompiled.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_runtime_compiled.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_graph.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_heuristic.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: rrent environment ```text Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: ngc24.05 "RuntimeError: Cannot re-initialize CUDA in forked subprocess." bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ess." bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [pip3] optree==0.11.0 [pip3] pytorch-quantization==2.1.2 [pip3] pytorch-triton==3.0.0+989adb9a2 [pip3] torch==2.4.0 [pip3] torch-tensorrt==2.4.0a0 [pip3] torchvision==0.19.0 [pip3] transformers==4.43.4 [pip3] triton==3....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: cl-cu12==2.20.5 [pip3] onnx==1.16.0 [pip3] optree==0.11.0 [pip3] pytorch-quantization==2.1.2 [pip3] pytorch-triton==3.0.0+989adb9a2 [pip3] torch==2.4.0 [pip3] torch-tensorrt==2.4.0a0 [pip3] torchvision==0.19.0 [pip3] tr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
