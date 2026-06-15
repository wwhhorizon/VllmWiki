# vllm-project/vllm#15167: [Bug]: vllm:request_inference_time_seconds_bucket has too few buckets for long inference requests

| 字段 | 值 |
| --- | --- |
| Issue | [#15167](https://github.com/vllm-project/vllm/issues/15167) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm:request_inference_time_seconds_bucket has too few buckets for long inference requests

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Very long running tail requests aganist vllm report a p99 tail latency of 60s, when the real value is often much higher. The `request_latency_buckets` for inference_time_request histogram cap at 60s, but there are many requests to a large language model that could take in significant excess of this. In practice folks use p90 and p99 on histograms to understand the latency buckets, but the top bucket limits how high the quantile estimation algorithm can go. In general, the highest bucket should encompass the reasonable p99 distribution, and prometheus recommends: > Pick buckets suitable for the expected range of observed values in https://prometheus.io/docs/practices/histograms/#quantiles I would suggest adding at least 3 more exponential buckets - 120s, 240s, 480s - which means vllm out of the box would support p99 estimation for 8m and below. I have not heard of someone running requests longer than 8m, but it might be possible - so adding 960s (16m) would catch that. I think it is reasonable to do that for all histogram metrics - this is a core golden signal (latency distribution) and so spending a slightly larger amount of spac...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: st. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: vllm:request_inference_time_seconds_bucket has too few buckets for long inference requests bug ### Your current environment ### 🐛 Describe the bug Very long running tail requests aganist vllm report a p99 tail la...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: the bug Very long running tail requests aganist vllm report a p99 tail latency of 60s, when the real value is often much higher. The `request_latency_buckets` for inference_time_request histogram cap at 60s, but there a...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf;slowdown env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
