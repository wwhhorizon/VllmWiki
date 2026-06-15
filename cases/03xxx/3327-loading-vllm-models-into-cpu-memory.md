# vllm-project/vllm#3327: Loading vLLM models into CPU memory

| 字段 | 值 |
| --- | --- |
| Issue | [#3327](https://github.com/vllm-project/vllm/issues/3327) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Loading vLLM models into CPU memory

### Issue 正文摘录

Is it possible to load models into CPU memory instead of GPU memory?

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: PU memory stale Is it possible to load models into CPU memory instead of GPU memory?
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Loading vLLM models into CPU memory stale Is it possible to load models into CPU memory instead of GPU memory?
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Loading vLLM models into CPU memory stale Is it possible to load models into CPU memory instead of GPU memory?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
