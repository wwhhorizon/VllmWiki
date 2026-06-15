# vllm-project/vllm#7940: [Bug]: RuntimeError: operator torchvision::nms does not exist

| 字段 | 值 |
| --- | --- |
| Issue | [#7940](https://github.com/vllm-project/vllm/issues/7940) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: operator torchvision::nms does not exist

### Issue 正文摘录

### Your current environment Collecting environment information... INFO 08-28 14:32:56 importing.py:10] Triton not installed; certain GPU-related functions will not be available. WARNING 08-28 14:32:56 _custom_ops.py:17] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch version: 2.4.0+cpu Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (GCC) 12.2.0 Clang version: Could not collect CMake version: version 3.26.0 Libc version: glibc-2.31 Python version: 3.10.14 (main, May 6 2024, 19:42:50) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.4.0-26-generic-x86_64-with-glibc2.31 Is CUDA available: False CUDA runtime version: 10.1.243 CUDA_MODULE_LOADING set to: N/A GPU models and configuration: Could not collect Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 52 bits physical, 57 bits virtual CPU(s): 192 On-line CPU(s) list: 0-191 Thread(s) per c...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: t environment Collecting environment information... INFO 08-28 14:32:56 importing.py:10] Triton not installed; certain GPU-related functions will not be available. WARNING 08-28 14:32:56 _custom_ops.py:17] Failed to imp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: odule named 'vllm._C'") PyTorch version: 2.4.0+cpu Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (GCC) 12.2.0 Clang vers...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: t exist bug;stale ### Your current environment Collecting environment information... INFO 08-28 14:32:56 importing.py:10] Triton not installed; certain GPU-related functions will not be available. WARNING 08-28 14:32:56...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: llecting environment information... INFO 08-28 14:32:56 importing.py:10] Triton not installed; certain GPU-related functions will not be available. WARNING 08-28 14:32:56 _custom_ops.py:17] Failed to import from vllm._C...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local avx512_bf16 wbnoinvd dtherm ida arat pln pts avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme avx512_vpop...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
