# vllm-project/vllm#464: RoPE scaling support?

| 字段 | 值 |
| --- | --- |
| Issue | [#464](https://github.com/vllm-project/vllm/issues/464) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> RoPE scaling support?

### Issue 正文摘录

HF [Merged](https://github.com/huggingface/transformers/pull/24653) RoPE scaling into their library. This allows to increase context length by 4x without retraining.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: RoPE scaling support? feature request HF [Merged](https://github.com/huggingface/transformers/pull/24653) RoPE scaling into their library. This allows to increase context length by 4x without retraining.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: RoPE scaling support? feature request HF [Merged](https://github.com/huggingface/transformers/pull/24653) RoPE scaling into their library. This allows to increase context length by 4x without retraining.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
