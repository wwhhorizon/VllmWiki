# vllm-project/vllm#3573: [Feature]: Long context window - Ring Attention with Blockwise Transformers for Near-Infinite Context

| 字段 | 值 |
| --- | --- |
| Issue | [#3573](https://github.com/vllm-project/vllm/issues/3573) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Long context window - Ring Attention with Blockwise Transformers for Near-Infinite Context

### Issue 正文摘录

This paper might be of interest: https://arxiv.org/pdf/2310.01889.pdf This paper proposes Ring Attention with Blockwise Transformers, which leverages blockwise computation of self-attention and feedforward to distribute long sequences across multiple devices while fully overlapping the communication of key-value blocks with the computation of blockwise attention. This method handles long context window using multiple devices and could support up to 16M context window for extreme cases. @simon-mo Is this a feature you'd like to see implemented?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Attention with Blockwise Transformers for Near-Infinite Context feature request;stale This paper might be of interest: https://arxiv.org/pdf/2310.01889.pdf This paper proposes Ring Attention with Blockwise Transformers,...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Feature]: Long context window - Ring Attention with Blockwise Transformers for Near-Infinite Context feature request;stale This paper might be of interest: https://arxiv.org/pdf/2310.01889.pdf This paper proposes Ring...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
