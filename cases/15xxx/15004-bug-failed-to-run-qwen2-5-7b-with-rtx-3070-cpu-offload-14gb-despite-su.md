# vllm-project/vllm#15004: [Bug]:  Failed to Run Qwen2.5-7B with RTX 3070 & CPU Offload (14GB) Despite Sufficient Theoretical Memory

| 字段 | 值 |
| --- | --- |
| Issue | [#15004](https://github.com/vllm-project/vllm/issues/15004) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  Failed to Run Qwen2.5-7B with RTX 3070 & CPU Offload (14GB) Despite Sufficient Theoretical Memory

### Issue 正文摘录

### Your current environment The output of `python collect_env.py` (vllm) roy@Roy-L:~/projects$ python collect_env.py INFO 03-12 13:15:42 __init__.py:207] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0 Clang version: Could not collect CMake version: version 3.22.1 Libc version: glibc-2.35 Python version: 3.12.9 | packaged by Anaconda, Inc. | (main, Feb 6 2025, 18:56:27) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.167.4-microsoft-standard-WSL2-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.8.61 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 3070 Laptop GPU Nvidia driver version: 572.70 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 16 On-line CPU(s) list: 0-15 Vendor ID: Authen...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: Failed to Run Qwen2.5-7B with RTX 3070 & CPU Offload (14GB) Despite Sufficient Theoretical Memory bug;stale ### Your current environment The output of `python collect_env.py` (vllm) roy@Roy-L:~/projects$ python collect_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: Failed to Run Qwen2.5-7B with RTX 3070 & CPU Offload (14GB) Despite Sufficient Theoretical Memory bug;stale ### Your current environment The output of `python collect_env.py` (vllm) roy@Roy-L:~/projects$ python c...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: xsaveopt xsavec xgetbv1 xsaves clzero xsaveerptr arat npt nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload umip vaes vpclmulqdq rdpid fsrm Virtualization: AMD-V Hypervisor...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Failed to Run Qwen2.5-7B with RTX 3070 & CPU Offload (14GB) Despite Sufficient Theoretical Memory bug;stale ### Your current environment The output of `python collect_env.py` (vllm) roy@Roy-L:~/projects$ python c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: RTX 3070 & CPU Offload (14GB) Despite Sufficient Theoretical Memory bug;stale ### Your current environment The output of `python collect_env.py` (vllm) roy@Roy-L:~/projects$ python collect_env.py INFO 03-12 13:15:42 __i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
