# vllm-project/vllm#13953: [Feature]: Add Jump-Forward support for Guided Decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#13953](https://github.com/vllm-project/vllm/issues/13953) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add Jump-Forward support for Guided Decoding

### Issue 正文摘录

## Motivation Currently, vLLM use FSM to implement guided decoding with backends such as `outlines`. However, the FSM is constructed at the token level, it can transition the state by only one token at each step. Consequently, it can decode only one token at a time, which results in slow decoding. In my experiment, the inference speed is too slow (`0.89 toks/s`) with `Qwen2.5-7B-Instruct` on my npu device. Would you mind community contributors to introduce **Jump-Forward Decoding** proposed by SGLang? ### Additional context Find more details about Jump-Forward Decoding [ here ](https://lmsys.org/blog/2024-02-05-compressed-fsm/). Related issues: #13821 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: for Guided Decoding feature request ## Motivation Currently, vLLM use FSM to implement guided decoding with backends such as `outlines`. However, the FSM is constructed at the token level, it can transition the state by...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add Jump-Forward support for Guided Decoding feature request ## Motivation Currently, vLLM use FSM to implement guided decoding with backends such as `outlines`. However, the FSM is constructed at the token l...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ## Motivation Currently, vLLM use FSM to implement guided decoding with backends such as `outlines`. However, the FSM is constructed at the token level, it can transition the state by only one token at each step. Conseq...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: In my experiment, the inference speed is too slow (`0.89 toks/s`) with `Qwen2.5-7B-Instruct` on my npu device. Would you mind community contributors to introduce **Jump-Forward Decoding** proposed by SGLang? ### Additio...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
