# vllm-project/vllm#40121: [Bug]: CUDA graph replay triggers Xid 13 illegal memory access on Qwen3-32B-AWQ with TP=2 on dual RTX 3090

| 字段 | 值 |
| --- | --- |
| Issue | [#40121](https://github.com/vllm-project/vllm/issues/40121) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA graph replay triggers Xid 13 illegal memory access on Qwen3-32B-AWQ with TP=2 on dual RTX 3090

### Issue 正文摘录

### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.10.0+cu129 Is debug build : False CUDA used to build PyTorch : 12.9 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.13 (main, Mar 4 2026, 09:23:07) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-6.8.0-107-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.9.86 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA GeForce RTX 3090 GPU 1: NVIDIA GeForce RTX 3090 Nvidia driver version : 580.126.20 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info ====...

## 现有链接修复摘要

#40385 compilation: cap cudagraph sizes for TP Marlin on Ampere

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Bug]: CUDA graph replay triggers Xid 13 illegal memory access on Qwen3-32B-AWQ with TP=2 on dual RTX 3090 bug ### Your current environment Collecting environment information... ============================== System In
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: CUDA graph replay triggers Xid 13 illegal memory access on Qwen3-32B-AWQ with TP=2 on dual RTX 3090 bug ### Your current environment Collecting environment information... ============================== System Inf...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Mitigation; untrained return thunk; SMT disabled Vulnerability...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.6 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.9.1.4 [pip3] nvidia-cuda-cupti-cu12==12.9.79 [pip3] nvidia-cuda-nvrtc-c...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40385](https://github.com/vllm-project/vllm/pull/40385) | mentioned | 0.6 | compilation: cap cudagraph sizes for TP Marlin on Ampere | size` ## Why: - Mitigates CUDA graph replay instability reported in #40121 - Matches known workaround: limiting capture sizes to `<= 8` ## Test: - Adds `test_cudagraph_sizes_cappe… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
