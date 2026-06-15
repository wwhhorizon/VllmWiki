# vllm-project/vllm#11079: [Feature]: N-gram speculation on tokens other than prompt

| 字段 | 值 |
| --- | --- |
| Issue | [#11079](https://github.com/vllm-project/vllm/issues/11079) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: N-gram speculation on tokens other than prompt

### Issue 正文摘录

### 🚀 The feature, motivation and pitch N-gram speculation is a compelling optimization due to its plug and play nature. However, only being able to speculate on n-grams in the prompt limits the utility of this feature. The ability to provide any arbitrary sequence of tokens to draw n-grams from for speculation (rather than only being able to speculate on n-grams from the prompt) would be a simple but meaningful improvement, granting the user much more flexibility when using ngram speculation. ### Alternatives In theory you can include whatever tokens you want in the prompt, but it goes without saying that this is suboptimal. This may require growing the prompt size substantially, the model then also needs to compute attention on these tokens and this can affect the output distribution (which defeats the entire purpose of speculation, namely to produce the same outputs with lower latency). ### Additional context The interface for this feature could be as simple as this: (based on [this snippet](https://docs.vllm.ai/en/v0.5.5/models/spec_decode.html#speculating-by-matching-n-grams-in-the-prompt) from the documentation) ```python from vllm import LLM, SamplingParams model_inputs = {...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: N-gram speculation on tokens other than prompt feature request;stale ### 🚀 The feature, motivation and pitch N-gram speculation is a compelling optimization due to its plug and play nature. However, only bein...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: re purpose of speculation, namely to produce the same outputs with lower latency). ### Additional context The interface for this feature could be as simple as this: (based on [this snippet](https://docs.vllm.ai/en/v0.5....
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: (which defeats the entire purpose of speculation, namely to produce the same outputs with lower latency). ### Additional context The interface for this feature could be as simple as this: (based on [this snippet](https:...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: hing-n-grams-in-the-prompt) from the documentation) ```python from vllm import LLM, SamplingParams model_inputs = {} model_inputs["prompt"] = ... # Some tensor # Some other tensor, if provided speculation uses ngrams fr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
