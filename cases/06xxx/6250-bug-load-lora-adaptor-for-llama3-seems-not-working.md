# vllm-project/vllm#6250: [Bug]: Load LoRA adaptor for Llama3 seems not working 

| 字段 | 值 |
| --- | --- |
| Issue | [#6250](https://github.com/vllm-project/vllm/issues/6250) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Load LoRA adaptor for Llama3 seems not working 

### Issue 正文摘录

### Your current environment Collecting environment information. PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A 0S: Cent0S Linux release 7.9.2009 (Core) (x86 64) GCC version: (GCC) 11.1.0 Clang version: Could not collect CMake version: version 3.27.2 Libc version:qlibc-2.17 Python version: 3.11.4 (main, Jul5 2023,13:45:01) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-3.100-1160.e17.x86 64-x86 64-with-glibc2.17 Is CUDA available:True CUDA runtime version: 12.1.105 CUDA MODULE LOADING set to: LAZY GPU models and confiquration: GPU 0: NVIDIA.A100 80GB PCIe GPU 1: NVIDIA A100 80GB PCIe GPU 2: NVIDIA A100 80GB PCIe GPU 3:NVIDIA A100 80GB PCIe GPU 4:NVIDIA A100 80GB PCIe GPU 5:NVIDIA A100 80GB PCIe GPU 6: NVIDIA A100 80GB PCIe GPU 7: NVIDIA A100 80GB PCIe Nvidia driver version: 535.129.03 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available:True CPU: x86 64 Architecture: 32-6it64-bit CPU op-mode(s): Little Endian Byte Order: CPU(S): 48 On-Line CPU(s) list: Θ-47 Thread(s) per core: 1 Core(s) per socket: 24 Socket(s): 2 NUMA node(s): 2 Vendor ID: GenuineIntel...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ## Your current environment Collecting environment information. PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A 0S: Cent0S Linux release 7.9.2009 (Core...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ironment information. PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A 0S: Cent0S Linux release 7.9.2009 (Core) (x86 64) GCC version: (GCC) 11.1.0 Clang...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Load LoRA adaptor for Llama3 seems not working bug;stale ### Your current environment Collecting environment information. PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM u...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Load LoRA adaptor for Llama3 seems not working bug;stale ### Your current environment Collecting environment information. PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM u...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: environment information. PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A 0S: Cent0S Linux release 7.9.2009 (Core) (x86 64) GCC version: (GCC) 11.1.0 Cl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
