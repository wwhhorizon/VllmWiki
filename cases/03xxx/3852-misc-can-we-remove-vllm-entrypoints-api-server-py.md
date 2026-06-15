# vllm-project/vllm#3852: [Misc]: Can we remove `vllm/entrypoints/api_server.py`?

| 字段 | 值 |
| --- | --- |
| Issue | [#3852](https://github.com/vllm-project/vllm/issues/3852) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Can we remove `vllm/entrypoints/api_server.py`?

### Issue 正文摘录

### Anything you want to discuss about vllm. While gardening GitHub issues I've seen many issues where the user is using `-m vllm.entrypoints.api_server`, which indicates that users are either not aware of ignoring the note at the top of the file: https://github.com/vllm-project/vllm/blob/b7782002e1da25de77e0b1890ff8b72dd4df917c/vllm/entrypoints/api_server.py#L1-L7 Can we remove it to avoid future confusion?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Misc]: Can we remove `vllm/entrypoints/api_server.py`? stale ### Anything you want to discuss about vllm. While gardening GitHub issues I've seen many issues where the user is using `-m vllm.entrypoints.api_server`, wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
