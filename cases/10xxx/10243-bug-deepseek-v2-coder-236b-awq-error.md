# vllm-project/vllm#10243: [Bug]: Deepseek V2 coder 236B awq error!

| 字段 | 值 |
| --- | --- |
| Issue | [#10243](https://github.com/vllm-project/vllm/issues/10243) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Deepseek V2 coder 236B awq error!

### Issue 正文摘录

### Your current environment Collecting environment information... WARNING 11-12 05:39:35 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") Warning: Your installation of OpenCV appears to be broken: module 'cv2.dnn' has no attribute 'DictValue'.Please follow the instructions at https://github.com/opencv/opencv-python/issues/884 to correct your environment. The import of cv2 has been skipped. PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 10.5.0-1ubuntu1~20.04) 10.5.0 Clang version: Could not collect CMake version: version 3.30.4 Libc version: glibc-2.35 Python version: 3.10.12 (main, Sep 11 2024, 15:47:36) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.4.0-144-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.6.77 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A40 GPU 1: NVIDIA A40 GPU 2: NVIDIA A40 GPU 3: NVIDIA A40 GPU 4: NVIDIA A40 GPU 5: NVIDIA A40 GPU 6: NVIDIA A40 GPU 7: NVIDIA A40 Nvidia driver version: 550.54.14 cuDNN version: Probably...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: nment information... WARNING 11-12 05:39:35 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") Warning: Your installation of OpenCV appears to be broken: module 'cv2.d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: cv2 has been skipped. PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 10.5.0-1ubuntu1~20.04) 10.5....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: error! bug;stale ### Your current environment Collecting environment information... WARNING 11-12 05:39:35 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") Warning:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Deepseek V2 coder 236B awq error! bug;stale ### Your current environment Collecting environment information... WARNING 11-12 05:39:35 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: rs==3.2.1 [pip3] torch==2.4.0 [pip3] torch_tensorrt==2.5.0a0 [pip3] torchprofile==0.0.4 [pip3] torchvision==0.19.0 [pip3] transformers==4.46.1 [pip3] transformers-stream-generator==0.0.5 [pip3] triton==3.0.0 [conda] Cou...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
