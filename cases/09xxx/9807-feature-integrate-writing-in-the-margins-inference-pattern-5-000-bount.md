# vllm-project/vllm#9807: [Feature]: Integrate Writing in the Margins inference pattern ($5,000 Bounty)

| 字段 | 值 |
| --- | --- |
| Issue | [#9807](https://github.com/vllm-project/vllm/issues/9807) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Integrate Writing in the Margins inference pattern ($5,000 Bounty)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch [Writer](www.writer.com) has introduced ["Writing in the Margins" algorithm (WiM)](https://arxiv.org/html/2410.05258v1) that boosts results for long context window retrieval. The task is composed from "context" and "query" that is put at the end. The basic idea is to generate additional text while doing chunked prefill. The extra decoding step does not contribute to the KV-cache prefilling. The text is later concatenated and added to the final chunk. There exists a pure HuggingFace transformers implementation: [https://github.com/writer/writing-in-the-margins](https://github.com/writer/writing-in-the-margins) This is a high level overview of the inference pattern: And this is more detailed explanation how to do it efficiently by batch generation and prefill requests. The algorithm itself: The expected solution can be a feature added to vllm or a vllm fork, we are happy to maintain it. The WiM solution assumes extra input preprocessing steps (nltk splitting) and variable chunk size for chunked prefill, but those details can be left out from the solution. We offer $5,000 bounty for the main contributor (but the bounty can be shared if there is...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: tegrate Writing in the Margins inference pattern ($5,000 Bounty) feature request;stale ### 🚀 The feature, motivation and pitch [Writer](www.writer.com) has introduced ["Writing in the Margins" algorithm (WiM)](https://a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: org/html/2410.05258v1) that boosts results for long context window retrieval. The task is composed from "context" and "query" that is put at the end. The basic idea is to generate additional text while doing chunked pre...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rence pattern: And this is more detailed explanation how to do it efficiently by batch generation and prefill requests. The algorithm itself: The expected solution can be a feature added to vllm or a vllm fork, we are h...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ns) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: oing chunked prefill. The extra decoding step does not contribute to the KV-cache prefilling. The text is later concatenated and added to the final chunk. There exists a pure HuggingFace transformers implementation: [ht...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
