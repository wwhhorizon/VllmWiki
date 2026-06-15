# vllm-project/vllm#9640: [Bug]: glm4-9b-chat-lora-merge model with VLLM for concurrent requests, the process gets stuck and returns an "Aborted request" error.

| 字段 | 值 |
| --- | --- |
| Issue | [#9640](https://github.com/vllm-project/vllm/issues/9640) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: glm4-9b-chat-lora-merge model with VLLM for concurrent requests, the process gets stuck and returns an "Aborted request" error.

### Issue 正文摘录

### Your current environment env: ``` PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.30.5 Libc version: glibc-2.31 Python version: 3.11.0 (main, Mar 1 2023, 18:26:19) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.4.0-189-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 11.4.48 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100 80GB PCIe GPU 1: NVIDIA A100 80GB PCIe Nvidia driver version: 535.183.01 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 46 bits physical, 48 bits virtual CPU(s): 64 On-line CPU(s) list: 0-63 Thread(s) per core: 2 Core(s) per socket: 16 Socket(s): 2 NUMA node(s): 2 Vendor ID: GenuineIntel CPU family: 6 Model: 85 Model name: Intel(R) Xeon(R) Gold 6226R CPU @ 2.90GHz Stepping: 7 CPU MHz: 1258.394 CPU max MHz: 3900.0000 CPU min MHz...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: request" error. bug;stale ### Your current environment env: ``` PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04 LTS (x86_64) GCC versi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: environment env: ``` PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 C...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: glm4-9b-chat-lora-merge model with VLLM for concurrent requests, the process gets stuck and returns an "Aborted request" error. bug;stale ### Your current environment env: ``` PyTorch version: 2.3.1+cu121 Is debu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: glm4-9b-chat-lora-merge model with VLLM for concurrent requests, the process gets stuck and returns an "Aborted request" error. bug;stale ### Your current environment env: ``` PyTorch version: 2.3.1+cu121 Is debu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: (): user_counts = [100] for count in user_counts: await test_concurrent_users(num_users=count, max_concurrent=100) if __name__ == "__main__": asyncio.run(main()) ``` ### Then the inference process gets stuck when there...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
