# vllm-project/vllm#18783: [Bug][V1] Structured output FSM failures should be handled gracefully without aborting requests

| 字段 | 值 |
| --- | --- |
| Issue | [#18783](https://github.com/vllm-project/vllm/issues/18783) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][V1] Structured output FSM failures should be handled gracefully without aborting requests

### Issue 正文摘录

### Your current environment ``` INFO 05-27 16:20:01 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 4.0.0 Libc version: glibc-2.35 Python version: 3.12.10 (main, Apr 9 2025, 08:55:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-6.8.0-59-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA H200 Nvidia driver version: 550.144.03 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 57 bits virtual Byte Order: Little Endian CPU(s): 192 On-line CPU(s) list: 0-191 Vendor ID: GenuineIntel Model name: INTEL(R) XEON(R) PLATINUM 8568Y+ CPU family: 6 Model: 207 Thread(s) per core: 2 Core(s) per socket: 48 Socket(s): 2 Stepping: 2 CP...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ly detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ve...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug][V1] Structured output FSM failures should be handled gracefully without aborting requests bug;stale ### Your current environment ``` INFO 05-27 16:20:01 [__init__.py:239] Automatically detected platform cuda. Coll...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: _.py:239] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ctured output FSM failures should be handled gracefully without aborting requests bug;stale ### Your current environment ``` INFO 05-27 16:20:01 [__init__.py:239] Automatically detected platform cuda. Collecting environ...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: dio==2.6.0 [pip3] torchvision==0.21.0 [pip3] transformers==4.51.1 [pip3] triton==3.2.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.8.5 vLLM Build Flags: CUDA Archs:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
