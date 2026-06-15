# vllm-project/vllm#39060: [Feature]: Speculative Prefill — Draft-Assisted Sparse Prefill for TTFT Reduction

| 字段 | 值 |
| --- | --- |
| Issue | [#39060](https://github.com/vllm-project/vllm/issues/39060) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;fp8;moe;sampling |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Speculative Prefill — Draft-Assisted Sparse Prefill for TTFT Reduction

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Summary Add speculative prefill (aka sparse prefill) support to vLLM: use a lightweight draft model to score prompt token importance via attention patterns, then prefill only the top-k% most important tokens into the target model with position-preserving RoPE. This directly reduces TTFT, which is the primary latency bottleneck for long-context serving. ### Motivation TTFT scales linearly (or worse, due to O(n²) attention) with prompt length and is the dominant latency bottleneck for long-context workloads — coding assistants, document analysis, RAG with large retrieval contexts, and agentic tool-use pipelines. A 64K-token prompt on a 122B MoE model can take 7+ minutes to first token on consumer hardware, and even on datacenter GPUs the prefill phase dominates end-to-end latency at high concurrency. vLLM already has complementary prefill optimizations — chunked prefill and disaggregated prefill — but both process **all** prompt tokens. Speculative prefill is orthogonal: it reduces the **number of tokens** the target model must prefill, and composes with both chunked and disaggregated prefill. ### Prior Art **Academic + reference implement...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Feature]: Speculative Prefill — Draft-Assisted Sparse Prefill for TTFT Reduction feature request ### 🚀 The feature, motivation and pitch ### Summary Add speculative prefill (aka sparse prefill) support to vLLM: use a l...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: sition-preserving RoPE. This directly reduces TTFT, which is the primary latency bottleneck for long-context serving. ### Motivation TTFT scales linearly (or worse, due to O(n²) attention) with prompt length and is the...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: imary latency bottleneck for long-context serving. ### Motivation TTFT scales linearly (or worse, due to O(n²) attention) with prompt length and is the dominant latency bottleneck for long-context workloads — coding ass...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ll) support to vLLM: use a lightweight draft model to score prompt token importance via attention patterns, then prefill only the top-k% most important tokens into the target model with position-preserving RoPE. This di...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ve prefill (aka sparse prefill) support to vLLM: use a lightweight draft model to score prompt token importance via attention patterns, then prefill only the top-k% most important tokens into the target model with posit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
