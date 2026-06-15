# vllm-project/vllm#8301: [Bug]: Mistral Large Instruct 2407 tool calling leakage

| 字段 | 值 |
| --- | --- |
| Issue | [#8301](https://github.com/vllm-project/vllm/issues/8301) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Mistral Large Instruct 2407 tool calling leakage

### Issue 正文摘录

### Your current environment When using vllm 0.6.0, the mistral tool call parser does not work as expected for Mistral Large 2407 https://huggingface.co/mistralai/Mistral-Large-Instruct-2407 @K-Mistele ### 🐛 Describe the bug It used to work fine when using Autotokenizer to instantiate the tokenizer, but not with MistralTokenizer from mistral_commons. Basically, when you run the model and give it tools, the model thinks it is the tool. Aka, if I give Mistral Large 2407 a tool for looking up movie information on IMDB, the model responds to "Who are you" with "I am a movie database lookup bot" instead of "I am an AI trained by Mistral AI" ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ool call parser does not work as expected for Mistral Large 2407 https://huggingface.co/mistralai/Mistral-Large-Instruct-2407 @K-Mistele ### 🐛 Describe the bug It used to work fine when using Autotokenizer to instantiat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: AI" ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
