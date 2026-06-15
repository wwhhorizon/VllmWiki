# vllm-project/vllm#4646: [Bug]: Setting best_of and n in SamplingParameters makes the performance of LLaMa3 on GSM8K worse

| 字段 | 值 |
| --- | --- |
| Issue | [#4646](https://github.com/vllm-project/vllm/issues/4646) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Setting best_of and n in SamplingParameters makes the performance of LLaMa3 on GSM8K worse

### Issue 正文摘录

### Your current environment ```text ollecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Rocky Linux 8.8 (Green Obsidian) (x86_64) GCC version: (GCC) 8.5.0 20210514 (Red Hat 8.5.0-18) Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.28 Python version: 3.9.19 (main, Mar 21 2024, 17:11:28) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-4.18.0-477.27.1.el8_8.x86_64-x86_64-with-glibc2.28 Is CUDA available: True CUDA runtime version: 12.3.107 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB GPU 4: NVIDIA A100-SXM4-80GB GPU 5: NVIDIA A100-SXM4-80GB GPU 6: NVIDIA A100-SXM4-80GB GPU 7: NVIDIA A100-SXM4-80GB Nvidia driver version: 545.23.08 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 96 On-line CPU(s) list: 0-95 Thread(s) per core: 2 Core(s) per socket: 24 Sock...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: urrent environment ```text ollecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Rocky Linux 8.8 (Green Obsidian) (x...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: best_of and n in SamplingParameters makes the performance of LLaMa3 on GSM8K worse bug;stale ### Your current environment ```text ollecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False C...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: g]: Setting best_of and n in SamplingParameters makes the performance of LLaMa3 on GSM8K worse bug;stale ### Your current environment ```text ollecting environment information... PyTorch version: 2.3.0+cu121 Is debug bu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: in SamplingParameters makes the performance of LLaMa3 on GSM8K worse bug;stale ### Your current environment ```text ollecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to bu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: code that's only slightly adapted from [here](https://docs.vllm.ai/en/latest/getting_started/examples/api_client.html). If I don't set the best_of and n parameter in SamplingParameters, LLaMa 3's accuracy is 74.0. But i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
