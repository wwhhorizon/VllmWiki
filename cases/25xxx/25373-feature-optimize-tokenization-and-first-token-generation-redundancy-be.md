# vllm-project/vllm#25373: [Feature]: Optimize Tokenization and First Token Generation Redundancy Between Prefill and Decode Stages in Disaggregated Prefill

| 字段 | 值 |
| --- | --- |
| Issue | [#25373](https://github.com/vllm-project/vllm/issues/25373) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Optimize Tokenization and First Token Generation Redundancy Between Prefill and Decode Stages in Disaggregated Prefill

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Background In the current vLLM disaggregated prefill architecture, the workflow is as follows: - The prefill side receives an input request, performs tokenization, generates the first token via inference, and produces the corresponding KV cache. - The decode side then receives the same request, re-tokenizes the input, fetches the KV cache, and starts inference again from the first token. This leads to two redundant operations: 1. **Tokenization**: The decode side repeats the tokenization already performed by the prefill side. 2. **First Token Generation**: The decode side redundantly generates the first token, which was already inferred on the prefill side. ### Motivation Both points offer clear optimization opportunities for improved efficiency and latency in the disaggregated prefill design. ### Proposal - **Reuse Tokenization Results:** - Pass tokenization results from the prefill side to the proxy, and from the proxy to the decoder side. - The decoder should reuse these results and skip redundant tokenization. - **Reuse First Token Generation:** - Pass the first generated token from the prefill side to the proxy and then to the decod...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: re]: Optimize Tokenization and First Token Generation Redundancy Between Prefill and Decode Stages in Disaggregated Prefill feature request;stale ### 🚀 The feature, motivation and pitch ### Background In the current vLL...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: oints offer clear optimization opportunities for improved efficiency and latency in the disaggregated prefill design. ### Proposal - **Reuse Tokenization Results:** - Pass tokenization results from the prefill side to t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ion Both points offer clear optimization opportunities for improved efficiency and latency in the disaggregated prefill design. ### Proposal - **Reuse Tokenization Results:** - Pass tokenization results from the prefill...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ion and pitch ### Background In the current vLLM disaggregated prefill architecture, the workflow is as follows: - The prefill side receives an input request, performs tokenization, generates the first token via inferen...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: generates the first token via inference, and produces the corresponding KV cache. - The decode side then receives the same request, re-tokenizes the input, fetches the KV cache, and starts inference again from the first...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
