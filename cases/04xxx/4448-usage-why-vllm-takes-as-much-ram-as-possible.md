# vllm-project/vllm#4448: [Usage]: why vllm takes as much ram as possible ?

| 字段 | 值 |
| --- | --- |
| Issue | [#4448](https://github.com/vllm-project/vllm/issues/4448) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: why vllm takes as much ram as possible ?

### Issue 正文摘录

### Your current environment I have multiple 0.5B model running. By default each vllm instance would take 20G ram. I understand the vllm would maintain the memory management, however I don't see why it is necessary to take that much ram so this little model. My question is would there be some start up option to let it run in a "minimal" status ? ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ? ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: m as possible ? usage ### Your current environment I have multiple 0.5B model running. By default each vllm instance would take 20G ram. I understand the vllm would maintain the memory management, however I don't see wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
