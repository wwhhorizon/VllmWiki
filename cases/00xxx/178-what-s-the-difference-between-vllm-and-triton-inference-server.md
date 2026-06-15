# vllm-project/vllm#178: What's the difference between vllm and triton-inference-server?

| 字段 | 值 |
| --- | --- |
| Issue | [#178](https://github.com/vllm-project/vllm/issues/178) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> What's the difference between vllm and triton-inference-server?

### Issue 正文摘录

May vllm can achieve the performance like fastertransformer on inference side? Just curious about the detailed optimization you're done and the goal you want to achieve. BTW, vllm really accelerate our deploy work, thx.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: What's the difference between vllm and triton-inference-server? May vllm can achieve the performance like fastertransformer on inference side? Just curious about the detailed optimization you're done and the goal you wa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
