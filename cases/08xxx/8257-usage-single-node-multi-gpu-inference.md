# vllm-project/vllm#8257: [Usage]: Single-node multi-GPU inference

| 字段 | 值 |
| --- | --- |
| Issue | [#8257](https://github.com/vllm-project/vllm/issues/8257) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Single-node multi-GPU inference

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Red Hat Enterprise Linux 9.4 (Plow) (x86_64) GCC version: (GCC) 11.4.1 20231218 (Red Hat 11.4.1-3) Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.34 Python version: 3.10.14 (main, May 6 2024, 19:42:50) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.14.0-427.22.1.el9_4.x86_64-x86_64-with-glibc2.34 Is CUDA available: True CUDA runtime version: 12.5.40 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA H100 80GB HBM3 GPU 1: NVIDIA H100 80GB HBM3 GPU 2: NVIDIA H100 80GB HBM3 GPU 3: NVIDIA H100 80GB HBM3 GPU 4: NVIDIA H100 80GB HBM3 GPU 5: NVIDIA H100 80GB HBM3 GPU 6: NVIDIA H100 80GB HBM3 GPU 7: NVIDIA H100 80GB HBM3 Nvidia driver version: 555.42.02 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 57 bits virtual Byte Order: Little Endian CPU(s): 96 On-line CPU(s) list: 0-95 Vendor ID: GenuineIntel Model n...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: -GPU inference usage;stale ### Your current environment ```text PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Red Hat Enterprise Linux 9.4 (Plow)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: environment ```text PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Red Hat Enterprise Linux 9.4 (Plow) (x86_64) GCC version: (GCC) 11.4.1 20231218...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: _occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme avx512_vpo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: True CUDA runtime version: 12.5.40 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA H100 80GB HBM3 GPU 1: NVIDIA H100 80GB HBM3 GPU 2: NVIDIA H100 80GB HBM3 GPU 3: NVIDIA H100 80GB HBM3 GPU 4...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Usage]: Single-node multi-GPU inference usage;stale ### Your current environment ```text PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Red Hat E...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
