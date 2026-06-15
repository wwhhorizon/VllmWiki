# vllm-project/vllm#24748: [New Model]: KOSMOS2.5 IMPLEMENTATION

| 字段 | 值 |
| --- | --- |
| Issue | [#24748](https://github.com/vllm-project/vllm/issues/24748) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: KOSMOS2.5 IMPLEMENTATION

### Issue 正文摘录

### 🚀 The feature, motivation and pitch KOSMOS-2.5 has recently been implemented into the transformers library. It would be great to have support for it in vLLM as well. This would allow leveraging vLLM’s optimized inference capabilities for KOSMOS-2.5, especially for multimodal tasks where performance and efficiency are crucial. Adding this integration would enable the community to use KOSMOS-2.5 at scale with lower latency and memory efficiency, similar to other models already supported by vLLM. ### Alternatives Use the transformers implementation directly, but this comes with significant overhead compared to vLLM. Write custom adapters for KOSMOS-2.5 in vLLM, but this is less maintainable than official support. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [New Model]: KOSMOS2.5 IMPLEMENTATION new-model;stale ### 🚀 The feature, motivation and pitch KOSMOS-2.5 has recently been implemented into the transformers library. It would be great to have support for it in vLLM as w...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: KOSMOS2.5 IMPLEMENTATION new-model;stale ### 🚀 The feature, motivation and pitch KOSMOS-2.5 has recently been implemented into the transformers library. It would be great to have support for it in vLLM as w...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: gration would enable the community to use KOSMOS-2.5 at scale with lower latency and memory efficiency, similar to other models already supported by vLLM. ### Alternatives Use the transformers implementation directly, b...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: w leveraging vLLM’s optimized inference capabilities for KOSMOS-2.5, especially for multimodal tasks where performance and efficiency are crucial. Adding this integration would enable the community to use KOSMOS-2.5 at...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: Adding this integration would enable the community to use KOSMOS-2.5 at scale with lower latency and memory efficiency, similar to other models already supported by vLLM. ### Alternatives Use the transformers implementa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
