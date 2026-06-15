# vllm-project/vllm#16234: [Bug]: Calling /wake_up after /sleep and then sending a request leads to improper LLM response

| 字段 | 值 |
| --- | --- |
| Issue | [#16234](https://github.com/vllm-project/vllm/issues/16234) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Calling /wake_up after /sleep and then sending a request leads to improper LLM response

### Issue 正文摘录

### Your current environment Please note that I am using the docker image directly and generated the log by logging in into the Docker container using `docker exec` INFO 04-07 22:57:45 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 4.0.0 Libc version: glibc-2.35 Python version: 3.12.9 (main, Feb 5 2025, 08:49:00) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-6.8.0-1024-aws-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L4 GPU 1: NVIDIA L4 Nvidia driver version: 550.144.03 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 48 On-line CPU(s) list: 0-47 Vendor ID: AuthenticAMD...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: sponse bug ### Your current environment Please note that I am using the docker image directly and generated the log by logging in into the Docker container using `docker exec` INFO 04-07 22:57:45 [__init__.py:239] Autom...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: _.py:239] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ` INFO 04-07 22:57:45 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Calling /wake_up after /sleep and then sending a request leads to improper LLM response bug ### Your current environment Please note that I am using the docker image directly and generated the log by logging in i...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: async abort: Not affected Versions of relevant libraries: [pip3] flashinfer-python==0.2.1.post2+cu124torch2.6 [pip3] numpy==2.1.3 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda-cupti-cu12==12.4.127 [pip3] nvidia...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
