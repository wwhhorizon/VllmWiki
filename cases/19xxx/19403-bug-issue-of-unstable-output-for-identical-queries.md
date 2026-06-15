# vllm-project/vllm#19403: [Bug]: Issue of Unstable Output for Identical Queries

| 字段 | 值 |
| --- | --- |
| Issue | [#19403](https://github.com/vllm-project/vllm/issues/19403) |
| 状态 | closed |
| 标签 | bug;torch.compile;stale |
| 评论 | 31; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Issue of Unstable Output for Identical Queries

### Issue 正文摘录

### Your current environment INFO 06-10 00:07:35 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.31.4 Libc version: glibc-2.35 Python version: 3.12.8 (main, Dec 4 2024, 08:54:12) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.4.54-1.0.0.std7c.el7.2.x86_64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4090 GPU 1: NVIDIA GeForce RTX 4090 GPU 2: NVIDIA GeForce RTX 4090 GPU 3: NVIDIA GeForce RTX 4090 GPU 4: NVIDIA GeForce RTX 4090 GPU 5: NVIDIA GeForce RTX 4090 GPU 6: NVIDIA GeForce RTX 4090 GPU 7: NVIDIA GeForce RTX 4090 Nvidia driver version: 535.104.05 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 52 bits physical, 57 bits...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Bug]: Issue of Unstable Output for Identical Queries bug;torch.compile;stale ### Your current environment INFO 06-10 00:07:35 [__init__.py:239] Automatically detected platform cuda. Collecting environment information.....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: t INFO 06-10 00:07:35 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: _.py:239] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Issue of Unstable Output for Identical Queries bug;torch.compile;stale ### Your current environment INFO 06-10 00:07:35 [__init__.py:239] Automatically detected platform cuda. Collecting environment information.....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dio==2.6.0 [pip3] torchvision==0.21.0 [pip3] transformers==4.52.4 [pip3] triton==3.2.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.8.5 vLLM Build Flags: CUDA Archs:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
