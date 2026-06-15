# vllm-project/vllm#5707: [Misc]: 我在使用vllm启动的openai api在进行对话时出现这样的情况

| 字段 | 值 |
| --- | --- |
| Issue | [#5707](https://github.com/vllm-project/vllm/issues/5707) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: 我在使用vllm启动的openai api在进行对话时出现这样的情况

### Issue 正文摘录

![20240621-092752](https://github.com/vllm-project/vllm/assets/29626411/1a1eded9-9bf8-4e30-92d4-8751f9e5bce8) 在使用流式生成时，大模型的回答会出现自问自答的情况。

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Misc]: 我在使用vllm启动的openai api在进行对话时出现这样的情况 stale ![20240621-092752](https://github.com/vllm-project/vllm/assets/29626411/1a1eded9-9bf8-4e30-92d4-8751f9e5bce8) 在使用流式生成时，大模型的回答会出现自问自答的情况。

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
