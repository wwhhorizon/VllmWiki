# vllm-project/vllm#10204: [Usage]: cannot load GGUF model on multi GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#10204](https://github.com/vllm-project/vllm/issues/10204) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: cannot load GGUF model on multi GPU

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` WARNING 11-10 22:34:11 cuda.py:76] Detected different devices in the system: WARNING 11-10 22:34:11 cuda.py:76] NVIDIA GeForce RTX 3090 WARNING 11-10 22:34:11 cuda.py:76] NVIDIA GeForce RTX 3080 WARNING 11-10 22:34:11 cuda.py:76] Please make sure to set `CUDA_DEVICE_ORDER=PCI_BUS_ID` to avoid unexpected behavior. Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.35 Python version: 3.10.15 (main, Oct 3 2024, 07:27:34) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.153.1-microsoft-standard-WSL2-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 3090 GPU 1: NVIDIA GeForce RTX 3080 Nvidia driver version: 560.94 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK av...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: G 11-10 22:34:11 cuda.py:76] Please make sure to set `CUDA_DEVICE_ORDER=PCI_BUS_ID` to avoid unexpected behavior. Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to bui...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: nt ```text The output of `python collect_env.py` WARNING 11-10 22:34:11 cuda.py:76] Detected different devices in the system: WARNING 11-10 22:34:11 cuda.py:76] NVIDIA GeForce RTX 3090 WARNING 11-10 22:34:11 cuda.py:76]...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Vulnerable: Clear CPU buffers attempted, no microcode; SMT Host state unknown Vulnerability Retbleed: Mitigation; Enhanced IBRS Vulnerability Spec...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: cannot load GGUF model on multi GPU usage ### Your current environment ```text The output of `python collect_env.py` WARNING 11-10 22:34:11 cuda.py:76] Detected different devices in the system: WARNING 11-10 22...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: nvironment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
