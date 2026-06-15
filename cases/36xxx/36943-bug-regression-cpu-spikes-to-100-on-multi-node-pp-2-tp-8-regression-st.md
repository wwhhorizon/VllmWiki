# vllm-project/vllm#36943: [Bug/Regression]: CPU spikes to 100% on Multi-node (PP=2, TP=8) | Regression starting from v0.12.0

| 字段 | 值 |
| --- | --- |
| Issue | [#36943](https://github.com/vllm-project/vllm/issues/36943) |
| 状态 | open |
| 标签 | performance |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug/Regression]: CPU spikes to 100% on Multi-node (PP=2, TP=8) \| Regression starting from v0.12.0

### Issue 正文摘录

### Proposal to improve performance We are observing a severe regression in CPU management when running vLLM in a multi-node setup on OpenShift. While the deployment is perfectly stable on v0.11.0, any version from v0.12.0 up to v0.17.0 triggers complete CPU saturation. Even under light inference load, the CPU utilization on both nodes spikes to 100%, leading to a rapid decline in throughput and eventual node unresponsiveness. This behavior is consistent across various models using a TP=8, PP=2 topology on 2xH100 nodes via LeaderWorkerSet (LWS). The fact that the exact same configuration and infrastructure work seamlessly on v0.11.0 strongly suggests a regression introduced in v0.12.0, possibly related to how the distributed backend or the scheduler interacts with OpenShift's resource constraints. Questions: Were there specific changes in the Ray/Distributed backend or scheduling logic in v0.12.0 that could cause this busy-wait loop or thread contention? Are there recommended environment variables or flags to tune Ray/vLLM resource management in hardened environments like OpenShift? ### Report of performance regression _No response_ ### Misc discussion on performance Infrastructur...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug/Regression]: CPU spikes to 100% on Multi-node (PP=2, TP=8) | Regression starting from v0.12.0 performance ### Proposal to improve performance We are observing a severe regression in CPU management when running vLLM...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: p on OpenShift. While the deployment is perfectly stable on v0.11.0, any version from v0.12.0 up to v0.17.0 triggers complete CPU saturation. Even under light inference load, the CPU utilization on both nodes spikes to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ior is consistent across various models using a TP=8, PP=2 topology on 2xH100 nodes via LeaderWorkerSet (LWS). The fact that the exact same configuration and infrastructure work seamlessly on v0.11.0 strongly suggests a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: entual node unresponsiveness. This behavior is consistent across various models using a TP=8, PP=2 topology on 2xH100 nodes via LeaderWorkerSet (LWS). The fact that the exact same configuration and infrastructure work s...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: egression introduced in v0.12.0, possibly related to how the distributed backend or the scheduler interacts with OpenShift's resource constraints. Questions: Were there specific changes in the Ray/Distributed backend or...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
