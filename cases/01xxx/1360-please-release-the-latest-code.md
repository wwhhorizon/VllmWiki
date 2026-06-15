# vllm-project/vllm#1360: Please release the latest code

| 字段 | 值 |
| --- | --- |
| Issue | [#1360](https://github.com/vllm-project/vllm/issues/1360) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Please release the latest code

### Issue 正文摘录

Using the current release version, Mistral models cannot be used with VLLM, getting the error 'ValueError: Quantization is not supported for '. After the last release, lots of changes were added for Mistral models, without good GPU support VLLM cannot be built from the source, please release the latest build to Pypi so that everyone can access the latest features.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Please release the latest code Using the current release version, Mistral models cannot be used with VLLM, getting the error 'ValueError: Quantization is not supported for '. After the last release, lots of changes were...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: Mistral models cannot be used with VLLM, getting the error 'ValueError: Quantization is not supported for '. After the last release, lots of changes were added for Mistral models, without good GPU support VLLM cannot be...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: lease release the latest code Using the current release version, Mistral models cannot be used with VLLM, getting the error 'ValueError: Quantization is not supported for '. After the last release, lots of changes were...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Please release the latest code Using the current release version, Mistral models cannot be used with VLLM, getting the error 'ValueError: Quantization is not supported for '. After the last release, lots of changes were...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
