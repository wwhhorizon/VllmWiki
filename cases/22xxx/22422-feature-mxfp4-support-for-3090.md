# vllm-project/vllm#22422: [Feature]: mxfp4 support for 3090

| 字段 | 值 |
| --- | --- |
| Issue | [#22422](https://github.com/vllm-project/vllm/issues/22422) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: mxfp4 support for 3090

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Value error, The quantization method mxfp4 is not supported for the current GPU. Minimum capability: 100. Current capability: 86. [type=value_error, input_value=ArgsKwargs((), {'model_co...additional_config': {}}), input_type=ArgsKwargs] ### Alternatives int4 gptq ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Feature]: mxfp4 support for 3090 feature request;stale ### 🚀 The feature, motivation and pitch Value error, The quantization method mxfp4 is not supported for the current GPU. Minimum capability: 100. Current capabilit...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: quantization method mxfp4 is not supported for the current GPU. Minimum capability: 100. Current capability: 86. [type=value_error, input_value=ArgsKwargs((), {'model_co...additional_config': {}}), input_type=ArgsKwargs...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Current capability: 86. [type=value_error, input_value=ArgsKwargs((), {'model_co...additional_config': {}}), input_type=ArgsKwargs] ### Alternatives int4 gptq ### Additional context _No response_ ### Before submitting a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: mxfp4 support for 3090 feature request;stale ### 🚀 The feature, motivation and pitch Value error, The quantization method mxfp4 is not supported for the current GPU. Minimum capability: 100. Current capabilit...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
