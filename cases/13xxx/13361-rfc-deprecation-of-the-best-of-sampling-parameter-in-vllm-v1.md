# vllm-project/vllm#13361: [RFC]: Deprecation of the `best_of` Sampling Parameter in vLLM V1

| 字段 | 值 |
| --- | --- |
| Issue | [#13361](https://github.com/vllm-project/vllm/issues/13361) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Deprecation of the `best_of` Sampling Parameter in vLLM V1

### Issue 正文摘录

### Motivation. ### Overview As we transition to vLLM V1, we plan to discontinue support for the `best_of` sampling parameter. This decision is driven by a combination of low usage, alignment with industry trends, and a desire for system simplicity and performance. ### Background: What is `best_of`? The `best_of` parameter was originally part of the earlier OpenAI completion API. It enabled the generation of multiple completions—`n` different outputs—then selected the “best” completion based on the cumulative log probabilities of each result. ### Reasons for Deprecation 1. **Limited Usage and Industry Trends:** - **Low Adoption:** To the best of our knowledge, the `best_of` feature is used by very few users. Users have observed that output quality isn’t reliably correlated with their log probabilities in most cases. - **Evolving Standards:** Major AI providers such as OpenAI (in its current API), Claude, and Gemini have moved away from including the `best_of` option. 2. **Alternative Methods:** - Users can implement `best_of` by leveraging the `n` parameter to obtain multiple completions and the `logprobs` parameter for the log probability of each generated token. This method effe...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: AI completion API. It enabled the generation of multiple completions—`n` different outputs—then selected the “best” completion based on the cumulative log probabilities of each result. ### Reasons for Deprecation 1. **L...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: plan to discontinue support for the `best_of` sampling parameter. This decision is driven by a combination of low usage, alignment with industry trends, and a desire for system simplicity and performance. ### Background...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
