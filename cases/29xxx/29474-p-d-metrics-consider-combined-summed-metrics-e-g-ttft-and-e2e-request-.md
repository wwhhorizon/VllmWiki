# vllm-project/vllm#29474: [P/D][Metrics] Consider combined/summed metrics (e.g. ttft and e2e_request_latency) for prefill and decode instances

| 字段 | 值 |
| --- | --- |
| Issue | [#29474](https://github.com/vllm-project/vllm/issues/29474) |
| 状态 | open |
| 标签 | usage;unstale;kv-connector |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [P/D][Metrics] Consider combined/summed metrics (e.g. ttft and e2e_request_latency) for prefill and decode instances

### Issue 正文摘录

### Your current environment ### How would you like to use vllm Hi, team. In the pd-disagg service, the monitoring metrics for both prefill and decode instances include ttft and e2e_request_1atency. For calculating the total TTFT, should they be added together? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [P/D][Metrics] Consider combined/summed metrics (e.g. ttft and e2e_request_latency) for prefill and decode instances usage;unstale;kv-connector ### Your current environment ### How would you like to use vllm Hi, team. I...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: er? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: /D][Metrics] Consider combined/summed metrics (e.g. ttft and e2e_request_latency) for prefill and decode instances usage;unstale;kv-connector ### Your current environment ### How would you like to use vllm Hi, team. In...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
