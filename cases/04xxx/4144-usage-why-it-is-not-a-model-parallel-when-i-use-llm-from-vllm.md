# vllm-project/vllm#4144: [Usage]: Why it is not a model parallel when I use LLM from vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#4144](https://github.com/vllm-project/vllm/issues/4144) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Why it is not a model parallel when I use LLM from vllm

### Issue 正文摘录

### Your current environment ```text when I use vllm.entrypoints.api_server , the model is loaded separately to all gpu, so the gpu memory usage of each gpu is low but when I load LLM with python api: model=LLM(model=path,tensor_parallel_size=num_gpu,quantization="gptq",trust_remote_code=True) each gpu loads the whole model to its memory why is the difference, how can I control the way to load model ``` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: `` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: LLM with python api: model=LLM(model=path,tensor_parallel_size=num_gpu,quantization="gptq",trust_remote_code=True) each gpu loads the whole model to its memory why is the difference, how can I control the way to load mo...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: trypoints.api_server , the model is loaded separately to all gpu, so the gpu memory usage of each gpu is low but when I load LLM with python api: model=LLM(model=path,tensor_parallel_size=num_gpu,quantization="gptq",tru...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: Why it is not a model parallel when I use LLM from vllm usage ### Your current environment ```text when I use vllm.entrypoints.api_server , the model is loaded separately to all gpu, so the gpu memory usage of...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
