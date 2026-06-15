# vllm-project/vllm#25377: [Feature]: Add ViT memory/latency metrics, LLM prefill/decode latency, and TTFT tracing with environment switches

| 字段 | 值 |
| --- | --- |
| Issue | [#25377](https://github.com/vllm-project/vllm/issues/25377) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add ViT memory/latency metrics, LLM prefill/decode latency, and TTFT tracing with environment switches

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Background To profile and tune multimodal (ViT) + LLM pipelines on Ascend, we need first-class metrics for: - ViT (multimodal encoder) memory requirement - ViT latency - LLM prefill and decode latency - TTFT (Time-To-First-Token) This issue documents the instrumentation added in `model_runner_v1.py`, the log formats, and how to enable them via environment variables. https://github.com/hsliuustc0106/vllm-ascend/pull/11 ## What’s Instrumented 1) ViT (multimodal encoder) memory usage - Aggregated per encoder group (grouped by modality and batchable items). - Reports: - peak_MB_max: peak allocated memory (best estimate of peak within the measurement window). - delta_MB_total: total net allocation delta accumulated across steps. - avg_delta: average delta per observation. - alloc_after_MB_last: allocated memory right after the last measurement. 2) ViT latency - Per encoder group latency using device-side timing events. - Log line: “[MM] Image Encoding Time (group items=N): X.XXX ms” 3) LLM prefill and decode latency - Prefill phase (Prefill/PrefillCacheHit/ChunkedPrefill): - Device time (events) and wall time (host perf counter with stream syn...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: Add ViT memory/latency metrics, LLM prefill/decode latency, and TTFT tracing with environment switches feature request ### 🚀 The feature, motivation and pitch ## Background To profile and tune multimodal (ViT...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: rve /path/to/model --port 5580 --host 0.0.0.0 \ --max-num-seqs 128 --dtype bfloat16 --max-model-len 8192 \ --no-enable-prefix-caching --trust-remote-code -tp 1 \ --gpu-memory-utilization 0.93 \ --no-enable-chunked-prefi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: # 🚀 The feature, motivation and pitch ## Background To profile and tune multimodal (ViT) + LLM pipelines on Ascend, we need first-class metrics for: - ViT (multimodal encoder) memory requirement - ViT latency - LLM pref...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Feature]: Add ViT memory/latency metrics, LLM prefill/decode latency, and TTFT tracing with environment switches feature request ### 🚀 The feature, motivation and pitch ## Background To profile and tune multimodal (ViT...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Add ViT memory/latency metrics, LLM prefill/decode latency, and TTFT tracing with environment switches feature request ### 🚀 The feature, motivation and pitch ## Background To profile and tune multimodal (ViT) + LLM pip...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
