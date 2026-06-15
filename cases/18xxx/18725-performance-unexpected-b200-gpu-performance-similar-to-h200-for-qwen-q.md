# vllm-project/vllm#18725: [Performance]: Unexpected: B200 GPU Performance Similar to H200 for Qwen/QwQ-32B, Expected B200 to be Significantly Faster

| 字段 | 值 |
| --- | --- |
| Issue | [#18725](https://github.com/vllm-project/vllm/issues/18725) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Unexpected: B200 GPU Performance Similar to H200 for Qwen/QwQ-32B, Expected B200 to be Significantly Faster

### Issue 正文摘录

### Proposal to improve performance We are observing that the B200 GPU is performing similarly to the H200 GPU when running inference with the `Qwen/QwQ-32B` model using vLLM. We expect the B200 to have significantly better performance. **Hardware Information:** * CPU: 192 x vCPU * Memory: 1585 GB **Benchmark Script:** ```bash vllm serve Qwen/QwQ-32B ``` ```bash python3 ./vllm/benchmarks/benchmark_serving.py \ --backend vllm \ --model Qwen/QwQ-32B \ --max-concurrency 1 \ --base-url http://127.0.0.1:8000 \ --endpoint /v1/completions \ --dataset-name sharegpt \ --dataset-path ./ShareGPT_V3_unfiltered_cleaned_split.json \ --num-prompts 10 ``` **Performance Metrics:** **H200 (8x H200 QwQ-32B elaich/simple-vllm-launcher):** ``` ============ Serving Benchmark Result ============ Successful requests: 10 Benchmark duration (s): 23.10 Total input tokens: 1374 Total generated tokens: 2663 Request throughput (req/s): 0.43 Output token throughput (tok/s): 115.31 Total Token throughput (tok/s): 174.80 ---------------Time to First Token---------------- Mean TTFT (ms): 585.38 Median TTFT (ms): 594.23 P99 TTFT (ms): 615.97 -----Time per Output Token (excl. 1st token)------ Mean TPOT (ms): 6.70 Me...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: PU should exhibit significantly higher throughput (tok/s) and lower latencies (TTFT, TPOT, ITL) compared to the H200 GPU. **Actual Behavior:** The performance metrics for both GPUs are very similar, with the B200 showin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Performance]: Unexpected: B200 GPU Performance Similar to H200 for Qwen/QwQ-32B, Expected B200 to be Significantly Faster performance;stale ### Proposal to improve performance We are observing that the B200 GPU is perf...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: . **Hardware Information:** * CPU: 192 x vCPU * Memory: 1585 GB **Benchmark Script:** ```bash vllm serve Qwen/QwQ-32B ``` ```bash python3 ./vllm/benchmarks/benchmark_serving.py \ --backend vllm \ --model Qwen/QwQ-32B \...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Performance]: Unexpected: B200 GPU Performance Similar to H200 for Qwen/QwQ-32B, Expected B200 to be Significantly Faster performance;stale ### Proposal to improve performance We are observing that the B200 GPU is perf...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: 0 for Qwen/QwQ-32B, Expected B200 to be Significantly Faster performance;stale ### Proposal to improve performance We are observing that the B200 GPU is performing similarly to the H200 GPU when running inference with t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
