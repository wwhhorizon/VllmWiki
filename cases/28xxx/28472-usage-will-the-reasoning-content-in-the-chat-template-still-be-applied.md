# vllm-project/vllm#28472: [Usage]: Will the reasoning_content in the chat template still be applied correctly after switching reasoning_content to reasoning

| 字段 | 值 |
| --- | --- |
| Issue | [#28472](https://github.com/vllm-project/vllm/issues/28472) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Will the reasoning_content in the chat template still be applied correctly after switching reasoning_content to reasoning

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Will the message.reasoning_content for (which exists in default chat_template for qwen3-next-thinking qwen3-vl-thinking or other qwen3-thinking series or glm4.5 or kimi-k2-thinking or other models) in the chat template still be applied correctly after changing reasoning_content to reasoning (apply reasoning on ai message to reasoning_content on chat template) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: message.reasoning_content for (which exists in default chat_template for qwen3-next-thinking qwen3-vl-thinking or other qwen3-thinking series or glm4.5 or kimi-k2-thinking or other models) in the chat template still be...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: te) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
