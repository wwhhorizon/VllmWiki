# vllm-project/vllm#23607: [Usage]: How to reason about a modified large language model

| 字段 | 值 |
| --- | --- |
| Issue | [#23607](https://github.com/vllm-project/vllm/issues/23607) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to reason about a modified large language model

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm ```text If I modify the output layer (LMHead) of a large language model (e.g., Qwen3-32B) to perform binary classification, can I still use vLLM for inference? Additionally, if I want to continue using the /v1/chat/completions API with this modified model, does vLLM support such a configuration? ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: How to reason about a modified large language model usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm ```text If I modify the output layer (...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
