# vllm-project/vllm#1707: API causes slowdown in batch request handling

| 字段 | 值 |
| --- | --- |
| Issue | [#1707](https://github.com/vllm-project/vllm/issues/1707) |
| 状态 | closed |
| 标签 | bug;unstale |
| 评论 | 42; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> API causes slowdown in batch request handling

### Issue 正文摘录

Using the API server and submitting multiple prompts to take advantage of speed benefit returns the following error: "multiple prompts in a batch is not currently supported" What's the point of vLLM without being able to send batches to the API? Of course, I can send multiple seperate requests, but those are handled sequentially and do not benefit from speed improvements. Correct me if I'm wrong...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: API causes slowdown in batch request handling bug;unstale Using the API server and submitting multiple prompts to take advantage of speed benefit returns the following error: "multiple prompts in a batch is not currentl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
