# vllm-project/vllm#10777: [Usage]: how to skip samples that have error and process the rest when using llm.generate(prompts, sampling_params)？

| 字段 | 值 |
| --- | --- |
| Issue | [#10777](https://github.com/vllm-project/vllm/issues/10777) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: how to skip samples that have error and process the rest when using llm.generate(prompts, sampling_params)？

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: 2.5.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Red Hat Enterprise Linux release 8.10 (Ootpa) (x86_64) GCC version: (GCC) 9.2.0 Clang version: Could not collect CMake version: version 3.31.1 Libc version: glibc-2.28 Python version: 3.10.15 (main, Oct 3 2024, 07:27:34) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-4.18.0-553.22.1.el8_10.x86_64-x86_64-with-glibc2.28 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB Nvidia driver version: 560.35.03 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 64 On-line CPU(s) list: 0-63 Thread(s) per core: 1 Core(s) per socket: 32 Socket(s): 2 NUMA node(s): 8 Vendor ID: AuthenticAMD CPU family: 25 Model: 1 Model name: AMD EPYC 7543 32-Core Processor Stepping: 1 CPU MHz: 3706.844 CPU max MHz: 2800.0000 CPU min MHz: 1500.0000 BogoMIPS: 5589.76 Virtualizatio...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: Your current environment Collecting environment information... PyTorch version: 2.5.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Red Hat Enterprise Linux release 8.1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.5.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Red Hat Enterprise Linux release 8.10 (Ootpa) (x86_64) GCC version: (GCC) 9.2...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ams)？ usage;stale ### Your current environment Collecting environment information... PyTorch version: 2.5.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Red Hat Enterp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: rocess the rest when using llm.generate(prompts, sampling_params)？ usage;stale ### Your current environment Collecting environment information... PyTorch version: 2.5.1+cu121 Is debug build: False CUDA used to build PyT...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: u121 [pip3] torchvision==0.20.1+cu121 [pip3] transformers==4.46.3 [pip3] triton==3.1.0 [conda] numpy 1.26.3 pypi_0 pypi [conda] nvidia-cublas-cu12 12.1.3.1 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.1.105

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
