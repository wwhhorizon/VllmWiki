# vllm-project/vllm#9585: [Misc]: Does FP8 KV Cache function have an inverse quantization process？

| 字段 | 值 |
| --- | --- |
| Issue | [#9585](https://github.com/vllm-project/vllm/issues/9585) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Does FP8 KV Cache function have an inverse quantization process？

### Issue 正文摘录

In vLLM, enable FP8 KV Cache and observe from the code that quantization operations were indeed performed before storing KV. But currently, no inverse quantization operation has been found when reading KV. Is there no inverse quantization operation, or is it implicitly implemented at the underlying level? If it exists, I cannot find the relevant code implementation. Can you tell me where the inverse quantization operation is implemented.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Misc]: Does FP8 KV Cache function have an inverse quantization process？ In vLLM, enable FP8 KV Cache and observe from the code that quantization operations were indeed performed before storing KV. But currently, no inv...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: en reading KV. Is there no inverse quantization operation, or is it implicitly implemented at the underlying level? If it exists, I cannot find the relevant code implementation. Can you tell me where the inverse quantiz...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Misc]: Does FP8 KV Cache function have an inverse quantization process？ In vLLM, enable FP8 KV Cache and observe from the code that quantization operations were indeed performed before storing KV. But currently, no inv...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
