# vllm-project/vllm#20794: [Bug]: Unexpected Results from Qwen3-Reranker-0.6B in /v1/rerank API

| 字段 | 值 |
| --- | --- |
| Issue | [#20794](https://github.com/vllm-project/vllm/issues/20794) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Unexpected Results from Qwen3-Reranker-0.6B in /v1/rerank API

### Issue 正文摘录

### Your current environment ## Description When using vllm v0.9.2, the Qwen3-Reranker-0.6B model produces results that significantly deviate from expectations in the `/v1/rerank` endpoint. In contrast, the Qwen3-Embedding-0.6B model produces reasonable results in the same environment. ## Environment - vllm v0.9.2 - CUDA 12.4 - GPU: A100 ## Steps to Reproduce Make a POST request to `/v1/rerank` with the following payload: ```json { "model": "Qwen3-Reranker-0.6B", "query": "What is the capital of France?", "documents": [ "Paris is the capital and most populous city of France.", "London is the capital city of England and the United Kingdom.", "Berlin is the capital and largest city of Germany.", "Madrid is the capital and most populous city of Spain.", "Rome is the capital city of Italy." ], "top_n": 3 } ``` ## Current Behavior The Qwen3-Reranker-0.6B model returns London as the most relevant result for the query "What is the capital of France?", with Paris ranked second: ```json "results": [ { "index": 1, "document": { "text": "London is the capital city of England and the United Kingdom." }, "relevance_score": 0.8511418104171753 }, { "index": 0, "document": { "text": "Paris is the...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: onable results in the same environment. ## Environment - vllm v0.9.2 - CUDA 12.4 - GPU: A100 ## Steps to Reproduce Make a POST request to `/v1/rerank` with the following payload: ```json { "model": "Qwen3-Reranker-0.6B"...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Unexpected Results from Qwen3-Reranker-0.6B in /v1/rerank API bug;stale ### Your current environment ## Description When using vllm v0.9.2, the Qwen3-Reranker-0.6B model produces results that significantly deviat...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Unexpected Results from Qwen3-Reranker-0.6B in /v1/rerank API bug;stale ### Your current environment ## Description When using vllm v0.9.2, the Qwen3-Reranker-0.6B model produces results that significantly deviat...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ent. ## Environment - vllm v0.9.2 - CUDA 12.4 - GPU: A100 ## Steps to Reproduce Make a POST request to `/v1/rerank` with the following payload: ```json { "model": "Qwen3-Reranker-0.6B", "query": "What is the capital of...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ce?", "documents": [ "Paris is the capital and most populous city of France.", "London is the capital city of England and the United Kingdom.", "Berlin is the capital and largest city of Germany.", "Madrid is the capita...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
