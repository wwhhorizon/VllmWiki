# vllm-project/vllm#37001: [Bug]: Crash when using PP in multi-node

| 字段 | 值 |
| --- | --- |
| Issue | [#37001](https://github.com/vllm-project/vllm/issues/37001) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Crash when using PP in multi-node

### Issue 正文摘录

### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 3.28.3 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.10.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.18 (main, Jun 4 2025, 08:56:00) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.14.0-27-generic-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.61 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA GeForce RTX 3090 GPU 1: NVIDIA GeForce RTX 3090 GPU 2: NVIDIA GeForce RTX 3090 GPU 3: NVIDIA GeForce RTX 3090 GPU 4: NVIDIA GeForce RTX 3090 GPU 5: NVIDIA GeForce RTX 3090 GPU 6: NVIDIA GeForce RTX 3090 GPU 7: NVIDIA GeForce RTX 3090 Nvidia driver ver...

## 现有链接修复摘要

#41218 fix: convert LogprobsLists to lists for cross node Ray transport (#38602)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: =========== OS : Ubuntu 24.04 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 3.28.3 Libc version : glibc-2.39 =================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.10.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.18...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: in multi-node bug ### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04 LTS (x86_64) GCC version : (Ubuntu 13.3.0-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ed Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Mitigation; Enhanced IBRS V...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: rsions of relevant libraries ============================== [pip3] conch-triton-kernels==1.3 [pip3] flashinfer-python==0.6.4 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41218](https://github.com/vllm-project/vllm/pull/41218) | closes_keyword | 0.95 | fix: convert LogprobsLists to lists for cross node Ray transport (#38602) | fix this case. I tested it before going further. - #29373, #37001: related multi node Ray crashes, different code paths. - #38602: the issue this closes. Bisect data and the experi |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
