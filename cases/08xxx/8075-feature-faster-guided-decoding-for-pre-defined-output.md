# vllm-project/vllm#8075: [Feature]: Faster guided decoding for pre-defined output

| 字段 | 值 |
| --- | --- |
| Issue | [#8075](https://github.com/vllm-project/vllm/issues/8075) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Faster guided decoding for pre-defined output

### Issue 正文摘录

### 🚀 The feature, motivation and pitch vLLM provides a guided generation via outlines, e.g. ```Python from outlines import models, generate model = models.VLLM(llm) generator = generate.choice(model, array_of_categories) ``` This however does not fully utilise deterministic nature of output. Since categories are pre-defined, I wander if decoding can run in parallel for all tokens to increase throughput of decoding. I would be interested in trying to make contributions if folks can provide guidance on steps and where to look in vLLM codebase. ### Alternatives Speculative generation is somewhat similar, for example when ngrams are used in place of approximation model. ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Faster guided decoding for pre-defined output feature request;stale ### 🚀 The feature, motivation and pitch vLLM provides a guided generation via outlines, e.g. ```Python from outlines import models, generate...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ice(model, array_of_categories) ``` This however does not fully utilise deterministic nature of output. Since categories are pre-defined, I wander if decoding can run in parallel for all tokens to increase throughput of...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ice(model, array_of_categories) ``` This however does not fully utilise deterministic nature of output. Since categories are pre-defined, I wander if decoding can run in parallel for all tokens to increase throughput of...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: provides a guided generation via outlines, e.g. ```Python from outlines import models, generate model = models.VLLM(llm) generator = generate.choice(model, array_of_categories) ``` This however does not fully utilise de...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
