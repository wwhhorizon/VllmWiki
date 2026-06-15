# vllm-project/vllm#22193: [Usage]: ValueError: Head size 40 is not supported by MLACommon. Supported head sizes are: [576]. Set VLLM_ATTENTION_BACKEND=FLEX_ATTENTION to use FlexAttention backend which supports all head sizes.

| 字段 | 值 |
| --- | --- |
| Issue | [#22193](https://github.com/vllm-project/vllm/issues/22193) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: ValueError: Head size 40 is not supported by MLACommon. Supported head sizes are: [576]. Set VLLM_ATTENTION_BACKEND=FLEX_ATTENTION to use FlexAttention backend which supports all head sizes.

### Issue 正文摘录

VLLM_ATTENTION_BACKEND=FLEX_ATTENTION has been set, but take no effect ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ported by MLACommon. Supported head sizes are: [576]. Set VLLM_ATTENTION_BACKEND=FLEX_ATTENTION to use FlexAttention backend which supports all head sizes. usage;stale VLLM_ATTENTION_BACKEND=FLEX_ATTENTION has been set,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ect ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ENTION to use FlexAttention backend which supports all head sizes. usage;stale VLLM_ATTENTION_BACKEND=FLEX_ATTENTION has been set, but take no effect ### Before submitting a new issue... - [x] Make sure you already sear...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
