# vllm-project/vllm#42404: [Bug]: expandable_segments:True rejected with SimpleCPUOffloadConnector — no opt-in mechanism for DMA-only connectors

| 字段 | 值 |
| --- | --- |
| Issue | [#42404](https://github.com/vllm-project/vllm/issues/42404) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: expandable_segments:True rejected with SimpleCPUOffloadConnector — no opt-in mechanism for DMA-only connectors

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug PR #41237 added a blanket rejection of **all** KV connectors when `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` is set (unless `--enable-sleep-mode` is also enabled). The reasoning is correct for RDMA-based connectors like `NixlConnector` and `MooncakeConnectorV1` — VMM can remap KV cache pages, invalidating registered memory regions. However, `SimpleCPUOffloadConnector` uses **DMA (memcpy via `torch.cat`/tensor slicing)** — not RDMA or pinned memory registrations. These operations go through the CUDA allocator and are transparent to VMM remapping. The blanket rejection is a false positive for this connector. **Impact:** Users on memory-constrained GPUs (12–24 GiB) who need both: - KV cache offloading to CPU (to serve models whose weights barely fit in VRAM) - `expandable_segments:True` (to reduce memory fragmentation and avoid OOM during prefill) …are blocked with no workaround. Sleep mode (`--enable-sleep-mode`) adds ~868 MiB/GPU overhead for CuMemAllocator pools, which is too much for already-tight memory budgets. **Reproduction:** ```bash PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \ python3 -m vllm.entrypoints.open...

## 现有链接修复摘要

#41237 [Bugfix][KV Transfer] Reject NixlConnector + expandable_segments:True | #42405 [Bugfix][KV Transfer] Allow DMA-only connectors with expandable_segments:True

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: [Bug]: expandable_segments:True rejected with SimpleCPUOffloadConnector — no opt-in mechanism for DMA-only connectors ### Your current environment ### 🐛 Describe the bug PR #41237 added a blanket rejection of **all** KV...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: `SimpleCPUOffloadConnector` uses **DMA (memcpy via `torch.cat`/tensor slicing)** — not RDMA or pinned memory registrations. These operations go through the CUDA allocator and are transparent to VMM remapping. The blanke...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: se operations go through the CUDA allocator and are transparent to VMM remapping. The blanket rejection is a false positive for this connector. **Impact:** Users on memory-constrained GPUs (12–24 GiB) who need both: - K...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: d GPUs (12–24 GiB) who need both: - KV cache offloading to CPU (to serve models whose weights barely fit in VRAM) - `expandable_segments:True` (to reduce memory fragmentation and avoid OOM during prefill) …are blocked w...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: able_segments:True` (to reduce memory fragmentation and avoid OOM during prefill) …are blocked with no workaround. Sleep mode (`--enable-sleep-mode`) adds ~868 MiB/GPU overhead for CuMemAllocator pools, which is too muc...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41237](https://github.com/vllm-project/vllm/pull/41237) | mentioned | 0.45 | [Bugfix][KV Transfer] Reject NixlConnector + expandable_segments:True | on gpu, kv on cpu" pattern), #19854 (canonical kv offloading rfc), pr #41237 (source of blanket rejection) |
| [#42405](https://github.com/vllm-project/vllm/pull/42405) | closes_keyword | 0.95 | [Bugfix][KV Transfer] Allow DMA-only connectors with expandable_segments:True | Closes #42404 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
