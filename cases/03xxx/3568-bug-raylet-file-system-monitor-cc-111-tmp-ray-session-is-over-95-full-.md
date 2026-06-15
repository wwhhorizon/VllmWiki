# vllm-project/vllm#3568: [Bug]: (raylet) file_system_monitor.cc:111: /tmp/ray/session_ is over 95% full, Object creation will fail if spilling is required.

| 字段 | 值 |
| --- | --- |
| Issue | [#3568](https://github.com/vllm-project/vllm/issues/3568) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: (raylet) file_system_monitor.cc:111: /tmp/ray/session_ is over 95% full, Object creation will fail if spilling is required.

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86_64) GCC version: (Debian 10.2.1-6) 10.2.1 20210110 Clang version: Could not collect CMake version: version 3.18.4 Libc version: glibc-2.31 Python version: 3.10.13 | packaged by conda-forge | (main, Dec 23 2023, 15:36:39) [GCC 12.3.0] (64-bit runtime) Python platform: Linux-5.10.0-27-cloud-amd64-x86_64-with-glibc2.31 Is CUDA available: N/A CUDA runtime version: 11.8.89 CUDA_MODULE_LOADING set to: N/A GPU models and configuration: GPU 0: NVIDIA L4 GPU 1: NVIDIA L4 GPU 2: NVIDIA L4 GPU 3: NVIDIA L4 GPU 4: NVIDIA L4 GPU 5: NVIDIA L4 GPU 6: NVIDIA L4 GPU 7: NVIDIA L4 Nvidia driver version: 525.105.17 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: N/A CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 46 bits physical, 48 bits virtual CPU(s): 96 On-line CPU(s) list: 0-95 Thread(s) per core: 2 Core(s) per socket: 24 Socket(s): 2 NUMA node(s): 2 Vendor ID: GenuineIntel CPU f...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: Your current environment Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86_64) GCC version: (Debian 10.2.1-6) 10.2.1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: quired. bug;stale ### Your current environment Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bull...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=8, max_parallel_load...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: is over 95% full, Object creation will fail if spilling is required. bug;stale ### Your current environment Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
