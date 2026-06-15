# vllm-project/vllm#5541: [Feature]: asymmetric tensor parallel

| 字段 | 值 |
| --- | --- |
| Issue | [#5541](https://github.com/vllm-project/vllm/issues/5541) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: asymmetric tensor parallel

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Current vllm don't support tp if vocab_size cannot be fully divided by tp number. it would raise error as: ``` ERROR 06-14 21:04:12 worker_base.py:165] File "/usr/local/lib/python3.10/dist-packages/vllm/distributed/utils.py", line 29, in divide ERROR 06-14 21:04:12 worker_base.py:165] ensure_divisibility(numerator, denominator) ERROR 06-14 21:04:12 worker_base.py:165] File "/usr/local/lib/python3.10/dist-packages/vllm/distributed/utils.py", line 22, in ensure_divisibility ERROR 06-14 21:04:12 worker_base.py:165] assert numerator % denominator == 0, "{} is not divisible by {}".format( ``` But for those model may only 5 card's gpu memory could hold, still need 8 for this reason, which is some kind of waste. ### Alternatives Could we support this asymmetric tp case? So that more gpu card could be saved? ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 65] assert numerator % denominator == 0, "{} is not divisible by {}".format( ``` But for those model may only 5 card's gpu memory could hold, still need 8 for this reason, which is some kind of waste. ### Alternatives C...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: asymmetric tensor parallel feature request;stale ### 🚀 The feature, motivation and pitch Current vllm don't support tp if vocab_size cannot be fully divided by tp number. it would raise error as: ``` ERROR 06...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: not divisible by {}".format( ``` But for those model may only 5 card's gpu memory could hold, still need 8 for this reason, which is some kind of waste. ### Alternatives Could we support this asymmetric tp case? So that...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
