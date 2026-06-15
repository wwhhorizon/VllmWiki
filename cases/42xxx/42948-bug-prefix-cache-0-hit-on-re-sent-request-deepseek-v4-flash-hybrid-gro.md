# vllm-project/vllm#42948: [Bug]: Prefix-cache 0% hit on re-sent request — DeepSeek-V4-Flash hybrid groups lose all first-block cache keys on every request reassignment (DSv4 variant of #32802)

| 字段 | 值 |
| --- | --- |
| Issue | [#42948](https://github.com/vllm-project/vllm/issues/42948) |
| 状态 | open |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | attention;cuda;fp8;moe;triton |
| 症状 | build_error;nondeterministic |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Prefix-cache 0% hit on re-sent request — DeepSeek-V4-Flash hybrid groups lose all first-block cache keys on every request reassignment (DSv4 variant of #32802)

### Issue 正文摘录

### Your current environment ``` ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.11.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.13 (main, May 4 2026, 09:06:35) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-6.8.0-100-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 13.0.88 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA H200 NVL GPU 1: NVIDIA H200 NVL Nvidia driver version : 595.71.05 cuDNN version : Could not collect ============================== CPU Info ============================== Architecture: x86_64 CPU(s): 60 Model name: AMD EPYC-Turin Processor Virtua...

## 现有链接修复摘要

#33270 [Bugfix] Fix Hybrid KV cache hit length computation for eagle | #42985 [PoC] Soft-pin recently-hit prefix-cache entries in get_new_blocks | #43302 [KVConnector] Multi-storage replication for shared-prefix KV blocks (fixes #42948 cascade collapse)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Prefix-cache 0% hit on re-sent request — DeepSeek-V4-Flash hybrid groups lose all first-block cache keys on every request reassignment (DSv4 variant of #32802) bug ### Your current environment ``` ===============...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: version : 2.11.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ========================...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: dentical model-side framing precede any user content). For each of the 5 KV-cache groups in the hybrid coordinator, this produces a single-storage entry in `BlockHashToBlockMap._cache` keyed by `BlockHashWithGroupId(sha...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: hit on re-sent request — DeepSeek-V4-Flash hybrid groups lose all first-block cache keys on every request reassignment (DSv4 variant of #32802) bug ### Your current environment ``` ============================== System...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#33270](https://github.com/vllm-project/vllm/pull/33270) | mentioned | 0.45 | [Bugfix] Fix Hybrid KV cache hit length computation for eagle | , merged 2026-02-02. special-cases 1-full+1-swa topology only. - **pr #33270** — referenced in #33524 as an earlier workaround attempt. - **#40902 (v4 roadmap)** — does not curren… |
| [#42985](https://github.com/vllm-project/vllm/pull/42985) | closes_keyword | 0.95 | [PoC] Soft-pin recently-hit prefix-cache entries in get_new_blocks | fix. See "Known limitations" below. ## Motivation Detailed report and instrumentation in **#42948**. Background: #32802 (GPT-OSS hybrid + EAGLE) was closed by #33524 with the |
| [#43302](https://github.com/vllm-project/vllm/pull/43302) | closes_keyword | 0.95 | [KVConnector] Multi-storage replication for shared-prefix KV blocks (fixes #42948 cascade collapse) | fix for the cascade-collapse pathology in #42948, via deliberate multi-storage of shared-prefix KV blocks. This supersedes the protection-based approach in #43191. ### The bug |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
