# vllm-project/vllm#5078: [Usage]: Inference on LLama3-8b-Instruct using Lora Adapter

| 字段 | 值 |
| --- | --- |
| Issue | [#5078](https://github.com/vllm-project/vllm/issues/5078) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Inference on LLama3-8b-Instruct using Lora Adapter

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.3 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-6.5.0-35-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4090 Nvidia driver version: 555.42.02 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 24 On-line CPU(s) list: 0-23 Vendor ID: GenuineIntel Model name: 13th Gen Intel(R) Core(TM) i7-13700K CPU family: 6 Model: 183 Thread(s) per core: 2 Core(s) per socket: 16 Socket(s): 1 Stepping: 1 CPU max MHz: 5400.0000 CPU min MHz: 800.0000 BogoMIPS: 6835.20 Flags: fpu vme de pse tsc...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: t using Lora Adapter usage ### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: nce pipeline in vLLM. ```python # The bits and bytes config we use for quantization bnb_config = BitsAndBytesConfig( load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_compute_dtype=torch.bfloat16, bnb_4bit_use_doub...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: Inference on LLama3-8b-Instruct using Lora Adapter usage ### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not affected Vulnerability Spec store bypass: Mitigation; Sp...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
