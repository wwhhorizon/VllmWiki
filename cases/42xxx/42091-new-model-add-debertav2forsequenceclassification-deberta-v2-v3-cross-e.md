# vllm-project/vllm#42091: [New Model]:  Add DebertaV2ForSequenceClassification (DeBERTa-v2/v3 cross-encoder / reranker)

| 字段 | 值 |
| --- | --- |
| Issue | [#42091](https://github.com/vllm-project/vllm/issues/42091) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]:  Add DebertaV2ForSequenceClassification (DeBERTa-v2/v3 cross-encoder / reranker)

### Issue 正文摘录

## Your current environment vLLM main branch (post v0.9.x) ## 🚀 New model request **Model family:** DeBERTa-v2 / DeBERTa-v3 (Microsoft) **Architecture class:** `DebertaV2ForSequenceClassification` **HuggingFace examples:** - `cross-encoder/nli-deberta-v3-small` / `-base` / `-large` - `OpenAssistant/reward-model-deberta-v3-large-v2` - `BAAI/bge-reranker-base` - `meta-llama/Prompt-Guard-86M` ## Motivation DeBERTa-v3 is one of the most widely used encoder models for reranking and NLI — popular checkpoints include: - `cross-encoder/nli-deberta-v3-small` / `-base` / `-large` - `Capreolus/deberta-v3-base-msmarco` - `OpenAssistant/reward-model-deberta-v3-large-v2` - `meta-llama/Prompt-Guard-86M` - All `microsoft/deberta-v2-*` and `microsoft/deberta-v3-*` variants PR #20215 attempted to add this support but has been stalled for ~10 months, is in draft state, and contains critical bugs (see below). I am proposing a clean, production-ready implementation. ## Problems with PR #20215 1. **Runtime crash** — `DebertaV2Model.forward()` returns a `BaseModelOutput` object, but the code does `hidden_states[:, 0]` on that object directly → `TypeError` at inference time (never caught because no CI wa...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [New Model]: Add DebertaV2ForSequenceClassification (DeBERTa-v2/v3 cross-encoder / reranker) ## Your current environment vLLM main branch (post v0.9.x) ## 🚀 New model request **Model family:** DeBERTa-v2 / DeBERTa-v3 (M...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: model request **Model family:** DeBERTa-v2 / DeBERTa-v3 (Microsoft) **Architecture class:** `DebertaV2ForSequenceClassification` **HuggingFace examples:** - `cross-encoder/nli-deberta-v3-small` / `-base` / `-large` - `O...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Your current environment vLLM main branch (post v0.9.x) ## 🚀 New model request **Model family:** DeBERTa-v2 / DeBERTa-v3 (Microsoft) **Architecture class:** `DebertaV2ForSequenceClassification` **HuggingFace examples:**...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: at inference time (never caught because no CI was run). 2. **Performance regression** — disentangled attention (c2p + p2c) is implemented with nested Python `for` loops over `seq_len`, giving O(seq_len²) Python overhead...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ~630-line implementation - `DebertaV2ForSequenceClassification` using `DispatchPooler` pattern - `DebertaV2ContextPooler` as a `SequencePoolingMethod` (CLS pooling) - Fully vectorized disentangled attention via `torch.e...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
