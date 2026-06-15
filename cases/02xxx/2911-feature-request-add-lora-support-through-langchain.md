# vllm-project/vllm#2911: Feature Request: Add LoRA support through LangChain

| 字段 | 值 |
| --- | --- |
| Issue | [#2911](https://github.com/vllm-project/vllm/issues/2911) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Feature Request: Add LoRA support through LangChain

### Issue 正文摘录

Would love to see LoRA (and QLoRA when #2828 is merged in) integration for LangChain. This would be good for systems that already have LangChain integration up and running, but are low on GPU memory and want to utilize vLLM

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: s that already have LangChain integration up and running, but are low on GPU memory and want to utilize vLLM
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Feature Request: Add LoRA support through LangChain Would love to see LoRA (and QLoRA when #2828 is merged in) integration for LangChain. This would be good for systems that already have LangChain integration up and run...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
