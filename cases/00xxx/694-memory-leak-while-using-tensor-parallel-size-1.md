# vllm-project/vllm#694: Memory leak while using tensor_parallel_size>1

| 字段 | 值 |
| --- | --- |
| Issue | [#694](https://github.com/vllm-project/vllm/issues/694) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Memory leak while using tensor_parallel_size>1

### Issue 正文摘录

![image](https://github.com/vllm-project/vllm/assets/26181650/70c44266-fbb4-4945-a567-78e9eb4c9b06)

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Memory leak while using tensor_parallel_size>1 bug;stale ![image](https://github.com/vllm-project/vllm/assets/26181650/70c44266-fbb4-4945-a567-78e9eb4c9b06)

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
