# vllm-project/vllm#14636: [Bug]: CPU KV Cache Offload: AssertionError: disaggregated KV cache transfer parallel group is not initialized

| 字段 | 值 |
| --- | --- |
| Issue | [#14636](https://github.com/vllm-project/vllm/issues/14636) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CPU KV Cache Offload: AssertionError: disaggregated KV cache transfer parallel group is not initialized

### Issue 正文摘录

### Your current environment ``` Collecting environment information... PyTorch version: 2.7.0.dev20250121+cu126 Is debug build: False CUDA used to build PyTorch: 12.6 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (aarch64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.35 Python version: 3.12.8 (main, Dec 4 2024, 08:54:12) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-6.8.0-1022-nvidia-64k-aarch64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.6.20 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GH200 480GB Nvidia driver version: 550.120 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: aarch64 CPU op-mode(s): 64-bit Byte Order: Little Endian CPU(s): 72 On-line CPU(s) list: 0-71 Vendor ID: ARM Model name: Neoverse-V2 Model: 0 Thread(s) per core: 1 Core(s) per socket: 72 Socket(s): 1 Stepping: r0p0 Frequency boost: disabled CPU max MHz: 3456.0000 CPU min MHz: 81.0000 BogoMIPS: 2000.00 Flags: fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: r current environment ``` Collecting environment information... PyTorch version: 2.7.0.dev20250121+cu126 Is debug build: False CUDA used to build PyTorch: 12.6 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (aar...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: mation... PyTorch version: 2.7.0.dev20250121+cu126 Is debug build: False CUDA used to build PyTorch: 12.6 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (aarch64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: zed bug;stale ### Your current environment ``` Collecting environment information... PyTorch version: 2.7.0.dev20250121+cu126 Is debug build: False CUDA used to build PyTorch: 12.6 ROCM used to build PyTorch: N/A OS: Ub...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: r: disaggregated KV cache transfer parallel group is not initialized bug;stale ### Your current environment ``` Collecting environment information... PyTorch version: 2.7.0.dev20250121+cu126 Is debug build: False CUDA u...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: pip3] torchvision==0.22.0.dev20250121 [pip3] transformers==4.49.0 [pip3] triton==3.2.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.7.4.dev12+g0b8b2700.d20250221 vLLM...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
