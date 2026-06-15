# vllm-project/vllm#34333: [RFC]: Automated baselining and degradation detection

| 字段 | 值 |
| --- | --- |
| Issue | [#34333](https://github.com/vllm-project/vllm/issues/34333) |
| 状态 | open |
| 标签 | RFC;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Automated baselining and degradation detection

### Issue 正文摘录

### Motivation. TL;DR We published a method to detect accuracy degradations with statistical guarantees. This RFC serves as a platform to discuss whether and how this method could help in vLLMs model onboarding and CI processes ## Context When onboarding a new model to vLLM or optimizing the performance, an end-to-end accuracy check is very useful to catch any potential performance degradations against a baseline. Such a baseline could be either the implementation in `transformers` (in case of onboarding) or a previous stable version of vLLM itself (in case of perf optimizations). ## Problem The difficulty is that even if everything works fine, we cannot expect accuracies to match exactly. But using fixed accuracy differences as a rule to flag degradations fails to reliably detect those. Furthermore, when we evaluate on multiple tasks the question arises how to make a single joint decision. ## Potential Science Solution We recently published a paper to compute reliable p-values for exactly that situation, see 📜 [When LLMs get significantly worse: A statistical approach to detect model degradations](https://openreview.net/forum?id=cM3gsqEI4K) Adding such a method into model onboard...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: tection RFC;stale ### Motivation. TL;DR We published a method to detect accuracy degradations with statistical guarantees. This RFC serves as a platform to discuss whether and how this method could help in vLLMs model o...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: tection RFC;stale ### Motivation. TL;DR We published a method to detect accuracy degradations with statistical guarantees. This RFC serves as a platform to discuss whether and how this method could help in vLLMs model o...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: uss whether and how this method could help in vLLMs model onboarding and CI processes ## Context When onboarding a new model to vLLM or optimizing the performance, an end-to-end accuracy check is very useful to catch an...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: automate the detection of accuracy degradations. If the p-values is very small, we can confidently flag an accuracy degradation and do further investigations before launching a feature / model. We also have a Repo with...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: eoretically lossless methods and others without accuracy guarantees like quantization. In all of these cases it is crucial to ensure that the model quality has not degraded. However, even at temperature zero, model gene...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
