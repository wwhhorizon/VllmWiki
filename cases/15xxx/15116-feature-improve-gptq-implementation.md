# vllm-project/vllm#15116: [Feature]: Improve GPTQ implementation

| 字段 | 值 |
| --- | --- |
| Issue | [#15116](https://github.com/vllm-project/vllm/issues/15116) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Improve GPTQ implementation

### Issue 正文摘录

### 🚀 The feature, motivation and pitch As we all know, quantizing some layers in the model will cause a large loss of accuracy. When using the AWQ algorithm, you can use the **modules_to_not_convert** attribute to avoid quantizing some layers. If the same function is also available in the GPTQ algorithm, I think it will be very convenient. ### Alternatives I have pull a request [#12103](https://github.com/vllm-project/vllm/pull/12103) ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Improve GPTQ implementation feature request;stale ### 🚀 The feature, motivation and pitch As we all know, quantizing some layers in the model will cause a large loss of accuracy. When using the AWQ algorithm,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: all know, quantizing some layers in the model will cause a large loss of accuracy. When using the AWQ algorithm, you can use the **modules_to_not_convert** attribute to avoid quantizing some layers. If the same function...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: all know, quantizing some layers in the model will cause a large loss of accuracy. When using the AWQ algorithm, you can use the **modules_to_not_convert** attribute to avoid quantizing some layers. If the same function...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: e request;stale ### 🚀 The feature, motivation and pitch As we all know, quantizing some layers in the model will cause a large loss of accuracy. When using the AWQ algorithm, you can use the **modules_to_not_convert** a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
