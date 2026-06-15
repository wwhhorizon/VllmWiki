# vllm-project/vllm#19342: [Usage]: How to get the router logits for an MoE model?

| 字段 | 值 |
| --- | --- |
| Issue | [#19342](https://github.com/vllm-project/vllm/issues/19342) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to get the router logits for an MoE model?

### Issue 正文摘录

### How would you like to use vllm I would like to run a Qwen/Qwen3-30B-A3B model and need to store the router logits for each prompt in order to calculate the usage balance among experts. Is there a recommended or efficient way to implement this? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Usage]: How to get the router logits for an MoE model? usage;stale ### How would you like to use vllm I would like to run a Qwen/Qwen3-30B-A3B model and need to store the router logits for each prompt in order to calcu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: How to get the router logits for an MoE model? usage;stale ### How would you like to use vllm I would like to run a Qwen/Qwen3-30B-A3B model and need to store the router logits for each prompt in order to calcu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: calculate the usage balance among experts. Is there a recommended or efficient way to implement this? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: is? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: How to get the router logits for an MoE model? usage;stale ### How would you like to use vllm I would like to run a Qwen/Qwen3-30B-A3B model and need to store the router logits for each prompt in order to calcu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
