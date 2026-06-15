# vllm-project/vllm#35226: [Performance]: DeepSeek 3.2 Multi-stream indexer

| 字段 | 值 |
| --- | --- |
| Issue | [#35226](https://github.com/vllm-project/vllm/issues/35226) |
| 状态 | open |
| 标签 | performance;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: DeepSeek 3.2 Multi-stream indexer

### Issue 正文摘录

### Proposal to improve performance Make the DeepSeek 3.2 use multiple cuda streams for overlap `weights_proj` with `wq_b`, `wk`, `k_norm`, `rotary_emb` etc. like sglang, see: https://github.com/sgl-project/sglang/pull/16637 https://github.com/sgl-project/sglang/pull/17688

## 现有链接修复摘要

#35968 [Performance] DeepSeek V3.2 multi-stream indexer overlap

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Proposal to improve performance Make the DeepSeek 3.2 use multiple cuda streams for overlap `weights_proj` with `wq_b`, `wk`, `k_norm`, `rotary_emb` etc. like sglang, see: https://github.com/sgl-project/sglang/pull/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Performance]: DeepSeek 3.2 Multi-stream indexer performance;stale ### Proposal to improve performance Make the DeepSeek 3.2 use multiple cuda streams for overlap `weights_proj` with `wq_b`, `wk`, `k_norm`, `rotary_emb`...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35968](https://github.com/vllm-project/vllm/pull/35968) | closes_keyword | 0.95 | [Performance] DeepSeek V3.2 multi-stream indexer overlap | Closes #35226 Overlap `weights_proj` with `wk + k_norm` in the DeepSeek V3.2 `Indexer` forward pass using a secondary CUDA stream. The `weights_proj` GEMM is small (hidden_size |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
