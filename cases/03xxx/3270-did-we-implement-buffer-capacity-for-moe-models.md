# vllm-project/vllm#3270: Did we implement buffer capacity for moe models?

| 字段 | 值 |
| --- | --- |
| Issue | [#3270](https://github.com/vllm-project/vllm/issues/3270) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Did we implement buffer capacity for moe models?

### Issue 正文摘录

https://arxiv.org/abs/2402.05526 shows that it can overflow if there is buffer capacity for an expert.

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: Did we implement buffer capacity for moe models? https://arxiv.org/abs/2402.05526 shows that it can overflow if there is buffer capacity for an expert.
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Did we implement buffer capacity for moe models? https://arxiv.org/abs/2402.05526 shows that it can overflow if there is buffer capacity for an expert.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Did we implement buffer capacity for moe models? https://arxiv.org/abs/2402.05526 shows that it can overflow if there is buffer capacity for an expert.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
