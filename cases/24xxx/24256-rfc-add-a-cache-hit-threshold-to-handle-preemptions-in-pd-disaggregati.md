# vllm-project/vllm#24256: [RFC]: Add a cache hit threshold to handle Preemptions in PD-Disaggregation and enable lightweight powerful P/D implementations

| 字段 | 值 |
| --- | --- |
| Issue | [#24256](https://github.com/vllm-project/vllm/issues/24256) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Add a cache hit threshold to handle Preemptions in PD-Disaggregation and enable lightweight powerful P/D implementations

### Issue 正文摘录

### Motivation. This RFC introduces cache hit–based admission control for requests, motivated by PD-Disaggregation and preemption handling scenarios. Related llm-d ticket and documentation: [here](https://github.com/llm-d/llm-d-inference-scheduler/issues/382). *Edit: updated Sep 12, 2025 - added Preemption handling use-case* ### 🧩 Summary This RFC proposes adding an optional field to incoming requests and an optional global configuration to vLLM, which set a minimum KV-Cache hit rate for handling requests. Requests which are found to have a lower cache hit percentage than the given threshold, will be rejected with a specific new finish reason. The cache hit rate includes cache from external and previously offloaded KV-Cache, obtained via the KVConnector, and not just the local APC. This feature is useful in several use-cases in PD-Disaggregated deployments: 1. Request Preemption: In P/D systems a Preempted request on a Decode instance ("Decoder") will perform recalculation (prefill) on the Decoder itself, in case cache was not offloaded, which can degrade Decoder performance and cascade into instance lockups. This feature allows an external inference management system such as llm-...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: D-Disaggregation and enable lightweight powerful P/D implementations RFC;stale ### Motivation. This RFC introduces cache hit–based admission control for requests, motivated by PD-Disaggregation and preemption handling s...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: quests and an optional global configuration to vLLM, which set a minimum KV-Cache hit rate for handling requests. Requests which are found to have a lower cache hit percentage than the given threshold, will be rejected...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ache hit percentage than the given threshold, will be rejected with a specific new finish reason. The cache hit rate includes cache from external and previously offloaded KV-Cache, obtained via the KVConnector, and not...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ses adding an optional field to incoming requests and an optional global configuration to vLLM, which set a minimum KV-Cache hit rate for handling requests. Requests which are found to have a lower cache hit percentage...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [RFC]: Add a cache hit threshold to handle Preemptions in PD-Disaggregation and enable lightweight powerful P/D implementations RFC;stale ### Motivation. This RFC introduces cache hit–based admission control for request...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
