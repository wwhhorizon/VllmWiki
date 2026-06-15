# vllm-project/vllm#18633: [RFC]: [Spec Decode] Combine Ngram and EAGLE

| 字段 | 值 |
| --- | --- |
| Issue | [#18633](https://github.com/vllm-project/vllm/issues/18633) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: [Spec Decode] Combine Ngram and EAGLE

### Issue 正文摘录

### Motivation. EAGLE and Ngram give speedup in different scenarios. * Ngram is beneficial when the prompt has ngrams which can be useful for creating drafts, e.g., editing task * EAGLE is a drafting strategy which can propose draft tokens in any general situation Right now, we can either start vllm serve either with ngram OR with EAGLE. We need to decide beforehand which draft strategy we are going to use. This means we have to deploy different model instances in production if we want to support editing request and general requests. This leads to less than optimal GPU resource utilization since traffic for editing and non-editing task will not be static ### Proposed Change. If we combine ngram and EAGLE then we don't need separate instances of ngram and EAGLE deployments and the instance can pick which strategy to use at any given timestep for a given request. Ngram is a model-free drafter whereas EAGLE needs a draft model so the overhead of running them will not be too much over EAGLE's overhead. It could improve overall AL compared to just using EAGLE. #### Draft merge strategy For any given timestep and for a given seq in a batch: * find if there any ngram match * If yes, then...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [RFC]: [Spec Decode] Combine Ngram and EAGLE RFC;stale ### Motivation. EAGLE and Ngram give speedup in different scenarios. * Ngram is beneficial when the prompt has ngrams which can be useful for creating drafts, e.g.,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: EAGLE and Ngram give speedup in different scenarios. * Ngram is beneficial when the prompt has ngrams which can be useful for creating drafts, e.g., editing task * EAGLE is a drafting strategy which can propose draft to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: llm-project/vllm/issues/17812), [src2](https://developer.nvidia.com/blog/blackwell-breaks-the-1000-tps-user-barrier-with-metas-llama-4-maverick/)), i.e., EAGLE proposes max 3 tokens at a time. Ngram usually is with 5 bu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: aft strategy we are going to use. This means we have to deploy different model instances in production if we want to support editing request and general requests. This leads to less than optimal GPU resource utilization...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
