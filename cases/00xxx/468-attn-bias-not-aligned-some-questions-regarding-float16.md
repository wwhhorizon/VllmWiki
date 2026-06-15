# vllm-project/vllm#468: attn_bias not aligned & some questions regarding float16

| 字段 | 值 |
| --- | --- |
| Issue | [#468](https://github.com/vllm-project/vllm/issues/468) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> attn_bias not aligned & some questions regarding float16

### Issue 正文摘录

Hi, 1. When playing with MPT-7b models, I frequently meet the issues of "attn_bias not aligned", with tensor_parallel_size - 2, how do alleviate this issue? 2. Besides, I just find that your default model loading scripts load float16 versions, for fair evaluation, is it necessary to switch to float32? Thanks very much in advance!

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: attn_bias not aligned & some questions regarding float16 bug Hi, 1. When playing with MPT-7b models, I frequently meet the issues of "attn_bias not aligned", with tensor_parallel_size - 2, how do alleviate this issue? 2...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: esides, I just find that your default model loading scripts load float16 versions, for fair evaluation, is it necessary to switch to float32? Thanks very much in advance!
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: & some questions regarding float16 bug Hi, 1. When playing with MPT-7b models, I frequently meet the issues of "attn_bias not aligned", with tensor_parallel_size - 2, how do alleviate this issue? 2. Besides, I just find...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: that your default model loading scripts load float16 versions, for fair evaluation, is it necessary to switch to float32? Thanks very much in advance!

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
