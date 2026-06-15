# vllm-project/vllm#11793: [Usage]: tool calls for Qwen/QwQ-32B-Preview

| 字段 | 值 |
| --- | --- |
| Issue | [#11793](https://github.com/vllm-project/vllm/issues/11793) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: tool calls for Qwen/QwQ-32B-Preview

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Hi, from the chat template of Qwen/QwQ-32B-Preview: https://huggingface.co/Qwen/QwQ-32B-Preview/blob/1032e81cb936c486aae1d33da75b2fbcd5deed4a/tokenizer_config.json#L197, it seems that it supports `tool_calls`, but I tested it and found that `tool_calls` returned is empty. Is this a problem of vllm or just the model's capability? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: tool calls for Qwen/QwQ-32B-Preview usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Hi, from the chat template of Qwen/QwQ-32B-Preview: ht...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: _calls` returned is empty. Is this a problem of vllm or just the model's capability? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bot...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: okenizer_config.json#L197, it seems that it supports `tool_calls`, but I tested it and found that `tool_calls` returned is empty. Is this a problem of vllm or just the model's capability? ### Before submitting a new iss...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
