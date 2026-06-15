# vllm-project/vllm#22992: [RFC]: Refactor CI/CD

| 字段 | 值 |
| --- | --- |
| Issue | [#22992](https://github.com/vllm-project/vllm/issues/22992) |
| 状态 | closed |
| 标签 | help wanted;good first issue;RFC |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Refactor CI/CD

### Issue 正文摘录

### Motivation. vLLM's CI/CD has grown in a less than ideal way as it has built up over the years. We have the following problems: - CI takes very long, especially on a per commit cycle - CI has failures that cannot be reproduced on every machine due to numerics - CI has failures on models that are not the 80-20 of our usage --- which runs per commit - CI failures in early tests often lead to vLLM not cleaning up properly --- which creates failures across many tests that makes it hard to identify what is wrong - CI is NOT covering the models that actually matter (since not enough GPU memory) or hardware that actually matters to the majority of our users - CI is NOT covering performance! These issues are creating a bad developer experience for vLLM and causes issues like the CI "death spiral", where we get into a cycle of force-merges. These issues are creating challenges for vLLM's multiple HW backends, as we are unable to get reliable signal that keeps blocking issues. ### Proposed Change. The CI needs to be completely refactored and the culture around vLLM CI needs to be significantly improved. Overall Goals: - Remove V0 tests and migrate any missing coverage into V1 - Reduce pe...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: long, especially on a per commit cycle - CI has failures that cannot be reproduced on every machine due to numerics - CI has failures on models that are not the 80-20 of our usage --- which runs per commit - CI failures...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rce-merges. These issues are creating challenges for vLLM's multiple HW backends, as we are unable to get reliable signal that keeps blocking issues. ### Proposed Change. The CI needs to be completely refactored and the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [RFC]: Refactor CI/CD help wanted;good first issue;RFC ### Motivation. vLLM's CI/CD has grown in a less than ideal way as it has built up over the years. We have the following problems: - CI takes very long, especially...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: g - CI is NOT covering the models that actually matter (since not enough GPU memory) or hardware that actually matters to the majority of our users - CI is NOT covering performance! These issues are creating a bad devel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
