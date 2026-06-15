# vllm-project/vllm#6774: [Bug]: --max-model-len configuration robustness

| 字段 | 值 |
| --- | --- |
| Issue | [#6774](https://github.com/vllm-project/vllm/issues/6774) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: --max-model-len configuration robustness

### Issue 正文摘录

### Your current environment bash-5.1# python collect_env.py Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Oracle Linux Server 9.4 (x86_64) GCC version: (GCC) 11.4.1 20231218 (Red Hat 11.4.1-3.0.1) Clang version: Could not collect CMake version: version 3.30.1 Libc version: glibc-2.34 Python version: 3.11.9 (main, Apr 19 2024, 16:48:06) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-203.146.5.1.el8uek.x86_64-x86_64-with-glibc2.34 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A10 GPU 1: NVIDIA A10 GPU 2: NVIDIA A10 GPU 3: NVIDIA A10 Nvidia driver version: 535.154.05 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 57 bits virtual Byte Order: Little Endian CPU(s): 128 On-line CPU(s) list: 0-127 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) Platinum 8358 CPU @ 2.60GHz CPU family: 6 Model: 106 Thread(s) per cor...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: 5.1# python collect_env.py Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Oracle Linux Server 9.4 (x86_64) G...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Oracle Linux Server 9.4 (x86_64) GCC version: (GCC) 11.4.1 20231218 (Red Hat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: --max-model-len configuration robustness bug;stale ### Your current environment bash-5.1# python collect_env.py Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: --max-model-len configuration robustness bug;stale ### Your current environment bash-5.1# python collect_env.py Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rch==2.3.1 [pip3] torchvision==0.18.1 [pip3] transformers==4.43.1 [pip3] triton==2.3.1 [conda] blas 1.0 mkl [conda] mkl 2023.1.0 h213fc3f_46344 [conda] nccl 2.22.3.1 hbc370b7_0 c

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
