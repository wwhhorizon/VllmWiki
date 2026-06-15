# vllm-project/vllm#40315: [Bug]: DeepSeek-V3.2 DSA MFU bug

| 字段 | 值 |
| --- | --- |
| Issue | [#40315](https://github.com/vllm-project/vllm/issues/40315) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: DeepSeek-V3.2 DSA MFU bug

### Issue 正文摘录

### Your current environment vLLM-0.17.0 ### 🐛 Describe the bug Bug: vLLM MFU metric overestimates for DeepSeek-V3.2 sparse attention (Indexer) Summary The MFU metric reported by vLLM 0.17.0 is an analytic FLOPs throughput estimate, not a hardware measurement. For DeepSeek-V3.2, which uses sparse attention via SparseAttnIndexer (index_topk), the estimator still computes attention FLOPs using the dense QK/AV formula. This overestimates the numerator, causing MFU to exceed 100% in some cases. Root Cause vllm/v1/metrics/perf.py:5 explicitly defines MFU as analytic flops estimation Attention FLOPs are calculated using dense formula at perf.py:421-422, without accounting for index_topk or sparse attention ratios At runtime, the model reads index_topk (deepseek_v2.py:615), switches to the Indexer sparse path (deepseek_v2.py:922,931), and executes top_k_per_row_prefill/decode (sparse_attn_indexer.py:138,223) with FP8 sparse attention (flashmla_sparse.py:52) The estimator uses full attention FLOPs; the kernel computes only top-k → numerator is inflated Numerical Evidence From H20 prefill test (TP=2 DP=8): Metric Sample A Sample B Ratio MFU (TF/s/GPU) 360.0 216.0 1.6667 Prompt throughput (...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: DeepSeek-V3.2, which uses sparse attention via SparseAttnIndexer (index_topk), the estimator still computes attention FLOPs using the dense QK/AV formula. This overestimates the numerator, causing MFU to exceed 100% in...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: attention FLOPs; the kernel computes only top-k → numerator is inflated Numerical Evidence From H20 prefill test (TP=2 DP=8): Metric Sample A Sample B Ratio MFU (TF/s/GPU) 360.0 216.0 1.6667 Prompt throughput (tok/s) 20...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: out accounting for index_topk or sparse attention ratios At runtime, the model reads index_topk (deepseek_v2.py:615), switches to the Indexer sparse path (deepseek_v2.py:922,931), and executes top_k_per_row_prefill/deco...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Indexer sparse path (deepseek_v2.py:922,931), and executes top_k_per_row_prefill/decode (sparse_attn_indexer.py:138,223) with FP8 sparse attention (flashmla_sparse.py:52) The estimator uses full attention FLOPs; the ker...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: xer) Summary The MFU metric reported by vLLM 0.17.0 is an analytic FLOPs throughput estimate, not a hardware measurement. For DeepSeek-V3.2, which uses sparse attention via SparseAttnIndexer (index_topk), the estimator...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
