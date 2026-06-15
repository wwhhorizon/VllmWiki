# vllm-project/vllm#44341: [ROCm] Simple CPU offload is slow without hipMemcpyBatchAsync mapping

| 字段 | 值 |
| --- | --- |
| Issue | [#44341](https://github.com/vllm-project/vllm/issues/44341) |
| 状态 | open |
| 标签 | rocm |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [ROCm] Simple CPU offload is slow without hipMemcpyBatchAsync mapping

### Issue 正文摘录

## Motivation Simple CPU offloading is currently very slow on AMD SKUs without the `hipMemcpyBatchAsync` mapping. In image below, circled dots are with offloading enabled. They are immensely slower than their no offloading counterparts. Confirmed that D2H H2D functioning at theoretical max on cluster. ## Tracking The implementation is under review in #43018. This issue tracks landing the mapping and validating simple CPU-offload performance on AMD SKUs.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [ROCm] Simple CPU offload is slow without hipMemcpyBatchAsync mapping rocm ## Motivation Simple CPU offloading is currently very slow on AMD SKUs without the `hipMemcpyBatchAsync` mapping. In image below, circled dots a
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: on AMD SKUs without the `hipMemcpyBatchAsync` mapping. In image below, circled dots are with offloading enabled. They are immensely slower than their no offloading counterparts. Confirmed that D2H H2D functioning at the...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [ROCm] Simple CPU offload is slow without hipMemcpyBatchAsync mapping rocm ## Motivation Simple CPU offloading is currently very slow on AMD SKUs without the `hipMemcpyBatchAsync` mapping. In image below, circled dots a...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [ROCm] Simple CPU offload is slow without hipMemcpyBatchAsync mapping rocm ## Motivation Simple CPU offloading is currently very slow on AMD SKUs without the `hipMemcpyBatchAsync` mapping. In image below, circled dots a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
