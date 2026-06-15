# vllm-project/vllm#6314: [Bug]: Server fails to boot due to a tensor size mismatch when LoRA is enabled for GPTBigCode

| 字段 | 值 |
| --- | --- |
| Issue | [#6314](https://github.com/vllm-project/vllm/issues/6314) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;quantization;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Server fails to boot due to a tensor size mismatch when LoRA is enabled for GPTBigCode

### Issue 正文摘录

### Your current environment ``` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-4.18.0-372.46.1.el8_6.x86_64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB MIG 3g.40gb Device 0: Nvidia driver version: 535.104.05 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 57 bits virtual Byte Order: Little Endian CPU(s): 80 On-line CPU(s) list: 0-79 Vendor ID: GenuineIntel Model name: Intel Xeon Processor (Icelake) CPU family: 6 Model: 134 Thread(s) per core: 2 Core(s) per socket: 20 Socket(s): 2 Stepping: 0 BogoMIPS: 5600.03 Flags: fp...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: r current environment ``` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: Server fails to boot due to a tensor size mismatch when LoRA is enabled for GPTBigCode bug ### Your current environment ``` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: ffected Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Vulnerable: Clear CPU buffers attempted, no microcode; SMT Host state unknown Vulnerability Retbleed: Not affected Vulnerability Spec store byp...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='outlines', distributed_executor_ba...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: nvironment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
