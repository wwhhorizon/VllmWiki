# vllm-project/vllm#5063: [Misc]: How to use guided decoding and regex as well?

| 字段 | 值 |
| --- | --- |
| Issue | [#5063](https://github.com/vllm-project/vllm/issues/5063) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: How to use guided decoding and regex as well?

### Issue 正文摘录

### Anything you want to discuss about vllm. Here is my guided_json `guided_json = {"type": "object", "properties": { "age": {"type": "string", "pattern": r"^Fifty"}, "height": {"type": "string", "pattern": r"^five"}}}` I want to enforce the initial string in each of the keys, is this supported? And how can I go about doing this?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Misc]: How to use guided decoding and regex as well? stale ### Anything you want to discuss about vllm. Here is my guided_json `guided_json = {"type": "object", "properties": { "age": {"type": "string", "pattern": r"^F...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
