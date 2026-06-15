# vllm-project/vllm#22861: [Performance]: Embedding model Benchmarks

| 字段 | 值 |
| --- | --- |
| Issue | [#22861](https://github.com/vllm-project/vllm/issues/22861) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Embedding model Benchmarks

### Issue 正文摘录

## Requirements ### Short context length encoder models Many still widely used embedding models have surprisingly short context lengths. Most of the Bert and Roberta models have absolute position embeddings and a context length of 512. We need a benchmark in with prompts in the 128-512 token range to test this kind of model. ### Long context length encoder models Some newer encoder models support longer context lengths. For example jinaai/jina-embeddings-v3 is a Roberta model with RoPE which supports up to 8k of context. Alibaba-NLP/gte-Qwen2-1.5B-instruct is an encoder model converted from decoder using the LLM2VEC method. It supports 32k of context. ### Long context decoder models Not all embedding models are encoders. There are some models such as BAAI/bge-multilingual-gemma2, Qwen/Qwen3-Embedding-0.6B and Qwen/Qwen3-Embedding-4B which support context lengths of 8K, 32K and 40K respectively. Since these models use last token pooling, chunked prefill and prefix caching are possible. With a mix of short and long requests, chunked prefill should allow short requests to return earlier, while prefix caching should allow ### Tests To test the models above, we need three datasets with...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Performance]: Embedding model Benchmarks performance ## Requirements ### Short context length encoder models Many still widely used embedding models have surprisingly short context lengths. Most of the Bert and Roberta...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: . Alibaba-NLP/gte-Qwen2-1.5B-instruct is an encoder model converted from decoder using the LLM2VEC method. It supports 32k of context. ### Long context decoder models Not all embedding models are encoders. There are som...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Performance]: Embedding model Benchmarks performance ## Requirements ### Short context length encoder models Many still widely used embedding models have surprisingly short context lengths. Most of the Bert and Roberta...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: he models above, we need three datasets with different context lengths - Small: 128 to 512 token range - Medium: 512 to 8K range - Long 8K to 32K The medium dataset should also have enough common prefixes to test prefix...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: models are encoders. There are some models such as BAAI/bge-multilingual-gemma2, Qwen/Qwen3-Embedding-0.6B and Qwen/Qwen3-Embedding-4B which support context lengths of 8K, 32K and 40K respectively. Since these models us...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
