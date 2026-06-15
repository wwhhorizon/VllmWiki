# vllm-project/vllm#13099: [Bug]: Is vllm still support passing max_pixels and min_pixels for Qwen2VL?

| 字段 | 值 |
| --- | --- |
| Issue | [#13099](https://github.com/vllm-project/vllm/issues/13099) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cache;cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Is vllm still support passing max_pixels and min_pixels for Qwen2VL?

### Issue 正文摘录

### Your current environment INFO 02-12 00:04:31 __init__.py:190] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.22.1 Libc version: glibc-2.35 Python version: 3.10.16 (main, Dec 11 2024, 16:24:50) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-43-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A800 80GB PCIe GPU 1: NVIDIA A800 80GB PCIe GPU 2: NVIDIA A800 80GB PCIe GPU 3: NVIDIA A800 80GB PCIe Nvidia driver version: 535.86.05 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 52 bits physical, 57 bits virtual Byte Order: Little Endian CPU(s): 160 On-line CPU(s) list: 0-159 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) Platinum 8...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ly detected platform cuda. Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC ve...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Is vllm still support passing max_pixels and min_pixels for Qwen2VL? bug ### Your current environment INFO 02-12 00:04:31 __init__.py:190] Automatically detected platform cuda. Collecting environment information....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: INFO 02-12 00:04:31 __init__.py:190] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyT...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e, gpu_memory_utilization=self.args.vllm_gpu_memory_utilization, dtype=torch.bfloat16, # Automatic Prefix Caching caches the KV cache of existing queries, so that a new query can # directly reuse the KV cache if it shar...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ffected Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and secc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
