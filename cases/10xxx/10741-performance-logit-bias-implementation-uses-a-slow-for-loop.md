# vllm-project/vllm#10741: [Performance]: logit bias implementation uses a slow for loop

| 字段 | 值 |
| --- | --- |
| Issue | [#10741](https://github.com/vllm-project/vllm/issues/10741) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: logit bias implementation uses a slow for loop

### Issue 正文摘录

### Proposal to improve performance We were running logit bias with a big dictionary and noticed a significant slowdown in generation. We looked into the implementation and saw that it uses a for loop https://github.com/vllm-project/vllm/blob/a79b1224005836bdf0ab6d3bab807d2f5d8a5ef1/vllm/entrypoints/openai/logits_processors.py#L48 Any specific reason this is done this way? From quick tests it seems that a `scatter_add` would be significantly faster. If this has not been considered before, I'll spend some time to make a proper benchmark and a PR. On my Mac, with a -100 bias on 40k tokens out of 150k ``` In [48]: %timeit f_for(x, logit_bias) 106 ms ± 2.92 ms per loop (mean ± std. dev. of 7 runs, 10 loops each) In [49]: %timeit f_scatter(x, logit_bias) 3.74 ms ± 13.2 µs per loop (mean ± std. dev. of 7 runs, 100 loops each) ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: processors.py#L48 Any specific reason this is done this way? From quick tests it seems that a `scatter_add` would be significantly faster. If this has not been considered before, I'll spend some time to make a proper be...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: b807d2f5d8a5ef1/vllm/entrypoints/openai/logits_processors.py#L48 Any specific reason this is done this way? From quick tests it seems that a `scatter_add` would be significantly faster. If this has not been considered b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Performance]: logit bias implementation uses a slow for loop performance;stale ### Proposal to improve performance We were running logit bias with a big dictionary and noticed a significant slowdown in generation. We lo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
