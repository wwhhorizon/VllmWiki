# vllm-project/vllm#612: Multi-GPU error

| 字段 | 值 |
| --- | --- |
| Issue | [#612](https://github.com/vllm-project/vllm/issues/612) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Multi-GPU error

### Issue 正文摘录

While using tensor_parallel_size argument to load the vllm model, I was facing the issue in #557 stating something related to network address retrieval. According to [this comment](https://github.com/vllm-project/vllm/issues/570#issuecomment-1650973012) on #570 I trying building vllm from source and running it then. The error goes away, but it does not load the model and gets stuck on that cell. Is there any way I can get things working on multiple GPUs? I am able to run llama-2-7b, but in order to run llama-2-13b, I'll need to run it on multiple GPUs.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Multi-GPU error installation While using tensor_parallel_size argument to load the vllm model, I was facing the issue in #557 stating something related to network address retrieval. According to [this comment](https://g...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: installation While using tensor_parallel_size argument to load the vllm model, I was facing the issue in #557 stating something related to network address retrieval. According to [this comment](https://github.com/vllm-p...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: cing the issue in #557 stating something related to network address retrieval. According to [this comment](https://github.com/vllm-project/vllm/issues/570#issuecomment-1650973012) on #570 I trying building vllm from sou...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
