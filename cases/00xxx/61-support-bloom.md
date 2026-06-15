# vllm-project/vllm#61: Support BLOOM

| 字段 | 值 |
| --- | --- |
| Issue | [#61](https://github.com/vllm-project/vllm/issues/61) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support BLOOM

### Issue 正文摘录

BLOOM is an open-source LLM developed by BigScience. The BLOOM models have achieved high rankings in HuggingFace downloads. It'd be great to have these models in our catalog.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Support BLOOM new-model BLOOM is an open-source LLM developed by BigScience. The BLOOM models have achieved high rankings in HuggingFace downloads. It'd be great to have these models in our catalog.
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Support BLOOM new-model BLOOM is an open-source LLM developed by BigScience. The BLOOM models have achieved high rankings in HuggingFace downloads. It'd be great to have these models in our catalog.
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: Support BLOOM new-model BLOOM is an open-source LLM developed by BigScience. The BLOOM models have achieved high rankings in HuggingFace downloads. It'd be great to have these models in our catalog.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
