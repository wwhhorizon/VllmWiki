# vllm-project/vllm#38286: [Feature]: Batch invariance on 3090

| 字段 | 值 |
| --- | --- |
| Issue | [#38286](https://github.com/vllm-project/vllm/issues/38286) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Batch invariance on 3090

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Batch Invariance does not work on the 3090 (two unit tests failing) but in my testing I had managed to run Qwen3-0.6B and get deterministic results. As such I would like to work on getting the failing unit tests passing and batch invariance support on the 3090. This has been discussed briefly with @yewentao256 in #27433. ### Alternatives NA ### Additional context I include here the summary test output, from #27433 [https://github.com/vllm-project/vllm/issues/27433#issuecomment-4137438472](https://github.com/vllm-project/vllm/issues/27433#issuecomment-4137438472) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [Feature]: Batch invariance on 3090 feature request ### 🚀 The feature, motivation and pitch Batch Invariance does not work on the 3090 (two unit tests failing) but in my testing I had managed to run Qwen3-0.6B and get d...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: tivation and pitch Batch Invariance does not work on the 3090 (two unit tests failing) but in my testing I had managed to run Qwen3-0.6B and get deterministic results. As such I would like to work on getting the failing...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 72) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: the 3090 (two unit tests failing) but in my testing I had managed to run Qwen3-0.6B and get deterministic results. As such I would like to work on getting the failing unit tests passing and batch invariance support on t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Batch invariance on 3090 feature request ### 🚀 The feature, motivation and pitch Batch Invariance does not work on the 3090 (two unit tests failing) but in my testing I had managed to run Qwen3-0.6B and get d...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
