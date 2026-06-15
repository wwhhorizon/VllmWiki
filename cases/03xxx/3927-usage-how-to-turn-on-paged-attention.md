# vllm-project/vllm#3927: [Usage]:  how to turn on paged attention ?

| 字段 | 值 |
| --- | --- |
| Issue | [#3927](https://github.com/vllm-project/vllm/issues/3927) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:  how to turn on paged attention ?

### Issue 正文摘录

### Your current environment I am running : python -m vllm.entrypoints.openai.api_server --model meta-llama/Llama-2-7b-hf --dtype float32 --api-key token-abc123 question:is paged attention on by using this command ? Or should I do something ? thank you ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ironment I am running : python -m vllm.entrypoints.openai.api_server --model meta-llama/Llama-2-7b-hf --dtype float32 --api-key token-abc123 question:is paged attention on by using this command ? Or should I do somethin...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ou ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: -m vllm.entrypoints.openai.api_server --model meta-llama/Llama-2-7b-hf --dtype float32 --api-key token-abc123 question:is paged attention on by using this command ? Or should I do something ? thank you ### How would you...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
