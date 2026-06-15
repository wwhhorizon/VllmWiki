# vllm-project/vllm#3575: [Feature]: Long context window - LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#3575](https://github.com/vllm-project/vllm/issues/3575) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Long context window - LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens

### Issue 正文摘录

### 🚀 The feature, motivation and pitch This paper might be of interest: https://arxiv.org/pdf/2402.13753.pdf LongRoPE enhances the capabilities of pre-trained language models by extending their context windows to 2048k tokens while maintaining performance at shorter contexts. @simon-mo Is this a feature you'd like to see implemented? ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: - LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens feature request;stale ### 🚀 The feature, motivation and pitch This paper might be of interest: https://arxiv.org/pdf/2402.13753.pdf LongRoPE enhances the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 02.13753.pdf LongRoPE enhances the capabilities of pre-trained language models by extending their context windows to 2048k tokens while maintaining performance at shorter contexts. @simon-mo Is this a feature you'd like...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
