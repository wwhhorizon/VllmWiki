# vllm-project/vllm#37096: [Bug]: v0.17.0-aarch64 onwards will run out of CUDA memory for gpt-oss-120b on GH200 144GB

| 字段 | 值 |
| --- | --- |
| Issue | [#37096](https://github.com/vllm-project/vllm/issues/37096) |
| 状态 | open |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.17.0-aarch64 onwards will run out of CUDA memory for gpt-oss-120b on GH200 144GB

### Issue 正文摘录

### Your current environment I am running vLLM docker image, so some of the information below does not apply: ``` Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.4 LTS (aarch64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0 Clang version : Could not collect CMake version : version 3.28.3 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cu129 Is debug build : False CUDA used to build PyTorch : 12.9 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.7 | packaged by Anaconda, Inc. | (main, Oct 4 2024, 13:17:02) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-6.8.0-1049-nvidia-64k-aarch64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.9.86 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA GH200 144G HBM3e GPU 1: NVIDIA GH200 144G HBM3e Nvidia driver version : 575.57.08 cuDNN version : Probably one of the foll...

## 现有链接修复摘要

#37111 [Bugfix] Fix OOM caused by cumem allocator inflating memory_reserved()

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: -120b on GH200 144GB bug ### Your current environment I am running vLLM docker image, so some of the information below does not apply: ``` Collecting environment information... ============================== System Info...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 9: p sve2 sveaes svepmull svebitperm svesha3 svesm4 flagm2 frint svei8mm svebf16 i8mm bf16 dgh bti L1d cache: 9 MiB (144 instances) L1i cache: 9 MiB (144 instances) L2 cache: 144 MiB (144 instances) L3 cac
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 7: ant libraries ============================== [pip3] flake8==7.3.0 [pip3] flashinfer-python==0.5.2 [pip3] mypy==1.11.2 [pip3] mypy-extensions==1.0.0 [pip3] numpy==1.26.4 [pip3] numpydoc==1.7.0 [pip3] onnx==1.18.0 [pip3]...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: v0.17.0-aarch64 onwards will run out of CUDA memory for gpt-oss-120b on GH200 144GB bug ### Your current environment I am running vLLM docker image, so some of the information below does not apply: ``` Collecting...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: r pid=1) INFO 03-15 05:40:46 [cache.py:214] Using fp8 data type to store kv cache. It reduces the GPU memory footprint and boosts the performance. Meanwhile, it may cause accuracy drop without a proper scaling factor. (...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37111](https://github.com/vllm-project/vllm/pull/37111) | closes_keyword | 0.95 | [Bugfix] Fix OOM caused by cumem allocator inflating memory_reserved() | Fixes #37096 ## Test Plan - Added `test_memory_profiling_persistent_torch` to verify persistent torch allocations are not double-counted in `non_kv_cache_memory`. - E2E verificat |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
