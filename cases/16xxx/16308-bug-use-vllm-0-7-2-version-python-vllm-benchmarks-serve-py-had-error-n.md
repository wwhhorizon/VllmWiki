# vllm-project/vllm#16308: [Bug]: use vllm-0.7.2 version python vllm/benchmarks/serve.py had error: No plugins for group vllm.platform_plugins found. Automatically detected platform cuda.

| 字段 | 值 |
| --- | --- |
| Issue | [#16308](https://github.com/vllm-project/vllm/issues/16308) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: use vllm-0.7.2 version python vllm/benchmarks/serve.py had error: No plugins for group vllm.platform_plugins found. Automatically detected platform cuda.

### Issue 正文摘录

### Your current environment warnings.warn( PyTorch version: 2.5.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.22.1 Libc version: glibc-2.35 Python version: 3.10.0 (default, Mar 3 2022, 09:58:08) [GCC 7.5.0] (64-bit runtime) Python platform: Linux-5.15.0-94-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4090 D GPU 1: NVIDIA GeForce RTX 4090 D GPU 2: NVIDIA GeForce RTX 4090 D GPU 3: NVIDIA GeForce RTX 4090 D Nvidia driver version: 550.67 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.9.0 HIP runtime version: N/A MI...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: use vllm-0.7.2 version python vllm/benchmarks/serve.py had error: No plugins for group vllm.platform_plugins found. Automatically detected platform cuda. bug;stale ### Your current environment warnings.warn( PyTo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: s for group vllm.platform_plugins found. Automatically detected platform cuda. bug;stale ### Your current environment warnings.warn( PyTorch version: 2.5.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 RO...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4090 D GPU 1: NVIDIA GeForce RTX 4090 D GPU 2: NVIDIA GeForce RTX 4090 D GPU 3: NVIDIA GeForce...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: p vllm.platform_plugins found. Automatically detected platform cuda. bug;stale ### Your current environment warnings.warn( PyTorch version: 2.5.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: u118 [pip3] torchvision==0.20.1+cu118 [pip3] transformers==4.51.1 [pip3] triton==3.1.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu11 11.11.3.6 pypi_0 pypi [conda] nvidia-cublas-cu12 12.4.5.8

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
