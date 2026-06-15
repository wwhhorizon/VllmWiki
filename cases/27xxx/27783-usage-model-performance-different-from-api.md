# vllm-project/vllm#27783: [Usage]: Model performance different from api

| 字段 | 值 |
| --- | --- |
| Issue | [#27783](https://github.com/vllm-project/vllm/issues/27783) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Model performance different from api

### Issue 正文摘录

### Your current environment ```text vllm==0.10.0 ``` ### How would you like to use vllm I'm running model Qwen3-8B with vllm. I also run the same experiment using Qwen3-8B api. But I find the result is quite different, the accuracy of api-model on my task is much higher than the vllm-model. I use the same temperature and top_k. Is there anyone else meeting the same question (the api-model is stronger than the vllm-model)? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Model performance different from api usage;stale ### Your current environment ```text vllm==0.10.0 ``` ### How would you like to use vllm I'm running model Qwen3-8B with vllm. I also run the same experiment usi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: riment using Qwen3-8B api. But I find the result is quite different, the accuracy of api-model on my task is much higher than the vllm-model. I use the same temperature and top_k. Is there anyone else meeting the same q...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: riment using Qwen3-8B api. But I find the result is quite different, the accuracy of api-model on my task is much higher than the vllm-model. I use the same temperature and top_k. Is there anyone else meeting the same q...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: l)? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: the vllm-model. I use the same temperature and top_k. Is there anyone else meeting the same question (the api-model is stronger than the vllm-model)? ### Before submitting a new issue... - [x] Make sure you already sear...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
