# vllm-project/vllm#4156: [Misc]: How to access the KV cache directly?

| 字段 | 值 |
| --- | --- |
| Issue | [#4156](https://github.com/vllm-project/vllm/issues/4156) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: How to access the KV cache directly?

### Issue 正文摘录

### Anything you want to discuss about vllm. I'm looking to conduct an experiment, which involves copying the contents of KV cache between nodes. I'm not super familiar with the codebase, is there any way to access the page table/KV cache directly? Where do I start? Any suggestions are helpful!

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Misc]: How to access the KV cache directly? stale ### Anything you want to discuss about vllm. I'm looking to conduct an experiment, which involves copying the contents of KV cache between nodes. I'm not super familiar...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Misc]: How to access the KV cache directly? stale ### Anything you want to discuss about vllm. I'm looking to conduct an experiment, which involves copying the contents of KV cache between nodes. I'm not super familiar...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
