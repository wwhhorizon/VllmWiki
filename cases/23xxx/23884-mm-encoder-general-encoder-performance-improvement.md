# vllm-project/vllm#23884: [MM Encoder] General encoder performance improvement

| 字段 | 值 |
| --- | --- |
| Issue | [#23884](https://github.com/vllm-project/vllm/issues/23884) |
| 状态 | closed |
| 标签 | help wanted;good first issue;feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [MM Encoder] General encoder performance improvement

### Issue 正文摘录

### 🚀 The feature, motivation and pitch On vLLM, most multimodal model support was directly contributed by the model vendors, but sometimes the implementation can still be improved in terms of inference performance (e.g, by leveraging fused operations or avoid cumemcpy). Two examples are - https://github.com/vllm-project/vllm/pull/22792 - https://github.com/vllm-project/vllm/pull/22184 We should more actively hunt for such improvement, in particular for more popular models such as Qwen2.5VL, InternVL, GLM4.5V, etc. It should be also made sure that such improvement does not result in accuracy regression. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ure request;stale ### 🚀 The feature, motivation and pitch On vLLM, most multimodal model support was directly contributed by the model vendors, but sometimes the implementation can still be improved in terms of inferenc...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: tc. It should be also made sure that such improvement does not result in accuracy regression. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ral encoder performance improvement help wanted;good first issue;feature request;stale ### 🚀 The feature, motivation and pitch On vLLM, most multimodal model support was directly contributed by the model vendors, but so...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: tc. It should be also made sure that such improvement does not result in accuracy regression. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
