# vllm-project/vllm#3008: Can pip install hf_transfer be added to the docker openai template?

| 字段 | 值 |
| --- | --- |
| Issue | [#3008](https://github.com/vllm-project/vllm/issues/3008) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Can pip install hf_transfer be added to the docker openai template?

### Issue 正文摘录

This allows an env variable to be set that increases download speed for weights.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Can pip install hf_transfer be added to the docker openai template? This allows an env variable to be set that increases download speed for weights.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Can pip install hf_transfer be added to the docker openai template? This allows an env variable to be set that increases download speed for weights.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
