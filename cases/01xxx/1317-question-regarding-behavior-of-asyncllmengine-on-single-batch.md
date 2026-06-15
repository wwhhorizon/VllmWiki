# vllm-project/vllm#1317: Question regarding behavior of AsyncLLMEngine on single batch

| 字段 | 值 |
| --- | --- |
| Issue | [#1317](https://github.com/vllm-project/vllm/issues/1317) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Question regarding behavior of AsyncLLMEngine on single batch

### Issue 正文摘录

We're planning to serve online traffic using AsyncLLMEngine based on example: https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/api_server.py But our traffic limits to 1x1 traffic, i.e. each HTTP request contains only 1 prompt. Will AsyncLLMEngine dynamically form a larger batch size for incoming requests? Thru reading the code, it seems it should have the same behavior as offline batch llm engine: on each decoding iteration, the scheduler will automatically create a large enough batch from the requests queue to max out GPU memory utilization. I want to confirm if this is true for online serving.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ts/api_server.py But our traffic limits to 1x1 traffic, i.e. each HTTP request contains only 1 prompt. Will AsyncLLMEngine dynamically form a larger batch size for incoming requests? Thru reading the code, it seems it s...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: matically create a large enough batch from the requests queue to max out GPU memory utilization. I want to confirm if this is true for online serving.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
