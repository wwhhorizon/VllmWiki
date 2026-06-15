# vllm-project/vllm#6135: [Bug]: Phi-3 long context (longrope) doesn't work with fp8 kv cache

| 字段 | 值 |
| --- | --- |
| Issue | [#6135](https://github.com/vllm-project/vllm/issues/6135) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Phi-3 long context (longrope) doesn't work with fp8 kv cache

### Issue 正文摘录

### Your current environment (latest docker image `vllm/vllm-openai:latest`) ```text root@68ac2e4db323:/vllm-workspace# python3 collect_env.py Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.5 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.0-113-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4090 GPU 1: NVIDIA GeForce RTX 4090 Nvidia driver version: 550.90.07 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 32 On-line CPU(s) list: 0-31 Vendor ID: AuthenticAMD Model name: AMD Ryzen 9 7950X 16-Core Processor CPU fam...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: t work with fp8 kv cache bug;stale ### Your current environment (latest docker image `vllm/vllm-openai:latest`) ```text root@68ac2e4db323:/vllm-workspace# python3 collect_env.py Collecting environment information... PyT...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: onment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: Phi-3 long context (longrope) doesn't work with fp8 kv cache bug;stale ### Your current environment (latest docker image `vllm/vllm-openai:latest`) ```text root@68ac2e4db323:/vllm-workspace# python3 collect_env.p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: e4db323:/vllm-workspace# python3 collect_env.py Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Phi-3 long context (longrope) doesn't work with fp8 kv cache bug;stale ### Your current environment (latest docker image `vllm/vllm-openai:latest`) ```text root@68ac2e4db323:/vllm-workspace# python3 collect_env.p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
