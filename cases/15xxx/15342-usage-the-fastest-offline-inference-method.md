# vllm-project/vllm#15342: [usage]: The fastest offline inference method

| 字段 | 值 |
| --- | --- |
| Issue | [#15342](https://github.com/vllm-project/vllm/issues/15342) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [usage]: The fastest offline inference method

### Issue 正文摘录

### Motivation. I have an unlimited number of H100/A100. What is the fastest way to get Deepseek V3 generations on a dataset with a large number of examples? Is this an offline LLM or an OpenAI server? What parameters can be set for maximum speed? ### Proposed Change. The inference code, the parameters in the instance settings, a few comments with explanations ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ne inference method usage ### Motivation. I have an unlimited number of H100/A100. What is the fastest way to get Deepseek V3 generations on a dataset with a large number of examples? Is this an offline LLM or an OpenAI...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [usage]: The fastest offline inference method usage ### Motivation. I have an unlimited number of H100/A100. What is the fastest way to get Deepseek V3 generations on a dataset with a large number of examples? Is this a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
