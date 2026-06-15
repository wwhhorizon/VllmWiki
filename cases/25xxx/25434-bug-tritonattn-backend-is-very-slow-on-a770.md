# vllm-project/vllm#25434: [Bug]: TritonAttn Backend is very slow on A770

| 字段 | 值 |
| --- | --- |
| Issue | [#25434](https://github.com/vllm-project/vllm/issues/25434) |
| 状态 | closed |
| 标签 | bug;intel-gpu;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TritonAttn Backend is very slow on A770

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When "VLLM_ATTENTION_BACKEND=TRITON_ATTN_VLLM_V1" is set, vLLM runs very slowly: ``` ============ Serving Benchmark Result ============ Successful requests: 100 Benchmark duration (s): 509.37 Total input tokens: 102017 Total generated tokens: 12673 Request throughput (req/s): 0.20 Output token throughput (tok/s): 24.88 Total Token throughput (tok/s): 225.16 ---------------Time to First Token---------------- Mean TTFT (ms): 159865.89 Median TTFT (ms): 157245.90 P99 TTFT (ms): 321174.10 -----Time per Output Token (excl. 1st token)------ Mean TPOT (ms): 2606.34 Median TPOT (ms): 2657.28 P99 TPOT (ms): 3534.94 ---------------Inter-token Latency---------------- Mean ITL (ms): 2606.34 Median ITL (ms): 1751.32 P99 ITL (ms): 6918.84 ================================================== ``` When using FlashAttnBackend: ``` ============ Serving Benchmark Result ============ Successful requests: 100 Benchmark duration (s): 36.24 Total input tokens: 102017 Total generated tokens: 12068 Request throughput (req/s): 2.76 Output token throughput (tok/s): 332.97 Total Token throughput (tok/s): 3147.74 ---------------Time to First Token--------------...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: ON_ATTN_VLLM_V1" is set, vLLM runs very slowly: ``` ============ Serving Benchmark Result ============ Successful requests: 100 Benchmark duration (s): 509.37 Total input tokens: 102017 Total generated tokens: 12673 Re
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf;slowdo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: TritonAttn Backend is very slow on A770 bug;intel-gpu;stale ### Your current environment ### 🐛 Describe the bug When "VLLM_ATTENTION_BACKEND=TRITON_ATTN_VLLM_V1" is set, vLLM runs very slowly: ``` ============ Se...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: TritonAttn Backend is very slow on A770 bug;intel-gpu;stale ### Your current environment ### 🐛 Describe the bug When "VLLM_ATTENTION_BACKEND=TRITON_ATTN_VLLM_V1" is set, vLLM runs very slowly: ``` ============ Se...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
