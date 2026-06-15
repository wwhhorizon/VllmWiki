# vllm-project/vllm#11322: [Usage]: I want to use guided-decoding,chunked-prefill, and prefix-caching simultaneously in multimodal model. What parameters do I need to pass during startup?

| 字段 | 值 |
| --- | --- |
| Issue | [#11322](https://github.com/vllm-project/vllm/issues/11322) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: I want to use guided-decoding,chunked-prefill, and prefix-caching simultaneously in multimodal model. What parameters do I need to pass during startup?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I observed that when using the multimodal model, V0 does not support prefix-caching, while V1 does not support guided-decoding. Regardless of whether it's V0 or V1, using chunked-prefill causes the service to crash. How should I modify the startup parameters? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: se guided-decoding,chunked-prefill, and prefix-caching simultaneously in multimodal model. What parameters do I need to pass during startup? usage ### Your current environment ```text The output of `python collect_env.p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rs? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: I want to use guided-decoding,chunked-prefill, and prefix-caching simultaneously in multimodal model. What parameters do I need to pass during startup? usage ### Your current environment ```text The output of `...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
