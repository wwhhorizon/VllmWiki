# vllm-project/vllm#15255: [Bug]: --tensor-parallel-size Error

| 字段 | 值 |
| --- | --- |
| Issue | [#15255](https://github.com/vllm-project/vllm/issues/15255) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: --tensor-parallel-size Error

### Issue 正文摘录

### Your current environment INFO 03-20 23:36:27 [__init__.py:256] Automatically detected platform cuda. WARNING 03-20 23:36:27 [cuda.py:394] Detected different devices in the system: NVIDIA GeForce RTX 4080 SUPER, NVIDIA GeForce RTX 3060. Please make sure to set `CUDA_DEVICE_ORDER=PCI_BUS_ID` to avoid unexpected behavior. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.31.6 Libc version: glibc-2.35 Python version: 3.12.9 (main, Mar 17 2025, 21:01:58) [Clang 20.1.0 ] (64-bit runtime) Python platform: Linux-5.15.167.4-microsoft-standard-WSL2-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4080 SUPER GPU 1: NVIDIA GeForce RTX 3060 Nvidia driver version: 572.60 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-b...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ER, NVIDIA GeForce RTX 3060. Please make sure to set `CUDA_DEVICE_ORDER=PCI_BUS_ID` to avoid unexpected behavior. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to bui...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: t INFO 03-20 23:36:27 [__init__.py:256] Automatically detected platform cuda. WARNING 03-20 23:36:27 [cuda.py:394] Detected different devices in the system: NVIDIA GeForce RTX 4080 SUPER, NVIDIA GeForce RTX 3060. Please...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ORDER=PCI_BUS_ID` to avoid unexpected behavior. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: --tensor-parallel-size Error bug;stale ### Your current environment INFO 03-20 23:36:27 [__init__.py:256] Automatically detected platform cuda. WARNING 03-20 23:36:27 [cuda.py:394] Detected different devices in t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: async abort: Not affected Versions of relevant libraries: [pip3] flashinfer-python==0.2.1.post2+cu124torch2.6 [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda-cupti-cu12==12.4.127 [pip3] nvidi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
