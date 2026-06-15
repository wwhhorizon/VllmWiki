# vllm-project/vllm#37624: MLA and APC Conflict

| 字段 | 值 |
| --- | --- |
| Issue | [#37624](https://github.com/vllm-project/vllm/issues/37624) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> MLA and APC Conflict

### Issue 正文摘录

### Problem Description There is a conflict between MLA and PagedAttention/APC. This occurs because MLA decouples RoPE. In MLA, RoPE is applied during or after the up-projection from the compressed latent vector ($c_t$). Traditional APC relies on hashing contiguous token blocks where position-in-sequence is baked into the decoupled Key and Value tensors. Matching latent vectors without explicit up-projection is incompatible with this block-hashing mechanism. ### Impact on Compute and TTFT A common perspective is that MLA’s 98% memory compression makes prefix caching unnecessary. However, this separates memory capacity from computational limits. The prefill phase of a 100k-token prompt requires a high amount of FLOPs. By disabling prefix caching to accommodate MLA's memory structure, the engine recomputes dense matrix multiplications for every request. Saving VRAM may be offset if the SMs are fully saturated, which impacts TTFT without APC support for MLA.

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: he compressed latent vector ($c_t$). Traditional APC relies on hashing contiguous token blocks where position-in-sequence is baked into the decoupled Key and Value tensors. Matching latent vectors without explicit up-pr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: . However, this separates memory capacity from computational limits. The prefill phase of a 100k-token prompt requires a high amount of FLOPs. By disabling prefix caching to accommodate MLA's memory structure, the engin...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: he decoupled Key and Value tensors. Matching latent vectors without explicit up-projection is incompatible with this block-hashing mechanism. ### Impact on Compute and TTFT A common perspective is that MLA’s 98% memory...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ut explicit up-projection is incompatible with this block-hashing mechanism. ### Impact on Compute and TTFT A common perspective is that MLA’s 98% memory compression makes prefix caching unnecessary. However, this separ...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
