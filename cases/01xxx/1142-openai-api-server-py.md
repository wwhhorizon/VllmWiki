# vllm-project/vllm#1142: 源码openai api_server.py报错

| 字段 | 值 |
| --- | --- |
| Issue | [#1142](https://github.com/vllm-project/vllm/issues/1142) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> 源码openai api_server.py报错

### Issue 正文摘录

AttributeError: 'ChatCompletionRequest' object has no attribute 'stop_token_ids'

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 源码openai api_server.py报错 AttributeError: 'ChatCompletionRequest' object has no attribute 'stop_token_ids'

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
