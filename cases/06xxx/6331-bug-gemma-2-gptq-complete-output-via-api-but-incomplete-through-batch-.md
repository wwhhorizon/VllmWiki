# vllm-project/vllm#6331: [Bug]: Gemma 2 GPTQ - Complete output via API but incomplete through batch inference

| 字段 | 值 |
| --- | --- |
| Issue | [#6331](https://github.com/vllm-project/vllm/issues/6331) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma 2 GPTQ - Complete output via API but incomplete through batch inference

### Issue 正文摘录

### Your current environment > Collecting environment information... > PyTorch version: 2.3.0+cu121 > Is debug build: False > CUDA used to build PyTorch: 12.1 > ROCM used to build PyTorch: N/A > > OS: Ubuntu 22.04.4 LTS (x86_64) > GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 > Clang version: Could not collect > CMake version: version 3.30.0 > Libc version: glibc-2.35 > > Python version: 3.10.14 (main, May 6 2024, 19:42:50) [GCC 11.2.0] (64-bit runtime) > Python platform: Linux-5.15.153.1-microsoft-standard-WSL2-x86_64-with-glibc2.35 > Is CUDA available: True > CUDA runtime version: 12.1.105 > CUDA_MODULE_LOADING set to: LAZY > GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4080 Laptop GPU > Nvidia driver version: 556.12 > cuDNN version: Could not collect > HIP runtime version: N/A > MIOpen runtime version: N/A > Is XNNPACK available: True > > CPU: > Architecture: x86_64 > CPU op-mode(s): 32-bit, 64-bit > Address sizes: 39 bits physical, 48 bits virtual > Byte Order: Little Endian > CPU(s): 32 > On-line CPU(s) list: 0-31 > Vendor ID: GenuineIntel > Model name: 13th Gen Intel(R) Core(TM) i9-13900HX > CPU family: 6 > Model: 183 > Thread(s) per core: 2 > Core(s) per soc...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: r current environment > Collecting environment information... > PyTorch version: 2.3.0+cu121 > Is debug build: False > CUDA used to build PyTorch: 12.1 > ROCM used to build PyTorch: N/A > > OS: Ubuntu 22.04.4 LTS (x86_6...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: information... > PyTorch version: 2.3.0+cu121 > Is debug build: False > CUDA used to build PyTorch: 12.1 > ROCM used to build PyTorch: N/A > > OS: Ubuntu 22.04.4 LTS (x86_64) > GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Gemma 2 GPTQ - Complete output via API but incomplete through batch inference bug ### Your current environment > Collecting environment information... > PyTorch version: 2.3.0+cu121 > Is debug build: False > CUDA...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: c abort: Not affected > > Versions of relevant libraries: > [pip3] flashinfer==0.0.8+cu121torch2.3 > [pip3] numpy==1.26.4 > [pip3] nvidia-nccl-cu12==2.20.5 > [pip3] torch==2.3.0 > [pip3] torchvision==0.18.0 > [pip3] tra...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: > Vulnerability Meltdown: Not affected > Vulnerability Mmio stale data: Not affected > Vulnerability Retbleed: Mitigation; Enhanced IBRS > Vulnerability Spec rstack overflow: Not affected > Vulnerability Spec store bypa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
