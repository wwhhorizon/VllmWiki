# vllm-project/vllm#10748: [Feature]: Energy consumption of individual requests

| 字段 | 值 |
| --- | --- |
| Issue | [#10748](https://github.com/vllm-project/vllm/issues/10748) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Energy consumption of individual requests

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Some customers want to know about the energy consumption of individual requests. They would like to get the energy used directly with the outputs (similar in the idea to how [Ecologits](https://ecologits.ai/latest/#usage-example) is returning the estimations that it computes). The goal is to return the amount of energy that has been measured on the hardware that really generated the output, and not an estimation. Are you aware of other works in this area ? I guess it should be implemented via the plugin framework ? ### Alternatives Using a proxy architecture with something [LiteLLM](https://docs.litellm.ai/docs/#basic-usage)-like along with an energy-collecting tool could be an option. However, considering the generation is likely distributed, it cannot be done in front of vllm and must be included in the lower layers so that the measurement is done at the task level, on the host that is actually generating the output. ### Additional context We already do have some tooling available in the OSS community in order to get energy information from the hardware ([CodeCarbon](https://codecarbon.io/), [Scaphandre](https://github.com/hubblo-org/scaph...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Energy consumption of individual requests feature request;stale ### 🚀 The feature, motivation and pitch Some customers want to know about the energy consumption of individual requests. They would like to get...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: implemented via the plugin framework ? ### Alternatives Using a proxy architecture with something [LiteLLM](https://docs.litellm.ai/docs/#basic-usage)-like along with an energy-collecting tool could be an option. Howeve...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ave some tooling available in the OSS community in order to get energy information from the hardware ([CodeCarbon](https://codecarbon.io/), [Scaphandre](https://github.com/hubblo-org/scaphandre), [Alumet](https://alumet...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: e outputs (similar in the idea to how [Ecologits](https://ecologits.ai/latest/#usage-example) is returning the estimations that it computes). The goal is to return the amount of energy that has been measured on the hard...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
