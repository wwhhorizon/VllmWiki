# vllm-project/vllm#5375: [Usage]: Resolve: ModuleNotFoundError: No module named 'vllm.model_executor.parallel_utils'

| 字段 | 值 |
| --- | --- |
| Issue | [#5375](https://github.com/vllm-project/vllm/issues/5375) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Resolve: ModuleNotFoundError: No module named 'vllm.model_executor.parallel_utils'

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 12 (bookworm) (x86_64) GCC version: (Debian 12.2.0-14) 12.2.0 Clang version: Could not collect CMake version: version 3.29.5 Libc version: glibc-2.36 Python version: 3.11.2 (main, Mar 13 2023, 12:18:29) [GCC 12.2.0] (64-bit runtime) Python platform: Linux-6.1.0-21-amd64-x86_64-with-glibc2.36 Is CUDA available: True CUDA runtime version: 12.5.40 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A30 GPU 1: Quadro M2000 Nvidia driver version: 555.42.02 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 8 On-line CPU(s) list: 0-7 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) CPU E5-1620 v3 @ 3.50GHz CPU family: 6 Model: 63 Thread(s) per core: 2 Core(s) per socket: 4 Socket(s): 1 Stepping: 2 CPU(s) scaling MHz: 99% CPU max MHz: 3600,0000 CPU min...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: rrent environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 12 (bookworm) (x86...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 12 (bookworm) (x86_64) GCC version: (Debian 12.2.0-14) 12.2....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: Resolve: ModuleNotFoundError: No module named 'vllm.model_executor.parallel_utils' usage ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: F...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Vulnerability Meltdown: Mitigation; PTI Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Not affected Vulnerability...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ansformers==2.7.0 [pip3] torch==2.3.0 [pip3] transformers==4.41.2 [pip3] triton==2.3.0 [conda] Could not collect ROCM Version: 5.2.21153-0 Neuron SDK Version: N/A vLLM Version: 0.4.3 vLLM Build Flags: CUDA Archs: Not Se...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
