# vllm-project/vllm#8083: [Installation]: building CPU docker image crashes my machine 

| 字段 | 值 |
| --- | --- |
| Issue | [#8083](https://github.com/vllm-project/vllm/issues/8083) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: building CPU docker image crashes my machine 

### Issue 正文摘录

### Your current environment title says it all, when running ```bash docker build -f Dockerfile.cpu -t vllm-cpu-env --shm-size=4g . ``` the build process gets up to [this line](https://github.com/vllm-project/vllm/blob/e2b2aa5a0fdd3e682dd1fbd62e2ba81b8aa054d2/Dockerfile.cpu#L44 ) and subsequently freezes my pc indefinitely. No error messages to share.. PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0 Clang version: Could not collect CMake version: version 3.30.2 Libc version: glibc-2.35 Python version: 3.10.12 (main, Jul 29 2024, 16:56:48) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-6.8.0-40-generic-x86_64-with-glibc2.35 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 39 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 8 On-line CP...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: building CPU docker image crashes my machine installation;stale ### Your current environment title says it all, when running ```bash docker build -f Dockerfile.cpu -t vllm-cpu-env --shm-size=4g . ```
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: messages to share.. PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNN...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: nstallation]: building CPU docker image crashes my machine installation;stale ### Your current environment title says it all, when running ```bash docker build -f Dockerfile.cpu -t vllm-cpu-env --shm-size=4g . ``` the b...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rch==2.4.0 [pip3] torchvision==0.19.0 [pip3] transformers==4.44.2 [pip3] triton==3.0.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.5.5@2148441fd371faf3e90748b310fdb4...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
