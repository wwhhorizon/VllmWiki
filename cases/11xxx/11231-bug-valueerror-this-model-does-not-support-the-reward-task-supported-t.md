# vllm-project/vllm#11231: [Bug]: ValueError: This model does not support the 'reward' task. Supported tasks: {'embedding'}

| 字段 | 值 |
| --- | --- |
| Issue | [#11231](https://github.com/vllm-project/vllm/issues/11231) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: This model does not support the 'reward' task. Supported tasks: {'embedding'}

### Issue 正文摘录

### Your current environment WARNING 12-16 10:58:46 cuda.py:23] You are using a deprecated `pynvml` package. Please install `nvidia-ml-py` instead, and make sure to uninstall `pynvml`. When both of them are installed, `pynvml` will take precedence and cause errors. See https://pypi.org/project/pynvml for more information. Warning: Your installation of OpenCV appears to be broken: module 'cv2.dnn' has no attribute 'DictValue'.Please follow the instructions at https://github.com/opencv/opencv-python/issues/884 to correct your environment. The import of cv2 has been skipped. Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.2 Libc version: glibc-2.35 Python version: 3.10.12 (main, Jul 29 2024, 16:56:48) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-3.10.0-1160.99.1.el7.x86_64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.6.20 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A800-SX...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: 10:58:46 cuda.py:23] You are using a deprecated `pynvml` package. Please install `nvidia-ml-py` instead, and make sure to uninstall `pynvml`. When both of them are installed, `pynvml` will take precedence and cause erro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: {'embedding'} bug ### Your current environment WARNING 12-16 10:58:46 cuda.py:23] You are using a deprecated `pynvml` package. Please install `nvidia-ml-py` instead, and make sure to uninstall `pynvml`. When both of the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: ValueError: This model does not support the 'reward' task. Supported tasks: {'embedding'} bug ### Your current environment WARNING 12-16 10:58:46 cuda.py:23] You are using a deprecated `pynvml` package. Please in...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: eerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload vgif umip pku ospke vaes vpclmulqdq overflow_recov succor smca Virtualization: AMD-V L1d cac...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: onnx==1.16.0 [pip3] optree==0.12.1 [pip3] pynvml==11.4.1 [pip3] pytorch-triton==3.0.0+dedb7bdf3 [pip3] pyzmq==26.1.0 [pip3] torch==2.5.1 [pip3] torch_tensorrt==2.5.0a0 [pip3] torchvision==0.20.1 [pip3] transformers==4.4...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
