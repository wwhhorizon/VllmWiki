# vllm-project/vllm#1219: Support for Contrastive Search

| 字段 | 值 |
| --- | --- |
| Issue | [#1219](https://github.com/vllm-project/vllm/issues/1219) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support for Contrastive Search

### Issue 正文摘录

Does vllm supports contrastive search? If not, would be great to add that support as soon as possible? [Research](https://arxiv.org/pdf/2210.14140.pdf) shows that this improves model quality significantly and it is currently supported in transformers HF library. Would be great to get parity for this in vllm.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Research](https://arxiv.org/pdf/2210.14140.pdf) shows that this improves model quality significantly and it is currently supported in transformers HF library. Would be great to get parity for this in vllm.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Support for Contrastive Search feature request;stale Does vllm supports contrastive search? If not, would be great to add that support as soon as possible? [Research](https://arxiv.org/pdf/2210.14140.pdf) shows that thi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Support for Contrastive Search feature request;stale Does vllm supports contrastive search? If not, would be great to add that support as soon as possible? [Research](https://arxiv.org/pdf/2210.14140.pdf) shows that thi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
