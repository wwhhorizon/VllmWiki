# vllm-project/vllm#26858: [RFC]: Top-level CLI interface for KV cache offloading

| 字段 | 值 |
| --- | --- |
| Issue | [#26858](https://github.com/vllm-project/vllm/issues/26858) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Top-level CLI interface for KV cache offloading

### Issue 正文摘录

### Motivation. CPU (and tier-2 storage) offloading is an important feature in many cases (multi-round QA, document analysis, agent workflow, and reinforcement learning). With the recent advancement in the offloading connector, we already have the vLLM native CPU offloading implemented via the connector API. Also, there are multiple community efforts to provide other offloading implementations (e.g., LMCache, Nixl storage, mooncake) via the same set of APIs. However, there is no clear documentation about how to configure the CPU offloading from the user's perspective. Right now, in order to enable CPU offloading, the user needs to pass a JSON string to `--kv-transfer-config`, which may create a huge mental barrier for new users. Therefore, it would be better to have a simple & clear user interface for users to enable CPU offloading. ### Proposed Change. This proposal contains two new command-line arguments: - `--kv-offloading-size`: a numeric value to control a global offloading buffer size (in GB). When TP > 1, this number should be the total size summed across all the TP ranks. (An alternative is the buffer size for each TP rank.) - `--kv-offloading-backend`: a string that speci...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ffloading RFC ### Motivation. CPU (and tier-2 storage) offloading is an important feature in many cases (multi-round QA, document analysis, agent workflow, and reinforcement learning). With the recent advancement in the...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [RFC]: Top-level CLI interface for KV cache offloading RFC ### Motivation. CPU (and tier-2 storage) offloading is an important feature in many cases (multi-round QA, document analysis, agent workflow, and reinforcement...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: (An alternative is the buffer size for each TP rank.) - `--kv-offloading-backend`: a string that specifies which offloading backend to use, such as "native", "lmcache", "mooncake", "3fs", or "nixl". This will give enoug...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: sal contains two new command-line arguments: - `--kv-offloading-size`: a numeric value to control a global offloading buffer size (in GB). When TP > 1, this number should be the total size summed across all the TP ranks...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
