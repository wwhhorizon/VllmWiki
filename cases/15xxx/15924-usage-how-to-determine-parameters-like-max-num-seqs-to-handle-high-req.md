# vllm-project/vllm#15924: [Usage]: How to Determine parameters Like `max_num_seqs` to Handle High Request Throughput Faster?

| 字段 | 值 |
| --- | --- |
| Issue | [#15924](https://github.com/vllm-project/vllm/issues/15924) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to Determine parameters Like `max_num_seqs` to Handle High Request Throughput Faster?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Rocky Linux release 9.4 (Blue Onyx) (x86_64) GCC version: (GCC) 11.4.1 20231218 (Red Hat 11.4.1-3) Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.34 Python version: 3.10.0 (default, Mar 3 2022, 09:58:08) [GCC 7.5.0] (64-bit runtime) Python platform: Linux-5.14.0-427.20.1.el9_4.0.1.x86_64-x86_64-with-glibc2.34 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 40 On-line CPU(s) list: 0-39 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz CPU family: 6 Model: 85 Thread(s) per core: 1 Core(s) per socket: 20 Socket(s): 2 Stepping: 7 CPU(s) scaling MHz: 99% CPU max MHz: 3900.0000 CPU mi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: rrent environment ```text The output of `python collect_env.py` PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Rocky Linux release 9.4 (Blue Onyx)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ython collect_env.py` PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Rocky Linux release 9.4 (Blue Onyx) (x86_64) GCC version: (GCC) 11.4.1 202312...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNN...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: How to Determine parameters Like `max_num_seqs` to Handle High Request Throughput Faster? usage;stale ### Your current environment ```text The output of `python collect_env.py` PyTorch version: 2.6.0+cu124 Is d...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: : How to Determine parameters Like `max_num_seqs` to Handle High Request Throughput Faster? usage;stale ### Your current environment ```text The output of `python collect_env.py` PyTorch version: 2.6.0+cu124 Is debug bu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
