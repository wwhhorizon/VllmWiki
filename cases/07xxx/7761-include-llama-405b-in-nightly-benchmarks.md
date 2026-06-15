# vllm-project/vllm#7761: Include Llama-405B in nightly benchmarks?

| 字段 | 值 |
| --- | --- |
| Issue | [#7761](https://github.com/vllm-project/vllm/issues/7761) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Include Llama-405B in nightly benchmarks?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Include the Llama-405B model as part of the nightly performance benchmarks here: https://buildkite.com/vllm/performance-benchmark/builds/4068 Is the reason for not doing so primarily cost (16-24 H100s needed)? If so Akash.Network would consider providing the infra for it. Thanks! ### Alternatives Running the benchmarks ourselves ### Additional context We’ve been trying to run Llama-405B-FP8 in production (with vLLM + Ray) and have been encountering stability issues with it.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Include Llama-405B in nightly benchmarks? feature request;stale ### 🚀 The feature, motivation and pitch Include the Llama-405B model as part of the nightly performance benchmarks here: https://buildkite.com/vllm/perform...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Include Llama-405B in nightly benchmarks? feature request;stale ### 🚀 The feature, motivation and pitch Include the Llama-405B model as part of the nightly performance benchmarks here: https://buildkite.com/vllm/perform...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: a-405B model as part of the nightly performance benchmarks here: https://buildkite.com/vllm/performance-benchmark/builds/4068 Is the reason for not doing so primarily cost (16-24 H100s needed)? If so Akash.Network would...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ourselves ### Additional context We’ve been trying to run Llama-405B-FP8 in production (with vLLM + Ray) and have been encountering stability issues with it.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: chmark/builds/4068 Is the reason for not doing so primarily cost (16-24 H100s needed)? If so Akash.Network would consider providing the infra for it. Thanks! ### Alternatives Running the benchmarks ourselves ### Additio...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
