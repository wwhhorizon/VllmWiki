# vllm-project/vllm#14621: [Usage]:  how to use embeddings as input rather than token_ids

| 字段 | 值 |
| --- | --- |
| Issue | [#14621](https://github.com/vllm-project/vllm/issues/14621) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:  how to use embeddings as input rather than token_ids

### Issue 正文摘录

### Your current environment I want to use embeddings instead of token_ids as input, how can i do it? ### How would you like to use vllm I want to run inference of a DeepSeek-R1-Distill-Qwen-1.5B(deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: d you like to use vllm I want to run inference of a DeepSeek-R1-Distill-Qwen-1.5B(deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
