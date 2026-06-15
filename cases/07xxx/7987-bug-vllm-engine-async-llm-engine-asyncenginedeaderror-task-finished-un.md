# vllm-project/vllm#7987: [Bug]: vllm.engine.async_llm_engine.AsyncEngineDeadError: Task finished unexpectedly.

| 字段 | 值 |
| --- | --- |
| Issue | [#7987](https://github.com/vllm-project/vllm/issues/7987) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm.engine.async_llm_engine.AsyncEngineDeadError: Task finished unexpectedly.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have tried: 1. --enforce-eager 2. --disable-frontend-multiprocessing 3. --disable-custom-all-reduce 4. --distributed-executor-backend mp however, no one is working.. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: multiprocessing 3. --disable-custom-all-reduce 4. --distributed-executor-backend mp however, no one is working.. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: g.. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e.async_llm_engine.AsyncEngineDeadError: Task finished unexpectedly. bug;stale ### Your current environment ### 🐛 Describe the bug I have tried: 1. --enforce-eager 2. --disable-frontend-multiprocessing 3. --disable-cust...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
