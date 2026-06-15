# vllm-project/vllm#1026: Long prompt will block all running generation.

| 字段 | 值 |
| --- | --- |
| Issue | [#1026](https://github.com/vllm-project/vllm/issues/1026) |
| 状态 | closed |
| 标签 |  |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Long prompt will block all running generation.

### Issue 正文摘录

When i request using long prompt(larger than 4096), engine need 10s to process. At the moment, the running generation will be blocked until long prompt process task finished. When doing batch prompt, this phenomenon is more obvious. And may trigger abort onto new requests. vLLM: 0.1.7 @Yard1 Do you have any ideas? cc @zhuohan123 @WoosukKwon

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: Long prompt will block all running generation. When i request using long prompt(larger than 4096), engine need 10s to process. At the moment, the running generation will be blocked until long prompt process task finishe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Long prompt will block all running generation. When i request using long prompt(larger than 4096), engine need 10s to process. At the moment, the running generation will be blocked until long prompt process task finishe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
