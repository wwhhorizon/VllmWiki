# vllm-project/vllm#44294: [Bug][OffloadingConnector] _blocks_being_loaded serialises concurrent requests through a single load, causing 12× TTFT inflation

| 字段 | 值 |
| --- | --- |
| Issue | [#44294](https://github.com/vllm-project/vllm/issues/44294) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug][OffloadingConnector] _blocks_being_loaded serialises concurrent requests through a single load, causing 12× TTFT inflation

### Issue 正文摘录

_本地原始数据中没有 issue 正文。_

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug][OffloadingConnector] _blocks_being_loaded serialises concurrent requests through a single load, causing 12× TTFT inflation
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug][OffloadingConnector] _blocks_being_loaded serialises concurrent requests through a single load, causing 12× TTFT inflation
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug][OffloadingConnector] _blocks_being_loaded serialises concurrent requests through a single load, causing 12× TTFT inflation

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
