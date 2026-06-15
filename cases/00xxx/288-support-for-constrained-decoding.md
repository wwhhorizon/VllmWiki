# vllm-project/vllm#288: Support for Constrained decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#288](https://github.com/vllm-project/vllm/issues/288) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 32; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support for Constrained decoding

### Issue 正文摘录

For getting structured outputs from custom-finetuned LLMs, extensive use of [constrained decoding](https://huggingface.co/docs/transformers/internal/generation_utils#transformers.DisjunctiveConstraint) is standard. Is there a plan to add support for DisjunctiveConstraint (and others) to vLLM in the near future? How would one go about implementing this in vLLM (if I were to add a PR)?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: m custom-finetuned LLMs, extensive use of [constrained decoding](https://huggingface.co/docs/transformers/internal/generation_utils#transformers.DisjunctiveConstraint) is standard. Is there a plan to add support for Dis...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Support for Constrained decoding good first issue;feature request For getting structured outputs from custom-finetuned LLMs, extensive use of [constrained decoding](https://huggingface.co/docs/transformers/internal/gene...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
