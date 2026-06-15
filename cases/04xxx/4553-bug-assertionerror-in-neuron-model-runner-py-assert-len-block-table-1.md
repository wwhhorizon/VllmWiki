# vllm-project/vllm#4553: [Bug]: AssertionError in neuron_model_runner.py assert len(block_table) == 1

| 字段 | 值 |
| --- | --- |
| Issue | [#4553](https://github.com/vllm-project/vllm/issues/4553) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AssertionError in neuron_model_runner.py assert len(block_table) == 1

### Issue 正文摘录

### Your current environment PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.0-1031-aws-x86_64-with-glibc2.35 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 192 On-line CPU(s) list: 0-191 Vendor ID: AuthenticAMD Model name: AMD EPYC 7R13 Processor CPU family: 25 Model: 1 Thread(s) per core: 2 Core(s) per socket: 48 Socket(s): 2 Stepping: 1 BogoMIPS: 5299.99 Flags: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: rt len(block_table) == 1 bug;stale ### Your current environment PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: current environment PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: x==2.1.2.2.1.0 [pip3] torch-xla==2.1.2 [pip3] torchvision==0.16.2 [pip3] triton==2.1.0 [conda] Could not collectROCM Version: Could not collect Neuron SDK Version: (0, 'instance-type: inf2.48xlarge\ninstance-id: i-0e6cf...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: [Bug]: AssertionError in neuron_model_runner.py assert len(block_table) == 1 bug;stale ### Your current environment PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: AssertionError in neuron_model_runner.py assert len(block_table) == 1 bug;stale ### Your current environment PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
