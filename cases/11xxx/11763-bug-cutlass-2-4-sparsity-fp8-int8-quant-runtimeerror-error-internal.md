# vllm-project/vllm#11763: [Bug]: Cutlass 2:4 Sparsity + FP8/Int8 Quant RuntimeError: Error Internal

| 字段 | 值 |
| --- | --- |
| Issue | [#11763](https://github.com/vllm-project/vllm/issues/11763) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | attention;cuda;fp8;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Cutlass 2:4 Sparsity + FP8/Int8 Quant RuntimeError: Error Internal

### Issue 正文摘录

### Your current environment ``` PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Alibaba Group Enterprise Linux Server 7.2 (Paladin) (x86_64) GCC version: (GCC) 10.2.1 20200825 (Alibaba 10.2.1-3 2.17) Clang version: Could not collect CMake version: version 3.26.4 Libc version: glibc-2.32 Python version: 3.10.13 (main, Sep 11 2023, 13:44:35) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.10.134-16.3.al8.x86_64-x86_64-with-glibc2.32 Is CUDA available: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA H20 GPU 1: NVIDIA H20 GPU 2: NVIDIA H20 GPU 3: NVIDIA H20 Nvidia driver version: 535.183.06 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 192 On-line CPU(s) list: 0-191 Thread(s) per core: 2 Core(s) per socket: 48 Socket(s): 2 NUMA node(s): 2 Vendor ID: GenuineIntel CPU family: 6 Model: 143 Model name: Intel(R) Xeon(R) Platinum 8469C Stepping: 8 CPU MHz: 3100.000 CPU max MHz: 3800.0000 CPU m...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: Error: Error Internal bug;stale ### Your current environment ``` PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Alibaba Group Enterprise Linux Ser...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: Cutlass 2:4 Sparsity + FP8/Int8 Quant RuntimeError: Error Internal bug;stale ### Your current environment ``` PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: : Cutlass 2:4 Sparsity + FP8/Int8 Quant RuntimeError: Error Internal bug;stale ### Your current environment ``` PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: [Bug]: Cutlass 2:4 Sparsity + FP8/Int8 Quant RuntimeError: Error Internal bug;stale ### Your current environment ``` PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: rrent environment ``` PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Alibaba Group Enterprise Linux Server 7.2 (Paladin) (x86_64) GCC version: (GC...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
