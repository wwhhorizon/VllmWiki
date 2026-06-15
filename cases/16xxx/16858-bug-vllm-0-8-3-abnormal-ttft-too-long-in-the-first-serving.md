# vllm-project/vllm#16858: [Bug]: vllm 0.8.3 abnormal TTFT (too long) in the first serving

| 字段 | 值 |
| --- | --- |
| Issue | [#16858](https://github.com/vllm-project/vllm/issues/16858) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: vllm 0.8.3 abnormal TTFT (too long) in the first serving

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When the benchmark_serving.py is started for the first time of an num_prompt, the TTFT is very long. It will be much better the second time. - the first time ```text ============ Serving Benchmark Result ============ Successful requests: 10 Benchmark duration (s): 8.85 Total input tokens: 3354 Total generated tokens: 1200 Request throughput (req/s): 1.13 Output token throughput (tok/s): 135.58 Total Token throughput (tok/s): 514.51 ---------------Time to First Token---------------- Mean TTFT (ms): 361.76 Median TTFT (ms): 421.65 P99 TTFT (ms): 709.10 -----Time per Output Token (excl. 1st token)------ Mean TPOT (ms): 29.22 Median TPOT (ms): 29.21 P99 TPOT (ms): 32.98 ---------------Inter-token Latency---------------- Mean ITL (ms): 32.65 Median ITL (ms): 27.44 P99 ITL (ms): 231.45 ================================================== ``` - the second time ```text ============ Serving Benchmark Result ============ Successful requests: 10 Benchmark duration (s): 8.79 Total input tokens: 3354 Total generated tokens: 1200 Request throughput (req/s): 1.14 Output token throughput (tok/s): 136.47 Total Token throughput (tok/s): 517.91 -----...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: ng bug ### Your current environment ### 🐛 Describe the bug When the benchmark_serving.py is started for the first time of an num_prompt, the TTFT is very long. It will be much better the second time. - the first time ``...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: me ```text ============ Serving Benchmark Result ============ Successful requests: 10 Benchmark duration (s): 8.85 Total input tokens: 3354 Total generated tokens: 1200 Request throughput (req
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf;slowdown env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
