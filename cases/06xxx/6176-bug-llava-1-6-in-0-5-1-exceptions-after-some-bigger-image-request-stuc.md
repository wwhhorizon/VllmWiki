# vllm-project/vllm#6176: [Bug]: LLaVA 1.6 in 0.5.1: Exceptions after some bigger image request, stuck in faulty mode

| 字段 | 值 |
| --- | --- |
| Issue | [#6176](https://github.com/vllm-project/vllm/issues/6176) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;quantization;sampling |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LLaVA 1.6 in 0.5.1: Exceptions after some bigger image request, stuck in faulty mode

### Issue 正文摘录

### Your current environment ```text PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-6.5.0-35-generic-x86_64-with-glibc2.35 Is CUDA available: N/A CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: N/A GPU models and configuration: GPU 0: NVIDIA L40 GPU 1: NVIDIA L40 GPU 2: NVIDIA L40 GPU 3: NVIDIA L40 Nvidia driver version: 535.161.08 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: N/A CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 57 bits virtual Byte Order: Little Endian CPU(s): 128 On-line CPU(s) list: 0-127 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) Gold 6438Y+ CPU family: 6 Model: 143 Thread(s) per core: 2 Core(s) per socket: 32 Socket(s): 2 Stepping: 8 BogoMIPS: 4000.00 Flags: fpu vme de pse tsc msr pae mce cx8 api...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: , stuck in faulty mode bug ### Your current environment ```text PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubun...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: A runtime version: Could not collect CUDA_MODULE_LOADING set to: N/A GPU models and configuration: GPU 0: NVIDIA L40 GPU 1: NVIDIA L40 GPU 2: NVIDIA L40 GPU 3: NVIDIA L40 Nvidia driver version: 535.161.08 cuDNN version:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ur current environment ```text PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: LLaVA 1.6 in 0.5.1: Exceptions after some bigger image request, stuck in faulty mode bug ### Your current environment ```text PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: _occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts hfi vnmi avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
