# vllm-project/vllm#3785: [Bug]: 【P100】RuntimeError: CUDA error: no kernel image is available for execution on the device [repeated 6x across cluster]

| 字段 | 值 |
| --- | --- |
| Issue | [#3785](https://github.com/vllm-project/vllm/issues/3785) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 【P100】RuntimeError: CUDA error: no kernel image is available for execution on the device [repeated 6x across cluster]

### Issue 正文摘录

### Your current environment ``` Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: EulerOS 2.0 (SP10x86_64) (x86_64) GCC version: (GCC) 7.3.0 Clang version: Could not collect CMake version: version 3.29.0 Libc version: glibc-2.28 Python version: 3.10.14 (main, Mar 21 2024, 16:24:04) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-4.18.0-147.5.2.19.h1378.eulerosv2r10.x86_64-x86_64-with-glibc2.28 Is CUDA available: True CUDA runtime version: 12.1.66 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla P100-PCIE-16GB GPU 1: Tesla P100-PCIE-16GB GPU 2: Tesla P100-PCIE-16GB GPU 3: Tesla P100-PCIE-16GB GPU 4: Tesla P100-PCIE-16GB GPU 5: Tesla P100-PCIE-16GB GPU 6: Tesla P100-PCIE-16GB GPU 7: Tesla P100-PCIE-16GB Nvidia driver version: 530.30.02 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 46 bits physical, 48 bits virtual CPU(s): 72 On-line CPU(s) list: 0-71 Thread(s) per core: 2 Core(s) pe...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: r current environment ``` Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: EulerOS 2.0 (SP10x86_64) (x86_64) G...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: 【P100】RuntimeError: CUDA error: no kernel image is available for execution on the device [repeated 6x across cluster] bug ### Your current environment ``` Collecting environment information... PyTorch version: 2....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: cluster] bug ### Your current environment ``` Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: EulerOS 2.0 (SP...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: e Vulnerability Meltdown: Mitigation; PTI Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and seccomp...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: nvironment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: EulerOS 2.0 (SP10x86_64) (x86_64) GCC version: (GCC) 7.3.0 Clang version:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
