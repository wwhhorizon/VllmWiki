# vllm-project/vllm#24320: [Feature]: Batch interface request reordering to boost APC hits

| 字段 | 值 |
| --- | --- |
| Issue | [#24320](https://github.com/vllm-project/vllm/issues/24320) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Batch interface request reordering to boost APC hits

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Feature, motivation and pitch Large offline/batch jobs often contain requests that share exactly the same prefix (system prompt + template + few-shots, etc.). vLLM already has Automatic Prefix Caching (APC), so identical prefixes can reuse KV and skip prefill. However, with the current FCFS-style arrival order, two requests that could reuse the same prefix may be far apart in the queue (e.g., 1000th and 9000th), making APC hits unreliable due to LRU eviction under pressure. Proposal: add an *opt-in* request reordering pass at the batch interface (the JSONL “run-batch” path) that tries to maximize APC reuse by moving later requests with the same prefix close to the first occurrence, so KV blocks are more likely to remain hot and reused. This mirrors the global prefix sharing and throughput-oriented scheduling idea from [BatchLLM](https://arxiv.org/pdf/2412.03594), and implemented at the batch interface ([vllm/entrypoints/openai/run_batch.py](https://github.com/vllm-project/vllm/blob/e599e2c65ee32abcc986733ab0a55becea158bb4/vllm/entrypoints/openai/run_batch.py)) without touching the engine’s core scheduler. ### Background / prior art * APC...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Feature]: Batch interface request reordering to boost APC hits feature request;stale ### 🚀 The feature, motivation and pitch ### Feature, motivation and pitch Large offline/batch jobs often contain requests that share...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: ely to remain hot and reused. This mirrors the global prefix sharing and throughput-oriented scheduling idea from [BatchLLM](https://arxiv.org/pdf/2412.03594), and implemented at the batch interface ([vllm/entrypoints/o...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: LLM: caches KV for identical token prefixes; reuse avoids prefill. (Docs linked below) * BatchLLM: explicitly identifies common prefixes globally and reorders requests (also prioritizes decode-heavy ones and mixes prefi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ng window (e.g., 2k) to bound memory; window None = global reordering. * Fallback to the original order for unknown endpoints. CLI sketch: ```bash vllm run-batch \ --model \ --input-file in.jsonl \ --output-file out.jso...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
