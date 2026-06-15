# vllm-project/vllm#43726: [New Model]: Gemma4ForSequenceClassification

| 字段 | 值 |
| --- | --- |
| Issue | [#43726](https://github.com/vllm-project/vllm/issues/43726) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Gemma4ForSequenceClassification

### Issue 正文摘录

### The model to consider. Gemma4 is not supported for Classification. I would like to add support for a non-vocab-sized output head. ### The closest model vllm already supports. Gemma4ForCausalLM / Gemma4TextModel ### What's your difficulty of supporting the model you want? Its staightforward. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: Gemma4ForSequenceClassification ### The model to consider. Gemma4 is not supported for Classification. I would like to add support for a non-vocab-sized output head. ### The closest model vllm already suppo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rd. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [New Model]: Gemma4ForSequenceClassification ### The model to consider. Gemma4 is not supported for Classification. I would like to add support for a non-vocab-sized output head. ### The closest model vllm already suppo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
