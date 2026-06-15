# vllm-project/vllm#2952: The answer accuracy of the QWen series model is lost

| 字段 | 值 |
| --- | --- |
| Issue | [#2952](https://github.com/vllm-project/vllm/issues/2952) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> The answer accuracy of the QWen series model is lost

### Issue 正文摘录

After using Vllm acceleration on the QWen series model, there is a significant loss in the accuracy of answers

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: The answer accuracy of the QWen series model is lost stale After using Vllm acceleration on the QWen series model, there is a significant loss in the accuracy of answers
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: The answer accuracy of the QWen series model is lost stale After using Vllm acceleration on the QWen series model, there is a significant loss in the accuracy of answers
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: The answer accuracy of the QWen series model is lost stale After using Vllm acceleration on the QWen series model, there is a significant loss in the accuracy of answers
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: The answer accuracy of the QWen series model is lost stale After using Vllm acceleration on the QWen series model, there is a significant loss in the accuracy of answers

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
