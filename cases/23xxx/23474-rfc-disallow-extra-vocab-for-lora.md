# vllm-project/vllm#23474: [RFC]: Disallow extra vocab for LoRA

| 字段 | 值 |
| --- | --- |
| Issue | [#23474](https://github.com/vllm-project/vllm/issues/23474) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Disallow extra vocab for LoRA

### Issue 正文摘录

### Motivation. Currently, vLLM allows each LoRA adapter to define its own additional vocabulary: https://github.com/vllm-project/vllm/blob/65197a5fb37ef4d8b93e0b99ecc8b902fe948e97/vllm/config/__init__.py#L2456-L2460 However, this introduces significant complexity because: 1. We can no longer assume a single tokenizer per model (since each LoRA adapter can have its own tokenizer). 2. The size of the unembedding layer becomes ambiguous. ### Proposed Change. Since this feature appears to be rarely used, I propose removing it. Going forward, vLLM will assume that all LoRA adapters for a given model share the same vocabulary. ### Feedback Period. 1 week ### CC List. @jeejeelee ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: com/vllm-project/vllm/blob/65197a5fb37ef4d8b93e0b99ecc8b902fe948e97/vllm/config/__init__.py#L2456-L2460 However, this introduces significant complexity because: 1. We can no longer assume a single tokenizer per model (s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
