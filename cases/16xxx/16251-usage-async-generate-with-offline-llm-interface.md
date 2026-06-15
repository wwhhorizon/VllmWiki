# vllm-project/vllm#16251: [Usage]: Async generate with offline LLM interface

| 字段 | 值 |
| --- | --- |
| Issue | [#16251](https://github.com/vllm-project/vllm/issues/16251) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Async generate with offline LLM interface

### Issue 正文摘录

### Your current environment Based on version 0.8.2. ### How would you like to use vllm The background is that we hope to introduce async generate for RL rollout since different requests can call external function at different time and end up with different times of turns. Async generate can help process each request independently and reduce the latency. AsyncLLM is suitable for this, but currently verl only supports online parameter updating based on `LLM`, see [here](https://github.com/volcengine/verl/blob/main/verl/workers/sharding_manager/fsdp_vllm.py#L95-L104). So I wanna if `LLM` interface supports async generate. Or is there any idea we can access the weights of AsyncLLM's model executor. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Async generate with offline LLM interface usage;stale ### Your current environment Based on version 0.8.2. ### How would you like to use vllm The background is that we hope to introduce async generate for RL ro...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: sync generate can help process each request independently and reduce the latency. AsyncLLM is suitable for this, but currently verl only supports online parameter updating based on `LLM`, see [here](https://github.com/v...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: offline LLM interface usage;stale ### Your current environment Based on version 0.8.2. ### How would you like to use vllm The background is that we hope to introduce async generate for RL rollout since different request...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: or. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: c generate. Or is there any idea we can access the weights of AsyncLLM's model executor. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
