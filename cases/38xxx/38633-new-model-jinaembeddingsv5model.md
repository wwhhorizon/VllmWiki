# vllm-project/vllm#38633: [New Model]: JinaEmbeddingsV5Model

| 字段 | 值 |
| --- | --- |
| Issue | [#38633](https://github.com/vllm-project/vllm/issues/38633) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: JinaEmbeddingsV5Model

### Issue 正文摘录

### The model to consider. The model I want to deploy is https://huggingface.co/jinaai/jina-embeddings-v5-text-small but I am getting Value error, Model architectures ['JinaEmbeddingsV5Model'] are not supported for now. and also this error: ImportError: This modeling file requires the following packages that were not found in your environment: peft. Run `pip install peft` ### The closest model vllm already supports. https://huggingface.co/jinaai/jina-embeddings-v4 ### What's your difficulty of supporting the model you want? _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: naEmbeddingsV5Model'] are not supported for now. and also this error: ImportError: This modeling file requires the following packages that were not found in your environment: peft. Run `pip install peft` ### The closest...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: want to deploy is https://huggingface.co/jinaai/jina-embeddings-v5-text-small but I am getting Value error, Model architectures ['JinaEmbeddingsV5Model'] are not supported for now. and also this error: ImportError: This...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: JinaEmbeddingsV5Model ### The model to consider. The model I want to deploy is https://huggingface.co/jinaai/jina-embeddings-v5-text-small but I am getting Value error, Model architectures ['JinaEmbeddingsV
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
