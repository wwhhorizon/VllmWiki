# vllm-project/vllm#16874: [New Model]: jinaai/jina-embeddings-v2-base-code

| 字段 | 值 |
| --- | --- |
| Issue | [#16874](https://github.com/vllm-project/vllm/issues/16874) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: jinaai/jina-embeddings-v2-base-code

### Issue 正文摘录

### The model to consider. https://huggingface.co/jinaai/jina-embeddings-v2-base-code jina-embeddings-v2-base-code is an multilingual embedding model speaks English and 30 widely used programming languages. Same as other jina-embeddings-v2 series, it supports 8192 sequence length. jina-embeddings-v2-base-code is based on a Bert architecture (JinaBert) that supports the symmetric bidirectional variant of [ALiBi](https://arxiv.org/abs/2108.12409) to allow longer sequence length. The backbone jina-bert-v2-base-code is pretrained on the [github-code](https://huggingface.co/datasets/codeparrot/github-code) dataset. The model is further trained on Jina AI's collection of more than 150 millions of coding question answer and docstring source code pairs. These pairs were obtained from various domains and were carefully selected through a thorough cleaning process. ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting the model you want? _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm....

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: jinaai/jina-embeddings-v2-base-code new-model;stale ### The model to consider. https://huggingface.co/jinaai/jina-embeddings-v2-base-code jina-embeddings-v2-base-code is an multilingual embedding model spea...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s 8192 sequence length. jina-embeddings-v2-base-code is based on a Bert architecture (JinaBert) that supports the symmetric bidirectional variant of [ALiBi](https://arxiv.org/abs/2108.12409) to allow longer sequence len...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: jinaai/jina-embeddings-v2-base-code new-model;stale ### The model to consider. https://huggingface.co/jinaai/jina-embeddings-v2-base-code jina-embeddings-v2-base-code is an multilingual embedding model spea...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
