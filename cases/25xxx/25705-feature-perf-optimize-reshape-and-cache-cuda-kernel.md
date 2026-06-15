# vllm-project/vllm#25705: [Feature]: [Perf] Optimize `reshape_and_cache` CUDA Kernel

| 字段 | 值 |
| --- | --- |
| Issue | [#25705](https://github.com/vllm-project/vllm/issues/25705) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api |
| 子分类 |  |
| Operator 关键词 | cache;cuda;kernel |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: [Perf] Optimize `reshape_and_cache` CUDA Kernel

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Similar to https://github.com/vllm-project/vllm/pull/22036 We can optimize the `reshape_and_cache` Cuda kernel. Pick it up if you are interested.

## 现有链接修复摘要

#26021 [Perf] Optimize reshape_and_cache CUDA Kernel

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Feature]: [Perf] Optimize `reshape_and_cache` CUDA Kernel good first issue;feature request ### 🚀 The feature, motivation and pitch Similar to https://github.com/vllm-project/vllm/pull/22036 We can optimize the `reshape...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Perf] Optimize `reshape_and_cache` CUDA Kernel good first issue;feature request ### 🚀 The feature, motivation and pitch Similar to https://github.com/vllm-project/vllm/pull/22036 We can optimize the `reshape_and_cache`...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#26021](https://github.com/vllm-project/vllm/pull/26021) | closes_keyword | 0.95 | [Perf] Optimize reshape_and_cache CUDA Kernel | FIX #25705 ## Method - the shape of key/value is: num_tokens * num_heads * head_size - the shape of key_cache is: num_blocks * num_heads * (head_size // x) * block_size * x - th |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
