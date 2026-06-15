# vllm-project/vllm#25112: [Bug]: [Spec Decode] Spec decoding is not disabled at/after configured batch size

| 字段 | 值 |
| --- | --- |
| Issue | [#25112](https://github.com/vllm-project/vllm/issues/25112) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [Spec Decode] Spec decoding is not disabled at/after configured batch size

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I wanted to use the [`disable_by_batch_size`](https://docs.vllm.ai/en/v0.10.1/api/vllm/config/index.html#vllm.config.SpeculativeConfig.disable_by_batch_size) feature of speculative decoding to maintain throughput at higher batch sizes but I do not see any performance difference with and without the parameter. Upon searching in the vllm github, I see that the [parameter](https://github.com/vllm-project/vllm/blob/main/vllm/config/speculative.py#L83) is nowhere used. Is `disable_by_batch_size` still supported? If not, is there a plan to re-introduce it? It is a very useful feature to prevent throughput regressions at higher batch sizes with spec decoding ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: [Spec Decode] Spec decoding is not disabled at/after configured batch size bug;stale ### Your current environment ### 🐛 Describe the bug I wanted to use the [`disable_by_batch_size`](https://docs.vllm.ai/en/v0.10...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: onfig.disable_by_batch_size) feature of speculative decoding to maintain throughput at higher batch sizes but I do not see any performance difference with and without the parameter. Upon searching in the vllm github, I...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: see any performance difference with and without the parameter. Upon searching in the vllm github, I see that the [parameter](https://github.com/vllm-project/vllm/blob/main/vllm/config/speculative.py#L83) is nowhere used...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: [Spec Decode] Spec decoding is not disabled at/after configured batch size bug;stale ### Your current environment ### 🐛 Describe the bug I wanted to use the [`disable_by_batch_size`](https://docs.vllm.ai/en/v0.10...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
