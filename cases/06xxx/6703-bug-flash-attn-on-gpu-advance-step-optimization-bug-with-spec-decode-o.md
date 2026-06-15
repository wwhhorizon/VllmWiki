# vllm-project/vllm#6703: [Bug]: Flash-attn on-GPU advance step optimization bug with spec decode on LLama 405B

| 字段 | 值 |
| --- | --- |
| Issue | [#6703](https://github.com/vllm-project/vllm/issues/6703) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Flash-attn on-GPU advance step optimization bug with spec decode on LLama 405B

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.1 Libc version: glibc-2.35 Python version: 3.10.12 (main, Mar 22 2024, 16:50:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.0-116-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA H100 80GB HBM3 GPU 1: NVIDIA H100 80GB HBM3 GPU 2: NVIDIA H100 80GB HBM3 GPU 3: NVIDIA H100 80GB HBM3 GPU 4: NVIDIA H100 80GB HBM3 GPU 5: NVIDIA H100 80GB HBM3 GPU 6: NVIDIA H100 80GB HBM3 GPU 7: NVIDIA H100 80GB HBM3 Nvidia driver version: 550.90.07 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 57 bits virtual Byte Order: Little Endian CPU(s): 104 On-line CPU(s) list: 0-103 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R...

## 现有链接修复摘要

#6757 [Bugfix] Fix decode tokens w. CUDA graph

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: c decode on LLama 405B bug ### Your current environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ver...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: Flash-attn on-GPU advance step optimization bug with spec decode on LLama 405B bug ### Your current environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM use...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: _occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme avx512_vpo...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: rent environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#6757](https://github.com/vllm-project/vllm/pull/6757) | closes_keyword | 0.95 | [Bugfix] Fix decode tokens w. CUDA graph | Fixes #6703. This is not related to speculative decoding particularly but not sure why no unit test failed. Will try to add a unit test in this or a follow-up PR. cc @cadedanie |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
