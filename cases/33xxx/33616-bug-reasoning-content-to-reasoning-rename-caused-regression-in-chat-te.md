# vllm-project/vllm#33616: [Bug]: reasoning_content to reasoning rename caused regression in chat templates expecting reasoning_content

| 字段 | 值 |
| --- | --- |
| Issue | [#33616](https://github.com/vllm-project/vllm/issues/33616) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: reasoning_content to reasoning rename caused regression in chat templates expecting reasoning_content

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug A regression was introduced by https://github.com/vllm-project/vllm/pull/33402 The change to removing reasoning_content was intended to be for the chat completion endpoint, but that downstream effect of also breaking chat templates that expect reasoning_content (like glm and Kimi K2). It's unlikely many models will be updated to fix this change and will silently degrade in performance. And other inference engines are still providing/using "reasoning_content". So I think this is at a reasonable fix that ensures backwards compatibility with older models. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: reasoning_content to reasoning rename caused regression in chat templates expecting reasoning_content bug ### Your current environment ### 🐛 Describe the bug A regression was introduced by https://github.com/vllm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ls. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: hat expect reasoning_content (like glm and Kimi K2). It's unlikely many models will be updated to fix this change and will silently degrade in performance. And other inference engines are still providing/using "reasonin...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
