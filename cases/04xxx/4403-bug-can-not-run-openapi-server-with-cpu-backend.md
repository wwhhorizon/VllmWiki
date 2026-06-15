# vllm-project/vllm#4403: [Bug]: Can not run openapi server with cpu backend

| 字段 | 值 |
| --- | --- |
| Issue | [#4403](https://github.com/vllm-project/vllm/issues/4403) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Can not run openapi server with cpu backend

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.2.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Fedora Linux 40 (Workstation Edition) (x86_64) GCC version: (GCC) 14.0.1 20240411 (Red Hat 14.0.1-0) Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.39 Python version: 3.11.8 (main, Feb 28 2024, 00:00:00) [GCC 14.0.1 20240217 (Red Hat 14.0.1-0)] (64-bit runtime) Python platform: Linux-6.8.7-300.fc40.x86_64-x86_64-with-glibc2.39 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 39 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 16 On-line CPU(s) list: 0-15 Vendor ID: GenuineIntel Model name: 11th Gen Intel(R) Core(TM) i7-11850H @ 2.50GHz CPU family: 6 Model: 141 Thread(s) per core: 2 Core(s) per socket: 8 Socket(s): 1 Stepping: 1 CPU(s) scaling MHz: 29% CPU max MH...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: rrent environment ```text Collecting environment information... PyTorch version: 2.2.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Fedora Linux 40 (Workstation Edition)...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: ed Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not affecte...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ironment information... PyTorch version: 2.2.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Fedora Linux 40 (Workstation Edition) (x86_64) GCC version: (GCC) 14.0.1 2024...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='outlines', worker_use_ray=False, p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ckend bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.2.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Fedora Linux 40...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
