# vllm-project/vllm#66: A critical bug in attention kernel after refactoring

| 字段 | 值 |
| --- | --- |
| Issue | [#66](https://github.com/vllm-project/vllm/issues/66) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache |
| 子分类 |  |
| Operator 关键词 | attention;cuda;kernel |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> A critical bug in attention kernel after refactoring

### Issue 正文摘录

It seems there's a critical bug introduced by #53 Running the `single_query_cached_kv_attention` kernel with certain configurations leads to CUDA illegal memory access errors. I found the bug in the unit tests.

## 现有链接修复摘要

#53 Refactor attention kernels | #68 Fix a bug in attention kernel

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e_query_cached_kv_attention` kernel with certain configurations leads to CUDA illegal memory access errors. I found the bug in the unit tests. performance attention_kv_cache attention;cuda;kernel #53 Refactor attention...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: #53 Running the `single_query_cached_kv_attention` kernel with certain configurations leads to CUDA illegal memory access errors. I found the bug in the unit tests. performance attention_kv_cache attention;cuda;kernel #...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: leads to CUDA illegal memory access errors. I found the bug in the unit tests. performance attention_kv_cache attention;cuda;kernel #53 Refactor attention kernels | #68 Fix a bug in attention kernel It seems there's a c...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#53](https://github.com/vllm-project/vllm/pull/53) | mentioned | 0.45 | Refactor attention kernels | ernel after refactoring it seems there's a critical bug introduced by #53 running the `single_query_cached_kv_attention` kernel with certain configurations leads to cuda illegal m… |
| [#68](https://github.com/vllm-project/vllm/pull/68) | closes_keyword | 0.95 | Fix a bug in attention kernel | Fixes #66 This PR fixes a bug in our attention kernel. The bug was introduced in #53 when changing the precision of computations in the attention kernel. Now the kernel unit te |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
