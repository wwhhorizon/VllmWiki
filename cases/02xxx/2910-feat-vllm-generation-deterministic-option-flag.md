# vllm-project/vllm#2910: [feat] vLLM generation deterministic option/flag

| 字段 | 值 |
| --- | --- |
| Issue | [#2910](https://github.com/vllm-project/vllm/issues/2910) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [feat] vLLM generation deterministic option/flag

### Issue 正文摘录

Hi vllm maintainers, Thanks for the awesome project! I'm wondering is there a deterministic option/flag to let the model generate identical results in different runs with the same prompts? (Also support random and beam search sampler, not only greedy sampler) Does it enough to get deterministic behavior by setting the following random state? I'm not sure what other factors will violate the determinism. ``` torch.manual_seed(seed) np.random.seed(seed) random.seed(seed) torch.use_deterministic_algorithms(True) ``` CC: @WoosukKwon @zhuohan123 @Yard1

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: in different runs with the same prompts? (Also support random and beam search sampler, not only greedy sampler) Does it enough to get deterministic behavior by setting the following random state? I'm not sure what other...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [feat] vLLM generation deterministic option/flag stale Hi vllm maintainers, Thanks for the awesome project! I'm wondering is there a deterministic option/flag to let the model generate identical results in different run...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: project! I'm wondering is there a deterministic option/flag to let the model generate identical results in different runs with the same prompts? (Also support random and beam search sampler, not only greedy sampler) Doe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [feat] vLLM generation deterministic option/flag stale Hi vllm maintainers, Thanks for the awesome project! I'm wondering is there a deterministic option/flag to let the model generate identical results in different run...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [feat] vLLM generation deterministic option/flag stale Hi vllm maintainers, Thanks for the awesome project! I'm wondering is there a deterministic option/flag to let the model generate identical results in different run...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
