# vllm-project/vllm#35313: [Bug]: vLLM startup memory check mis-detects available VRAM (reclaimable OS memory) on UMA Systems

| 字段 | 值 |
| --- | --- |
| Issue | [#35313](https://github.com/vllm-project/vllm/issues/35313) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM startup memory check mis-detects available VRAM (reclaimable OS memory) on UMA Systems

### Issue 正文摘录

### 🐛 Describe the bug ## Issue Observed on UMA GPUs (DGX Spark and GH200) I have observed this bug on both **DGX Spark** and **GH200** systems. ### Problem Description vLLM defaults to requesting 90% GPU memory utilization (`--gpu-memory-utilization=0.9`). While it's typically easier to achieve 90% free memory on non-UMA systems, on UMA systems the memory can be occupied by **paged cache and buffers which are reclaimable** by the OS. Instead of accounting for this reclaimable memory, vLLM fails with: ``` ValueError: Free memory on device cuda:0 (74.9/142.5 GiB) on startup is less than desired GPU memory utilization (0.9, 128.25 GiB). Decrease GPU memory utilization or reduce GPU memory used by other processes. ``` ### Root Cause On UMA systems, `cudaMemGetInfo` (which vLLM uses via pynvml) doesn't account for memory that could be reclaimed from the OS (page cache, SWAP, buffers). This causes vLLM to underestimate available GPU memory during deployment, leading to false failures even when sufficient memory would be available after OS-level reclamation. ### Affected Systems - DGX Spark (GB10) - GH200 - Other UMA Systems ### Workarounds - Reduce `--gpu-memory-utilization` below 0.9...

## 现有链接修复摘要

#35356 [Bugfix] Use is_integrated to detect UMA GPUs for memory reporting

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: park** and **GH200** systems. ### Problem Description vLLM defaults to requesting 90% GPU memory utilization (`--gpu-memory-utilization=0.9`). While it's typically easier to achieve 90% free memory on non-UMA systems, o...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e GPU memory during deployment, leading to false failures even when sufficient memory would be available after OS-level reclamation. ### Affected Systems - DGX Spark (GB10) - GH200 - Other UMA Systems ### Workarounds -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: laimable memory, vLLM fails with: ``` ValueError: Free memory on device cuda:0 (74.9/142.5 GiB) on startup is less than desired GPU memory utilization (0.9, 128.25 GiB). Decrease GPU memory utilization or reduce GPU mem...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: 200** systems. ### Problem Description vLLM defaults to requesting 90% GPU memory utilization (`--gpu-memory-utilization=0.9`). While it's typically easier to achieve 90% free memory on non-UMA systems, on UMA systems t...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: LM to underestimate available GPU memory during deployment, leading to false failures even when sufficient memory would be available after OS-level reclamation. ### Affected Systems - DGX Spark (GB10) - GH200 - Other UM...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35356](https://github.com/vllm-project/vllm/pull/35356) | closes_keyword | 0.95 | [Bugfix] Use is_integrated to detect UMA GPUs for memory reporting | Fixes #35313. On UMA (Unified Memory Architecture) systems like GH200, DGX Spark, and Jetson Orin, `cudaMemGetInfo` doesn't account for reclaimable OS memory (page cache, buffers) |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
