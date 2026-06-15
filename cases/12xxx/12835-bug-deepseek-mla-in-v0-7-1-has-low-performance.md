# vllm-project/vllm#12835: [Bug]: DeepSeek MLA in v0.7.1 has low performance

| 字段 | 值 |
| --- | --- |
| Issue | [#12835](https://github.com/vllm-project/vllm/issues/12835) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error;crash;oom;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek MLA in v0.7.1 has low performance

### Issue 正文摘录

### Your current environment INFO 02-06 10:01:17 __init__.py:183] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Red Hat Enterprise Linux release 8.8 (Ootpa) (x86_64) GCC version: (GCC) 8.5.0 20210514 (Red Hat 8.5.0-18) Clang version: Could not collect CMake version: version 3.20.2 Libc version: glibc-2.28 Python version: 3.12.8 | packaged by conda-forge | (main, Dec 5 2024, 14:24:40) [GCC 13.3.0] (64-bit runtime) Python platform: Linux-4.18.0-477.81.1.el8_8.x86_64-x86_64-with-glibc2.28 Is CUDA available: True CUDA runtime version: 12.6.85 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA H100 80GB HBM3 Nvidia driver version: 560.35.05 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 96 On-line CPU(s) list: 0-95 Thread(s) per core: 1 Core(s) per socket: 48 Socket(s): 2 NUMA node(s): 2 Vendor ID: GenuineIntel CPU family: 6 Model: 143 Model name: Intel(R) Xe...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ly detected platform cuda. Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Red Hat Enterprise Linux release 8...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: _occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme avx512_vpo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: nt INFO 02-06 10:01:17 __init__.py:183] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: _.py:183] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Red Hat Enter...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: DeepSeek MLA in v0.7.1 has low performance bug;stale ### Your current environment INFO 02-06 10:01:17 __init__.py:183] Automatically detected platform cuda. Collecting environment information... PyTorch version:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
