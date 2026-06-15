# vllm-project/vllm#14432: [usage]:Cuda out of memory while loading the quantized model

| 字段 | 值 |
| --- | --- |
| Issue | [#14432](https://github.com/vllm-project/vllm/issues/14432) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [usage]:Cuda out of memory while loading the quantized model

### Issue 正文摘录

### Your current environment ``collect_env.py 100%[============================================================>] 25.64K --.-KB/s in 0.009s 2025-03-07 15:32:12 (2.72 MB/s) - ‘collect_env.py’ saved [26257/26257] Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.1 LTS (x86_64) GCC version: (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.39 Python version: 3.12.3 (main, Feb 4 2025, 14:48:35) [GCC 13.3.0] (64-bit runtime) Python platform: Linux-6.8.0-52-generic-x86_64-with-glibc2.39 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4060 Nvidia driver version: 550.120 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 12 On-line CPU(s) list: 0-11 Vendor ID: GenuineIntel Model name: Intel(R)...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: v.py’ saved [26257/26257] Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.1 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [usage]:Cuda out of memory while loading the quantized model usage;stale ### Your current environment ``collect_env.py 100%[============================================================>] 25.64K --.-KB/s
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [usage]:Cuda out of memory while loading the quantized model usage;stale ### Your current environment ``collect_env.py 100%[============================================================>] 25.64K --.-KB/s in 0.009s 2025-0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [usage]:Cuda out of memory while loading the quantized model usage;stale ### Your current environment ``collect_env.py 100%[============================================================>] 25.64K --.-KB/s in 0.009s 2025-0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [usage]:Cuda out of memory while loading the quantized model usage;stale ### Your current environment ``collect_env.py 100%[============================================================>] 25.64K --.-KB/s in 0.009s 2025-0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
