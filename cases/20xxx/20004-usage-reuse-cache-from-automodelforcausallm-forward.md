# vllm-project/vllm#20004: [Usage]: Reuse cache from AutoModelForCausalLM.forward

| 字段 | 值 |
| --- | --- |
| Issue | [#20004](https://github.com/vllm-project/vllm/issues/20004) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Reuse cache from AutoModelForCausalLM.forward

### Issue 正文摘录

### Your current environment N/A ### How would you like to use vllm Hi, my workflow involves both forwarding the AutoModelForCausalLM model to obtain the accurate log prob, and generating (not extremely long) rollouts. It is like RL with very long prompts. 1. Which is faster, vllm+AutoModelForCausalLM.forward or AutoModelForCausalLM.forward only? If using both, the prompt parts can be calculated twice and are thus inefficient, right? 2. Is there an elegant way to achieve this? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: using both, the prompt parts can be calculated twice and are thus inefficient, right? 2. Is there an elegant way to achieve this? ### Before submitting a new issue... - [x] Make sure you already searched for relevant is...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: is? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: Reuse cache from AutoModelForCausalLM.forward usage;stale ### Your current environment N/A ### How would you like to use vllm Hi, my workflow involves both forwarding the AutoModelForCausalLM model to obtain th...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Reuse cache from AutoModelForCausalLM.forward usage;stale ### Your current environment N/A ### How would you like to use vllm Hi, my workflow involves both forwarding the AutoModelForCausalLM model to obtain th...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
