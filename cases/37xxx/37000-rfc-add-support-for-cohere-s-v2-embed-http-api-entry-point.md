# vllm-project/vllm#37000: [RFC]: add support for Cohere's /v2/embed HTTP API entry point

| 字段 | 值 |
| --- | --- |
| Issue | [#37000](https://github.com/vllm-project/vllm/issues/37000) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: add support for Cohere's /v2/embed HTTP API entry point

### Issue 正文摘录

### Motivation. Today vLLM already has support for Cohere's `v1/rerank` & `/v2/rerank` HTTP API as a custom entry points for Rerank but the options for Embeddings are limited. For Embeddings only OpenAI's `/v1/embeddings` API is supported but `/v1/embeddings` is quite an old API interface that lacks support for modern features such as native multi modality, compression, and output types. Adding support for Cohere's `/v2/embed` HTTP API as a new custom entry point would add an embedding interface that matches Cohere's interface (https://docs.cohere.com/reference/embed) and can handle requests with modern embedding features like input types (e.g. classification, search_document, search_query, clustering), truncation, output dimension (for models that support matryoshka compression), and different embedding types (e.g. float, int8, uint8, binary, ubinary, base64) ### Proposed Change. Add support for Cohere's `/v2/embed` HTTP API entry point in `vllm/entrypoints/pooling/__init__.py` and create the a new `cohere_router.py`, `cohere_protocol.py` (matching Cohere's v2 embed schema ), and `cohere_serving.py` (to handle assembling the prompts and output type compression). Also try to reuse...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: with modern embedding features like input types (e.g. classification, search_document, search_query, clustering), truncation, output dimension (for models that support matryoshka compression), and different embedding ty...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: h_document, search_query, clustering), truncation, output dimension (for models that support matryoshka compression), and different embedding types (e.g. float, int8, uint8, binary, ubinary, base64) ### Proposed Change....
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: t in `vllm/entrypoints/pooling/__init__.py` and create the a new `cohere_router.py`, `cohere_protocol.py` (matching Cohere's v2 embed schema ), and `cohere_serving.py` (to handle assembling the prompts and output type c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ere's interface (https://docs.cohere.com/reference/embed) and can handle requests with modern embedding features like input types (e.g. classification, search_document, search_query, clustering), truncation, output dime...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
