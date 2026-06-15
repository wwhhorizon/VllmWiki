# vllm-project/vllm#40807: [Bug]: TurboQuant KV + spec-decode + chunked-prefill crashes CUDA graph capture at query_start_loc.tolist() in continuation-prefill path (Qwen3-Next hybrid dense)

| 字段 | 值 |
| --- | --- |
| Issue | [#40807](https://github.com/vllm-project/vllm/issues/40807) |
| 状态 | open |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;scheduler_memory;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | attention;cache;cuda;moe;operator;quantization;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: TurboQuant KV + spec-decode + chunked-prefill crashes CUDA graph capture at query_start_loc.tolist() in continuation-prefill path (Qwen3-Next hybrid dense)

### Issue 正文摘录

### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.11.0+cu129 Is debug build : False CUDA used to build PyTorch : 12.9 ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.13 (main, Mar 4 2026, 09:23:07) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-6.8.0-110-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.9.86 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA GeForce RTX 3090 GPU 1: NVIDIA GeForce RTX 3090 Nvidia driver version : 595.58.03 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True =============...

## 现有链接修复摘要

#39931 [Feature] TurboQuant: support hybrid models and uniform quantization | #40092 [TurboQuant] enable FA3/FA4 for prefill paths | #43747 [Bugfix][TurboQuant] Fix CUDA graph capture crash with spec-decode + chunked-prefill (#40807)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ===== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ====
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Bug]: TurboQuant KV + spec-decode + chunked-prefill crashes CUDA graph capture at query_start_loc.tolist() in continuation-prefill path (Qwen3-Next hybrid dense) bug ### Your current environment Collecting environment...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: graph capture at query_start_loc.tolist() in continuation-prefill path (Qwen3-Next hybrid dense) bug ### Your current environment Collecting environment information... ============================== System Info ========...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: TurboQuant KV + spec-decode + chunked-prefill crashes CUDA graph capture at query_start_loc.tolist() in continuation-prefill path (Qwen3-Next hybrid dense) bug ### Your current environment Collecting environment...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.7 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.9.1.4 [pip3] nvidia-cuda-cupti-cu12==12.9.79 [pip3] nvidia-cuda-nvrtc-cu12=...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39931](https://github.com/vllm-project/vllm/pull/39931) | mentioned | 0.45 | [Feature] TurboQuant: support hybrid models and uniform quantization | qwen3.6-35b-a3b (moe hybrid) once the arg_utils gate is lifted via #39931 or similar ### why this matters downstream [`lorbus/qwen3.6-27b-int4-autoround`](https://huggingface.co |
| [#40092](https://github.com/vllm-project/vllm/pull/40092) | mentioned | 0.45 | [TurboQuant] enable FA3/FA4 for prefill paths | nto the continuation branch and hitting the `.tolist()` sync. pr #40092 unblocked the eager-ok test matrix but left the spec-dec + chunked-prefill combination blocked. ### minima |
| [#43747](https://github.com/vllm-project/vllm/pull/43747) | closes_keyword | 0.95 | [Bugfix][TurboQuant] Fix CUDA graph capture crash with spec-decode + chunked-prefill (#40807) | fixes Layer 1 (the `.tolist()` crash) which had **no open PR**. ## Related Issues - #40807 — primary issue (this PR) - #40880 — MTP × TurboQuant × CUDA graph degenerate output (c |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
