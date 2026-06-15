# vllm-project/vllm#27245: [Bug]: High Latency in One-Time Scenarios for DeepSeek Deployed on H200

| 字段 | 值 |
| --- | --- |
| Issue | [#27245](https://github.com/vllm-project/vllm/issues/27245) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: High Latency in One-Time Scenarios for DeepSeek Deployed on H200

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In one-time scenarios, the end-to-end (E2E) latency is normal. However, the latency of Http_Request_Duration is relatively high, which results in significant latency experienced by users for their requests. I would like to know whether anyone has encountered this issue or how to troubleshoot it. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: it. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: os, the end-to-end (E2E) latency is normal. However, the latency of Http_Request_Duration is relatively high, which results in significant latency experienced by users for their requests. I would like to know whether an...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: High Latency in One-Time Scenarios for DeepSeek Deployed on H200 bug ### Your current environment ### 🐛 Describe the bug In one-time scenarios, the end-to-end (E2E) latency is normal. However, the latency of Http...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf;slowdown env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
