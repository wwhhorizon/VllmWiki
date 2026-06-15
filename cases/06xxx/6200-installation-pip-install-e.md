# vllm-project/vllm#6200: [Installation]: pip install -e .

| 字段 | 值 |
| --- | --- |
| Issue | [#6200](https://github.com/vllm-project/vllm/issues/6200) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: pip install -e .

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04 LTS (x86_64) GCC version: (Ubuntu 13.2.0-23ubuntu4) 13.2.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.39 Python version: 3.12.3 (main, Apr 10 2024, 05:33:47) [GCC 13.2.0] (64-bit runtime) Python platform: Linux-6.8.0-36-generic-x86_64-with-glibc2.39 Is CUDA available: True CUDA runtime version: 12.5.82 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 3090 Nvidia driver version: 555.42.06 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 39 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 16 On-line CPU(s) list: 0-15 Vendor ID: GenuineIntel Model name: Intel(R) Core(TM) i5-14400F CPU family: 6 Model: 183 Thread(s) per core: 2 Core(s) per socket: 10 Socket(s): 1 Stepping: 1 CPU(s) scaling MHz: 59% CPU max MHz: 4700.0000 CPU min MHz: 800.0000 BogoMIPS: 4992.00 Flags: fpu vme de pse tsc...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [Installation]: pip install -e . installation;stale ### Your current environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 24.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04 LTS (x86_64) GCC version: (Ubuntu 13.2.0-23ubuntu4) 13.2.0 Clang v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: True CUDA runtime version: 12.5.82 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 3090 Nvidia driver version: 555.42.06 cuDNN version: Could not collect HIP runtime version: N/A...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: rent environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04 LTS (x86_64) GCC version: (Ubuntu 13.2.0-23ubuntu4) 13.2.0 Cl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Installation]: pip install -e . installation;stale ### Your current environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 24....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
