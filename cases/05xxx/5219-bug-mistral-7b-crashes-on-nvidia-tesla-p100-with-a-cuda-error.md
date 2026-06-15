# vllm-project/vllm#5219: [Bug]: Mistral 7B crashes on NVidia Tesla P100 with a CUDA Error

| 字段 | 值 |
| --- | --- |
| Issue | [#5219](https://github.com/vllm-project/vllm/issues/5219) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Mistral 7B crashes on NVidia Tesla P100 with a CUDA Error

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 24.04 LTS (x86_64) GCC version: (Ubuntu 13.2.0-23ubuntu4) 13.2.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.39 Python version: 3.12.3 (main, Apr 10 2024, 05:33:47) [GCC 13.2.0] (64-bit runtime) Python platform: Linux-6.8.0-31-generic-x86_64-with-glibc2.39 Is CUDA available: N/A CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: N/A GPU models and configuration: GPU 0: Tesla P100-PCIE-16GB Nvidia driver version: 535.161.08 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: N/A CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 24 On-line CPU(s) list: 0-23 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) CPU E5-2630 v2 @ 2.60GHz CPU family: 6 Model: 62 Thread(s) per core: 2 Core(s) per socket: 6 Socket(s): 2 Stepping: 4 CPU(s) scaling MHz: 89% CPU max MHz: 3100.0000 CPU min MHz: 1200.0000 BogoMI...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: Your current environment Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 24.04 LTS (x86_64) GCC version: (Ubuntu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: a CUDA Error bug ### Your current environment Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 24.04 LTS (x86_64)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Mistral 7B crashes on NVidia Tesla P100 with a CUDA Error bug ### Your current environment Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: mpose.yml that install vLLM and downloads mistral 7b. That worked. The --dtype=half is needed for the P100. However, after Mistral is downloaded, the container crashes with a CUDA error. As far as I understand, CUDA is...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Vulnerability Meltdown: Mitigation; PTI Vulnerability Mmio stale data: Unknown: No mitigations Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
