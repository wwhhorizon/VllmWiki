# vllm-project/vllm#26823: [Feature]: support jina multimodal reranker api request format

| 字段 | 值 |
| --- | --- |
| Issue | [#26823](https://github.com/vllm-project/vllm/issues/26823) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: support jina multimodal reranker api request format

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Thanks to the [PR](https://github.com/vllm-project/vllm/pull/20260), vLLM now support serving jinaai/jina-reranker-m0 model. But the api do not align with jina official multimodal api. ``` curl https://api.jina.ai/v1/rerank \ -H "Content-Type: application/json" \ -H "Authorization: Bearer jina_fa1c5a379d5b44968a87a3b8b2edb380EqdhLGZGOALL9gVgJi-s2q-V80e4" \ -d @- <<EOFEOF { "model": "jina-reranker-m0", "query": "small language model data extraction", "documents": [ { "image": "https://raw.githubusercontent.com/jina-ai/multimodal-reranker-test/main/handelsblatt-preview.png" }, { "image": "https://raw.githubusercontent.com/jina-ai/multimodal-reranker-test/main/paper-11.png" }, { "image": "https://raw.githubusercontent.com/jina-ai/multimodal-reranker-test/main/wired-preview.png" }, { "text": "We present ReaderLM-v2, a compact 1.5 billion parameter language model designed for efficient web content extraction. Our model processes documents up to 512K tokens, transforming messy HTML into clean Markdown or JSON formats with high accuracy -- making it an ideal tool for grounding large language models. The models effectiveness results from two key inn...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: support jina multimodal reranker api request format feature request ### 🚀 The feature, motivation and pitch Thanks to the [PR](https://github.com/vllm-project/vllm/pull/20260), vLLM now support serving jinaai...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: "image": "https://raw.githubusercontent.com/jina-ai/multimodal-reranker-test/main/handelsblatt-preview.png" }, { "image": "https://raw.githubusercontent.com/jina-ai/multimodal-reranker-test/main/paper-11.png" }, { "imag...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 4" \ -d @- <<EOFEOF { "model": "jina-reranker-m0", "query": "small language model data extraction", "documents": [ { "image": "https://raw.githubusercontent.com/jina-ai/multimodal-reranker-test/main/handelsblatt-preview...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: support jina multimodal reranker api request format feature request ### 🚀 The feature, motivation and pitch Thanks to the [PR](https://github.com/vllm-project/vllm/pull/20260), vLLM now support serving jinaai...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: s, transforming messy HTML into clean Markdown or JSON formats with high accuracy -- making it an ideal tool for grounding large language models. The models effectiveness results from two key innovations: (1) a three-st...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
