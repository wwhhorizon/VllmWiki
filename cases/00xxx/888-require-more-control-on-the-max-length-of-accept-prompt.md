# vllm-project/vllm#888: Require more control on the max length of accept prompt

| 字段 | 值 |
| --- | --- |
| Issue | [#888](https://github.com/vllm-project/vllm/issues/888) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Require more control on the max length of accept prompt

### Issue 正文摘录

Hi, thanks for the wonderful vllm project. In this file https://github.com/vllm-project/vllm/blob/4b6f069b6fbb4f2ef7d4c6a62140229be61c5dd3/vllm/config.py#L119 we see that the max length is bounded by the config.json attached to the model. For example in llama-2, there is a `"max_position_embeddings": 4096` in its config. So in default vllm, the whole sequence (prompt+output) will always `"max_position_embeddings": 8192`. So is it possible to add an extra, new argument that can set a larger value to `scheduler_config.max_model_len`, to handle this special use case? Thanks in advance!

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: com/vllm-project/vllm/blob/4b6f069b6fbb4f2ef7d4c6a62140229be61c5dd3/vllm/config.py#L119 we see that the max length is bounded by the config.json attached to the model. For example in llama-2, there is a `"max_position_e...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: et a larger value to `scheduler_config.max_model_len`, to handle this special use case? Thanks in advance!
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: t possible to add an extra, new argument that can set a larger value to `scheduler_config.max_model_len`, to handle this special use case? Thanks in advance!

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
