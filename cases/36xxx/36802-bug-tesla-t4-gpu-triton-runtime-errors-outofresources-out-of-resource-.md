# vllm-project/vllm#36802: [Bug]: Tesla T4 GPU - triton.runtime.errors.OutOfResources: out of resource: shared memory, Required: 81920, Hardware limit: 65536. Reducing block sizes or `num_stages`

| 字段 | 值 |
| --- | --- |
| Issue | [#36802](https://github.com/vllm-project/vllm/issues/36802) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Tesla T4 GPU - triton.runtime.errors.OutOfResources: out of resource: shared memory, Required: 81920, Hardware limit: 65536. Reducing block sizes or `num_stages`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug This is how i try to load the model. The server starts succesfully. When i use curl to send prompt. Server crash. ``` !VLLM_USE_V1=0 vllm serve "nvidia/Nemotron-Content-Safety-Reasoning-4B" \ --tensor-parallel-size 4 \ --gpu-memory-utilization 0.8 \ --max-model-len 4096 \ --port 8000 \ --host 0.0.0.0 \ --enforce-eager ``` ``` Wed Mar 11 15:46:59 2026 +---------------------------------------------------------------------------------------+ | NVIDIA-SMI 535.161.07 Driver Version: 535.161.07 CUDA Version: 12.2 | |-----------------------------------------+----------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+======================+======================| | 0 Tesla T4 Off | 00000001:00:00.0 Off | Off | | N/A 26C P8 13W / 70W | 2MiB / 16384MiB | 0% Default | | | | N/A | +-----------------------------------------+----------------------+----------------------+ | 1 Tesla T4 Off | 00000002:00:00.0 Off | Off | | N/A 25C P8 9W / 70W | 2MiB / 16384MiB | 0% Def...

## 现有链接修复摘要

#43044 [Core] Add shmem-aware autotune pruner for non-H100 Triton kernels | #43047 [Core] Add shmem-aware autotune pruner for non-H100 Triton kernels

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: of resource: shared memory, Required: 81920, Hardware limit: 65536. Reducing block sizes or `num_stages` bug ### Your current environment ### 🐛 Describe the bug This is how i try to load the model. The server starts suc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: --------------------------------------------------------------+ | NVIDIA-SMI 535.161.07 Driver Version: 535.161.07 CUDA Version: 12.2 | |-----------------------------------------+----------------------+-----------------...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Tesla T4 GPU - triton.runtime.errors.OutOfResources: out of resource: shared memory, Required: 81920, Hardware limit: 65536. Reducing block sizes or `num_stages` bug ### Your current environment ### 🐛 Describe th...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: esource: shared memory, Required: 81920, Hardware limit: 65536. Reducing block sizes or `num_stages` bug ### Your current environment ### 🐛 Describe the bug This is how i try to load the model. The server starts succesf...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: PU GI CI PID Type Process name GPU Memory | | ID ID Usage | |=======================================================================================| | No running processes fou

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43044](https://github.com/vllm-project/vllm/pull/43044) | mentioned | 0.6 | [Core] Add shmem-aware autotune pruner for non-H100 Triton kernels | alidation below). Partially addresses the same root cause in #38918, #36802, #41063, #32826. ### Motivation Triton kernels in vLLM often ship with autotune config lists tuned for… |
| [#43047](https://github.com/vllm-project/vllm/pull/43047) | mentioned | 0.6 | [Core] Add shmem-aware autotune pruner for non-H100 Triton kernels | alidation below). Partially addresses the same root cause in #38918, #36802, #41063, #32826. ### Motivation Triton kernels in vLLM often ship with autotune config lists tuned for… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
