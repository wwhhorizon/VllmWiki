# vllm-project/vllm#28557: [New Model]: `jinaai/jina-reranker-v3` new reranking model

| 字段 | 值 |
| --- | --- |
| Issue | [#28557](https://github.com/vllm-project/vllm/issues/28557) |
| 状态 | closed |
| 标签 |  |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: `jinaai/jina-reranker-v3` new reranking model

### Issue 正文摘录

### The model to consider. https://huggingface.co/jinaai/jina-reranker-v3 This has better benchmarks than the `Qwen3-0.6B`. ### The closest model vllm already supports. https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/qwen3.py ### What's your difficulty of supporting the model you want? It's built on `Qwen3-0.6B` model. The [architecture](https://huggingface.co/jinaai/jina-reranker-v3/blob/main/config.json#L3) for this model is `JinaForRanking`. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [New Model]: `jinaai/jina-reranker-v3` new reranking model ### The model to consider. https://huggingface.co/jinaai/jina-reranker-v3 This has better benchmarks than the `Qwen3-0.6B`. ### The closest model vllm already s
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: nsider. https://huggingface.co/jinaai/jina-reranker-v3 This has better benchmarks than the `Qwen3-0.6B`. ### The closest model vllm already supports. https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/mo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: f supporting the model you want? It's built on `Qwen3-0.6B` model. The [architecture](https://huggingface.co/jinaai/jina-reranker-v3/blob/main/config.json#L3) for this model is `JinaForRanking`. ### Before submitting a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
