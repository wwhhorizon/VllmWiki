# vllm-project/vllm#14441: [Usage]: Question about Multimodal token ids on offloaded tokenization

| 字段 | 值 |
| --- | --- |
| Issue | [#14441](https://github.com/vllm-project/vllm/issues/14441) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Question about Multimodal token ids on offloaded tokenization

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86_64) GCC version: (Debian 10.2.1-6) 10.2.1 20210110 Clang version: Could not collect CMake version: version 3.18.4 Libc version: glibc-2.31 Python version: 3.10.16 | packaged by conda-forge | (main, Dec 5 2024, 14:16:10) [GCC 13.3.0] (64-bit runtime) Python platform: Linux-5.10.0-34-cloud-amd64-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 11.8.89 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L4 GPU 1: NVIDIA L4 GPU 2: NVIDIA L4 GPU 3: NVIDIA L4 Nvidia driver version: 550.90.07 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 46 bits physical, 48 bits virtual CPU(s): 48 On-line CPU(s) list: 0-47 Thread(s) per core: 2 Core(s) per socket: 24 Socket(s): 1 NUMA node(s): 1 Vendor ID: GenuineIntel CPU family: 6 Model: 85 Model name: Intel(R) Xeon(R) CPU @ 2.20GHz Stepping: 7 CPU MHz: 220...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: d tokenization usage;stale ### Your current environment ```text PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Usage]: Question about Multimodal token ids on offloaded tokenization usage;stale ### Your current environment ```text PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to bu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: environment ```text PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86_64) GCC version: (Debian 10.2.1-6) 10.2.1 2...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: yncLLMEngine`. We’ve adapted parts of `openai.api_server.py` to optimize latency on a limited GPU cluster, where CPU resources can scale, but GPU pods cannot. We noticed that prompt tokenization is offloaded to the API...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ge]: Question about Multimodal token ids on offloaded tokenization usage;stale ### Your current environment ```text PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
