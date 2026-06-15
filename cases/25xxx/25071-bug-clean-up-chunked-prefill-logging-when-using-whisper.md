# vllm-project/vllm#25071: [Bug]: Clean up chunked prefill logging when using whisper

| 字段 | 值 |
| --- | --- |
| Issue | [#25071](https://github.com/vllm-project/vllm/issues/25071) |
| 状态 | closed |
| 标签 | bug;help wanted;good first issue |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Clean up chunked prefill logging when using whisper

### Issue 正文摘录

### 🐛 Describe the bug When using whisper, for example: ``` vllm serve openai/whisper-large-v3 ``` There are some logs that are a bit confusing: ``` (APIServer pid=3140911) INFO 09-17 12:37:08 [scheduler.py:222] Chunked prefill is enabled with max_num_batched_tokens=8192. (APIServer pid=3140911) INFO 09-17 12:37:10 [__init__.py:2790] Encoder-decoder models do not support chunked prefill nor prefix caching; disabling both. ``` Ideally, we wouldn't get that first "Chunked prefill is enabled" message. It looks like we may need to relocate the logic that is disabling it.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Clean up chunked prefill logging when using whisper bug;help wanted;good first issue ### 🐛 Describe the bug When using whisper, for example: ``` vllm serve openai/whisper-large-v3 ``` There are some logs that are...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: rver pid=3140911) INFO 09-17 12:37:10 [__init__.py:2790] Encoder-decoder models do not support chunked prefill nor prefix caching; disabling both. ``` Ideally, we wouldn't get that first "Chunked prefill is enabled" mes...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
