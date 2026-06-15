# vllm-project/vllm#320: The  async_llm_engine may have resource leak when using stream

| 字段 | 值 |
| --- | --- |
| Issue | [#320](https://github.com/vllm-project/vllm/issues/320) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> The  async_llm_engine may have resource leak when using stream

### Issue 正文摘录

![image](https://github.com/vllm-project/vllm/assets/98044045/37400e69-a644-4b87-9e7d-fe1ba61eda3c) look at this, the output here continues for half a hour and never stops but nothing is generated. New request is pendding.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: continues for half a hour and never stops but nothing is generated. New request is pendding.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
