# vllm-project/vllm#7481: Release v0.5.5

| 字段 | 值 |
| --- | --- |
| Issue | [#7481](https://github.com/vllm-project/vllm/issues/7481) |
| 状态 | closed |
| 标签 |  |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Release v0.5.5

### Issue 正文摘录

We will make a release later this week or early next week (Aug 16-Aug19) to address Gemma logits soft-caps bug, openai server metrics bug, and include more performance enhancements. Please add blockers if needed.

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ver metrics bug, and include more performance enhancements. Please add blockers if needed.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e a release later this week or early next week (Aug 16-Aug19) to address Gemma logits soft-caps bug, openai server metrics bug, and include more performance enhancements. Please add blockers if needed.
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: e a release later this week or early next week (Aug 16-Aug19) to address Gemma logits soft-caps bug, openai server metrics bug, and include more performance enhancements. Please add blockers if needed.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
