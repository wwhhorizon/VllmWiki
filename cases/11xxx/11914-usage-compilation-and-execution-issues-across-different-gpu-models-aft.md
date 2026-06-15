# vllm-project/vllm#11914: [Usage]: Compilation and Execution Issues Across Different GPU Models After Modifying vLLM Source Code

| 字段 | 值 |
| --- | --- |
| Issue | [#11914](https://github.com/vllm-project/vllm/issues/11914) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;operator;triton |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Compilation and Execution Issues Across Different GPU Models After Modifying vLLM Source Code

### Issue 正文摘录

### Your current environment ```text No module named 'vllm._version' from vllm.version import __version__ as VLLM_VERSION Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.5 Libc version: glibc-2.35 Python version: 3.10.12 (main, Sep 11 2024, 15:47:36) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-3.10.0-1062.el7.x86_64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-PCIE-40GB Nvidia driver version: 535.161.07 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 57 bits virtual Byte Order: Little Endian CPU(s): 112 On-line CPU(s) list: 0-111 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) Gold 6348 CPU @ 2.60GHz CPU family: 6 Model: 106 Thread(s) per core: 2 Core(s) per...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: usage;stale ### Your current environment ```text No module named 'vllm._version' from vllm.version import __version__ as VLLM_VERSION Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: Fa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: Compilation and Execution Issues Across Different GPU Models After Modifying vLLM Source Code usage;stale ### Your current environment ```text No module named 'vllm._version' from vllm.version import __version_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ssues Across Different GPU Models After Modifying vLLM Source Code usage;stale ### Your current environment ```text No module named 'vllm._version' from vllm.version import __version__ as VLLM_VERSION Collecting environ...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rch==2.4.0 [pip3] torchvision==0.19.0 [pip3] transformers==4.45.0 [pip3] triton==3.0.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: N/A (dev) vLLM Build Flags: CUDA Arc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
