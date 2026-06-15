# vllm-project/vllm#4957: [Feature]: Support loading of sharded vLLM serialized models with Tensorizer

| 字段 | 值 |
| --- | --- |
| Issue | [#4957](https://github.com/vllm-project/vllm/issues/4957) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support loading of sharded vLLM serialized models with Tensorizer

### Issue 正文摘录

### 🚀 The feature, motivation and pitch PR https://github.com/vllm-project/vllm/pull/3476 added support for loading models with Tensorizer, but has the limitation that it does not support loading a sharded vllm-serialized model to multiple GPUs (see [this verification check](https://github.com/vllm-project/vllm/blob/c3af44722cff56bba5fc912c8e16d9de02dfb532/vllm/model_executor/model_loader/tensorizer.py#L81-L87)). Use of sharded models would also benefit from the faster loading and encryption provided by Tensorizer. [This issue open with Tensorizer](https://github.com/coreweave/tensorizer/issues/81#issuecomment-1935224826) suggests a couple of approaches to support sharding. With tensor-parallel models, the model is split across the GPUs and the suggestion is to serialize each shard separately. I have prototyped this approach of splitting the vllm-tensorized model into multiple shards and am working on a PR. ### Alternatives The alternative given in [the Tensorizer issue](https://github.com/coreweave/tensorizer/issues/81#issuecomment-1935224826) is to deserializing Tensors to CPU memory and then send the tensors to the GPUs. This would decouple the serialization of the model from t...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Support loading of sharded vLLM serialized models with Tensorizer feature request ### 🚀 The feature, motivation and pitch PR https://github.com/vllm-project/vllm/pull/3476 added support for loading models wit...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: of the model from the sharding configuration, but would also be less efficient. ### Additional context _No response_
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: upport loading of sharded vLLM serialized models with Tensorizer feature request ### 🚀 The feature, motivation and pitch PR https://github.com/vllm-project/vllm/pull/3476 added support for loading models with Tensorizer...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
