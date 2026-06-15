# vllm-project/vllm#12039: [Misc]: For disaggregated prefill with multiple decode instances, drop_select might not enough

| 字段 | 值 |
| --- | --- |
| Issue | [#12039](https://github.com/vllm-project/vllm/issues/12039) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: For disaggregated prefill with multiple decode instances, drop_select might not enough

### Issue 正文摘录

### Anything you want to discuss about vllm. I come here from https://docs.vllm.ai/en/latest/features/disagg_prefill.html. In the current disaggregated prefill architecture, the decode instance will call drop_select to get the kvcache. However, if multiple decode instances are supported in the coming future, we may need to support retrying the decode instance if the used one is down, which means we need to keep the kvcache and allow retransmitting when a new decode instance is selected. IMHO, we can provide a separate drop API, which will be called at the end of the request so the kvcache can be released (or reduce the reference) when the inference ends. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Misc]: For disaggregated prefill with multiple decode instances, drop_select might not enough stale ### Anything you want to discuss about vllm. I come here from https://docs.vllm.ai/en/latest/features/disagg_prefill.h...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: atest/features/disagg_prefill.html. In the current disaggregated prefill architecture, the decode instance will call drop_select to get the kvcache. However, if multiple decode instances are supported in the coming futu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: want to discuss about vllm. I come here from https://docs.vllm.ai/en/latest/features/disagg_prefill.html. In the current disaggregated prefill architecture, the decode instance will call drop_select to get the kvcache....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
