# vllm-project/vllm#29645: [Bug]: Rotated samples extraction - accuracy loss

| 字段 | 值 |
| --- | --- |
| Issue | [#29645](https://github.com/vllm-project/vllm/issues/29645) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Rotated samples extraction - accuracy loss

### Issue 正文摘录

Rotated image data not extracted properly for qwen3-vl

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: Rotated samples extraction - accuracy loss bug;stale Rotated image data not extracted properly for qwen3-vl
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: - accuracy loss bug;stale Rotated image data not extracted properly for qwen3-vl
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Rotated samples extraction - accuracy loss bug;stale Rotated image data not extracted properly for qwen3-vl
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: Rotated samples extraction - accuracy loss bug;stale Rotated image data not extracted properly for qwen3-vl

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
