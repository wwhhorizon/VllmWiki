# vllm-project/vllm#6572: [Bug]: INFO 07-19 10:17:50 async_llm_engine.py:167] Aborted request 30d35945-d526-40bc-90c6-40ad73e639b9. INFO 07-19 10:17:50 async_llm_engine.py:49] Engine is gracefully shutting down.

| 字段 | 值 |
| --- | --- |
| Issue | [#6572](https://github.com/vllm-project/vllm/issues/6572) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: INFO 07-19 10:17:50 async_llm_engine.py:167] Aborted request 30d35945-d526-40bc-90c6-40ad73e639b9. INFO 07-19 10:17:50 async_llm_engine.py:49] Engine is gracefully shutting down.

### Issue 正文摘录

Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.29.6 Libc version: glibc-2.31 Python version: 3.10.14 (main, Apr 6 2024, 18:45:05) [GCC 9.4.0] (64-bit runtime) Python platform: Linux-5.15.0-1068-azure-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 10.1.243 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100 80GB PCIe MIG 3g.40gb Device 0: MIG 3g.40gb Device 1: Nvidia driver version: 535.183.01 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 48 bits physical, 48 bits virtual CPU(s): 24 On-line CPU(s) list: 0-23 Thread(s) per core: 1 Core(s) per socket: 24 Socket(s): 1 NUMA node(s): 1 Vendor ID: AuthenticAMD CPU family: 25 Model: 1 Model name: AMD EPYC 7V13 64-Core Processor Stepping: 1 CPU MHz: 2445.437 BogoMIPS: 4890.87 Hypervis...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: y shutting down. bug;stale Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC ve...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: ] Engine is gracefully shutting down. bug;stale Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: tensor_parallel_size=1, gpu_memory_utilization=0.2, max_model_len=1024, dtype="bfloat16") ) async def run_query(query: str): params = SamplingParams( top_k=10, temperature=0.01, repetition_penalty=1.10, max_tokens=150,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: INFO 07-19 10:17:50 async_llm_engine.py:167] Aborted request 30d35945-d526-40bc-90c6-40ad73e639b9. INFO 07-19 10:17:50 async_llm_engine.py:49] Engine is gracefully shutting down. bug;stale Collecting environment...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
