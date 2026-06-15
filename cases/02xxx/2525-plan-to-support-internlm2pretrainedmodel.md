# vllm-project/vllm#2525: plan to support InternLM2PreTrainedModel?

| 字段 | 值 |
| --- | --- |
| Issue | [#2525](https://github.com/vllm-project/vllm/issues/2525) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> plan to support InternLM2PreTrainedModel?

### Issue 正文摘录

InternLM2PreTrainedModel support 200k input&output， which realy need vllm and tp to build a model service

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: eTrainedModel support 200k input&output， which realy need vllm and tp to build a model service
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: plan to support InternLM2PreTrainedModel? InternLM2PreTrainedModel support 200k input&output， which realy need vllm and tp to build a model service

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
