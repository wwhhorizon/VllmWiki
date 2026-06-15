# vllm-project/vllm#4346: [Usage]: why can't the `max_model_len` be greater than `max_position_embeddings` for llama2?

| 字段 | 值 |
| --- | --- |
| Issue | [#4346](https://github.com/vllm-project/vllm/issues/4346) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: why can't the `max_model_len` be greater than `max_position_embeddings` for llama2?

### Issue 正文摘录

### Your current environment when we are running prefill stage, vllm take multiple requests to do prefill. Is this limited by the `max_position_embeddings`? I think it's not limited by this number, because each sequence has its own start index, we only need to ensure that each sequence is shorter than `max_position_embeddings`. Is that the fact? ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: x_model_len` be greater than `max_position_embeddings` for llama2? usage;stale ### Your current environment when we are running prefill stage, vllm take multiple requests to do prefill. Is this limited by the `max_posit...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: t? ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: why can't the `max_model_len` be greater than `max_position_embeddings` for llama2? usage;stale ### Your current environment when we are running prefill stage, vllm take multiple requests to do prefill. Is this...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
