# vllm-project/vllm#9967: [Usage]: How to use `llava-hf/llava-1.5-7b-hf` with bitsandbytes quantization in `vllm serve`?

| 字段 | 值 |
| --- | --- |
| Issue | [#9967](https://github.com/vllm-project/vllm/issues/9967) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to use `llava-hf/llava-1.5-7b-hf` with bitsandbytes quantization in `vllm serve`?

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.22.1 Libc version: glibc-2.35 Python version: 3.12.3 | packaged by Anaconda, Inc. | (main, May 6 2024, 19:46:43) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.153.1-microsoft-standard-WSL2-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 11.5.119 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4060 Ti Nvidia driver version: 555.99 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 39 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 16 On-line CPU(s) list: 0-15 Vendor ID: GenuineIntel Model name: Intel(R) Core(TM) i5-14400 CPU family: 6 Model: 191 Thread(s) per core: 2 Core(s) per socket: 8 Socket(s): 1 Stepping: 2 BogoMIPS: 4992.00 Flags: fpu vme de pse tsc msr pae mce cx8 a...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ion in `vllm serve`? usage ### Your current environment ```text PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: environment ```text PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Usage]: How to use `llava-hf/llava-1.5-7b-hf` with bitsandbytes quantization in `vllm serve`? usage ### Your current environment ```text PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Mitigation; Enhanced IBRS Vulnerability Spec rstack overflow: Not affected Vulnerability Spec store bypass: M...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: rent environment ```text PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
