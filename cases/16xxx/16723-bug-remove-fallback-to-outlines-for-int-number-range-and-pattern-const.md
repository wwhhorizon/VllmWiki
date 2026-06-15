# vllm-project/vllm#16723: [Bug]: Remove fallback to outlines for int/number range and pattern constraints in guided_json

| 字段 | 值 |
| --- | --- |
| Issue | [#16723](https://github.com/vllm-project/vllm/issues/16723) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Remove fallback to outlines for int/number range and pattern constraints in guided_json

### Issue 正文摘录

### Your current environment - vllm 0.8.3 - xgrammar ### 🐛 Describe the bug Hi team, I’d like to propose removing the current fallback mechanism to outlines for int/number range constraints and pattern-based validations in Guided JSON mode. https://github.com/vllm-project/vllm/blob/ee378f3d49f1404a72ec0948f0a2553f7c3a3726/vllm/model_executor/guided_decoding/utils.py#L6-L23 Previously, vLLM defaulted to Outlines when encountering complex JSON schema elements (like pattern, minimum, or maximum) due to limitations in xgrammar. https://github.com/vllm-project/vllm/pull/10899 However, xgrammar has now added full support for these schema constraints, which makes this fallback no longer necessary. - https://github.com/mlc-ai/xgrammar/pull/185 - https://github.com/mlc-ai/xgrammar/pull/289 - https://github.com/mlc-ai/xgrammar/blob/8fa47978e37970865a6630a9533f2e1db7dc8f46/cpp/json_schema_converter.cc#L1645-L1655 The main motivation behind this PR is not only to simplify and unify the backend behavior, but also to address a serious performance concern. When fallback to Outlines occurs in production, we've experienced: - **Significantly higher memory usage**, leading to OOM errors, and - **Mu...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Remove fallback to outlines for int/number range and pattern constraints in guided_json bug ### Your current environment - vllm 0.8.3 - xgrammar ### 🐛 Describe the bug Hi team, I’d like to propose removing the cu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: bug Hi team, I’d like to propose removing the current fallback mechanism to outlines for int/number range constraints and pattern-based validations in Guided JSON mode. https://github.com/vllm-project/vllm/blob/ee378f3d...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: it's now equally reasonable and timely to eliminate fallbacks related to numeric ranges and regex patterns as well. This change would allow Guided JSON to be more reliable and performant under real-world workloads, espe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: JSON to be more reliable and performant under real-world workloads, especially when schemas include numeric ranges or regex patterns. Looking forward to your feedback! ### Before submitting a new issue... - [x] Make sur...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: we've experienced: - **Significantly higher memory usage**, leading to OOM errors, and - **Much slower response times**, which in some cases rendered Guided JSON unusable for real-time services. Additionally, this propo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
