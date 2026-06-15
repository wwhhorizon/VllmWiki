# vllm-project/vllm#29651: [Feature]: Add P/D disaggregation deployment on Ray

| 字段 | 值 |
| --- | --- |
| Issue | [#29651](https://github.com/vllm-project/vllm/issues/29651) |
| 状态 | closed |
| 标签 | feature request;ray;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add P/D disaggregation deployment on Ray

### Issue 正文摘录

# 🚀 The feature, motivation and pitch This issue proposes adding a lightweight P/D disaggregation deployment mode for vLLM on Ray. ## Motivation - Provide a Ray-native deployment option for vLLM that cleanly separates Prefill (P) nodes and Decode (D) nodes. Improve flexibility in scheduling and resource utilization on heterogeneous Ray clusters (e.g., different GPU types, CPU-only nodes). - Keep the solution lightweight and easy to operate, without introducing heavy additional components or complex orchestration. ## High-level idea Introduce a P/D-disaggregated deployment mode built on top of Ray, with specialized P and D nodes for compute-bound vs latency-bound workloads. Design the deployment so that: - It is easy to configure and launch on an existing Ray cluster. - It reuses as much of the existing vLLM infrastructure as possible. - It remains compatible with the new router and the proxy implementation in the vLLM repository. ## Why this is useful - Lightweight deployment: minimal extra services and configuration; suitable for users who want elastic, distributed vLLM on Ray but don’t want to adopt a heavy multi-component stack. - Better resource utilization: P and D roles can...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: Add P/D disaggregation deployment on Ray feature request;ray;stale # 🚀 The feature, motivation and pitch This issue proposes adding a lightweight P/D disaggregation deployment mode for vLLM on Ray. ## Motivat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: n: users who already run vLLM on Ray can adopt this mode with relatively small changes. If this direction aligns with the project’s roadmap, I’d be happy to open a PR implementing this deployment mode and iterate based...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: built on top of Ray, with specialized P and D nodes for compute-bound vs latency-bound workloads. Design the deployment so that: - It is easy to configure and launch on an existing Ray cluster. - It reuses as much of th...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: es). - Keep the solution lightweight and easy to operate, without introducing heavy additional components or complex orchestration. ## High-level idea Introduce a P/D-disaggregated deployment mode built on top of Ray, w...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: latency-bound workloads. Design the deployment so that: - It is easy to configure and launch on an existing Ray cluster. - It reuses as much of the existing vLLM infrastructure as possible. - It remains compatible with...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
