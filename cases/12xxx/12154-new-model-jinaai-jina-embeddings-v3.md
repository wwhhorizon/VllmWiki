# vllm-project/vllm#12154: [New Model]: jinaai/jina-embeddings-v3

| 字段 | 值 |
| --- | --- |
| Issue | [#12154](https://github.com/vllm-project/vllm/issues/12154) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: jinaai/jina-embeddings-v3

### Issue 正文摘录

### The model to consider. https://huggingface.co/jinaai/jina-embeddings-v3 jina-embeddings-v3 is a multilingual multi-task text embedding model designed for a variety of NLP applications. Based on the [Jina-XLM-RoBERTa architecture](https://huggingface.co/jinaai/xlm-roberta-flash-implementation), this model supports Rotary Position Embeddings to handle long input sequences up to 8192 tokens. Additionally, it features 5 LoRA adapters to generate task-specific embeddings efficiently. ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting the model you want? In subsequent version updates, has the project team considered adding support for jinaai/jina-embeddings-v3? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 92 tokens. Additionally, it features 5 LoRA adapters to generate task-specific embeddings efficiently. ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting the model you wa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: jinaai/jina-embeddings-v3 new-model ### The model to consider. https://huggingface.co/jinaai/jina-embeddings-v3 jina-embeddings-v3 is a multilingual multi-task text embedding model designed for a variety of...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: signed for a variety of NLP applications. Based on the [Jina-XLM-RoBERTa architecture](https://huggingface.co/jinaai/xlm-roberta-flash-implementation), this model supports Rotary Position Embeddings to handle long input...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
