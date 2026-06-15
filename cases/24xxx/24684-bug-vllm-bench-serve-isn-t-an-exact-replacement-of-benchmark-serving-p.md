# vllm-project/vllm#24684: [Bug]: `vllm bench serve` isn't an exact replacement of benchmark_serving.py

| 字段 | 值 |
| --- | --- |
| Issue | [#24684](https://github.com/vllm-project/vllm/issues/24684) |
| 状态 | closed |
| 标签 | bug;good first issue |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: `vllm bench serve` isn't an exact replacement of benchmark_serving.py

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Starting with #24411 the benchmark_serving.py is deprecated in favor of vllm bench serve, but the replacement produces different results on the same config Sample config: On `vllm/vllm-openai:latest`, H100 machine While running the server as `vllm serve meta-llama/Llama-3.1-8B-Instruct --no-enable-prefix-caching` Using `vllm bench serve --model meta-llama/Llama-3.1-8B-Instruct --percentile-metrics ttft,tpot,itl,e2el --dataset-path /models/ShareGPT_Vicuna_unfiltered/ShareGPT_V3_unfiltered_cleaned_split.json --max-concurrency 64 --num-prompts 640 --ignore-eos --sharegpt-output-len 512` produces ``` ============ Serving Benchmark Result ============ Successful requests: 640 Maximum request concurrency: 64 Benchmark duration (s): 29.23 Total input tokens: 654052 Total generated tokens: 81920 Request throughput (req/s): 21.89 Output token throughput (tok/s): 2802.42 Total Token throughput (tok/s): 25177.00 ---------------Time to First Token---------------- Mean TTFT (ms): 579.39 Median TTFT (ms): 582.78 P99 TTFT (ms): 1584.13 -----Time per Output Token (excl. 1st token)------ Mean TPOT (ms): 18.41 Median TPOT (ms): 18.33 P99 TPOT (ms)...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Bug]: `vllm bench serve` isn't an exact replacement of benchmark_serving.py bug;good first issue ### Your current environment ### 🐛 Describe the bug Starting with #24411 the benchmark_serving.py is deprecated in favor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: results on the same config Sample config: On `vllm/vllm-openai:latest`, H100 machine While running the server as `vllm serve meta-llama/Llama-3.1-8B-Instruct --no-enable-prefix-caching` Using `vllm bench serve --model m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: bench serve, but the replacement produces different results on the same config Sample config: On `vllm/vllm-openai:latest`, H100 machine While running the server as `vllm serve meta-llama/Llama-3.1-8B-Instruct --no-enab...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: oduces ``` ============ Serving Benchmark Result ============ Successful requests: 640 Maximum request concurrency: 64 Benchmark duration (s): 29.23 Total input tokens: 654052 Total generated tokens: 81920

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
