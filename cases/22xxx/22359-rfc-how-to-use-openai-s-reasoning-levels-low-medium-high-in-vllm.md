# vllm-project/vllm#22359: [RFC]: How to use OpenAI's "Reasoning Levels" (low/medium/high) in vLLM?

| 字段 | 值 |
| --- | --- |
| Issue | [#22359](https://github.com/vllm-project/vllm/issues/22359) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: How to use OpenAI's "Reasoning Levels" (low/medium/high) in vLLM?

### Issue 正文摘录

### Motivation. Hi, According to OpenAI's documentation, there is a feature called Reasoning Levels that allows controlling the depth of reasoning in a model response. The levels are: ``` Reasoning levels You can adjust the reasoning level that suits your task across three levels: Low: Fast responses for general dialogue. Medium: Balanced speed and detail. High: Deep and detailed analysis. The reasoning level can be set in the system prompts, e.g., "Reasoning: high". ``` I would like to know: 1. How can I use this in vLLM? Should I just include "Reasoning: high" in the system prompt, or is there another preferred way to activate it? 2. What is the default reasoning level if I don’t explicitly set it? ### Proposed Change. None ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: y to activate it? 2. What is the default reasoning level if I don’t explicitly set it? ### Proposed Change. None ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Befo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: led Reasoning Levels that allows controlling the depth of reasoning in a model response. The levels are: ``` Reasoning levels You can adjust the reasoning level that suits your task across three levels: Low: Fast respon...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
