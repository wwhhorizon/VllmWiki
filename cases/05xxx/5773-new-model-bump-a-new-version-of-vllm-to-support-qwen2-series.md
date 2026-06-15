# vllm-project/vllm#5773: [New Model]: bump a new version of vllm to support Qwen2 series

| 字段 | 值 |
| --- | --- |
| Issue | [#5773](https://github.com/vllm-project/vllm/issues/5773) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: bump a new version of vllm to support Qwen2 series

### Issue 正文摘录

### The model to consider. Qwen2 series, in https://huggingface.co/Qwen/Qwen2-7B ### The closest model vllm already supports. Qwen1.5 series ### What's your difficulty of supporting the model you want? Current version （v0.5.0-post1）didn't have the kernel to run Qwen2 series. The intermediate size of all qwen2 models is not supported by punica yet. And now the problem have been solved by https://github.com/vllm-project/vllm/pull/5441 I'm glad to see that the code is bumped and a new version will be introduced in the next days!

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: bump a new version of vllm to support Qwen2 series new-model ### The model to consider. Qwen2 series, in https://huggingface.co/Qwen/Qwen2-7B ### The closest model vllm already supports. Qwen1.5 series ###...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [New Model]: bump a new version of vllm to support Qwen2 series new-model ### The model to consider. Qwen2 series, in https://huggingface.co/Qwen/Qwen2-7B ### The closest model vllm already supports. Qwen1.5 series ###...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
