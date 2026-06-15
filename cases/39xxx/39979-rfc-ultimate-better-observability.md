# vllm-project/vllm#39979: [RFC]: Ultimate Better Observability.

| 字段 | 值 |
| --- | --- |
| Issue | [#39979](https://github.com/vllm-project/vllm/issues/39979) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Ultimate Better Observability.

### Issue 正文摘录

### Motivation. I am desperate need of a new coarse-grained tracker (compared to PyTorch Profiler) that provides per-request and per-iteration (i.e., engine step) metrics for end-to-end performance optimization. Currently, while the PyTorch Profiler is very useful for profiling vLLM, but it can only monitor a small number of requests and is not suitable for monitoring online systems. Furthermore, it introduces significant overhead because it operates at the granularity of individual PyTorch ops. For online system monitoring, only a much coarser granularity is required. Let's build the Ultimate Better Observability (cite: [Feature]: Even Better Observability https://github.com/vllm-project/vllm/issues/3616). Related RPCs and issues and PRs: - #38760 - #36189 - #40781 - #39438 - #32573 - #32162 - #3616 ### Proposed Change. **Use a OpenTelemetry-based tracing, since we’ve already integrated OpenTelemetry.** #### Currently we only tracing the inference_time, We need more details. https://docs.vllm.ai/en/latest/design/metrics/#tracing-opentelemetry > Metrics provide an aggregated view over time of the system's performance and health. Tracing, on the other hand, tracks individual reques...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: coarse-grained tracker (compared to PyTorch Profiler) that provides per-request and per-iteration (i.e., engine step) metrics for end-to-end performance optimization. Currently, while the PyTorch Profiler is very useful...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: I am desperate need of a new coarse-grained tracker (compared to PyTorch Profiler) that provides per-request and per-iteration (i.e., engine step) metrics for end-to-end performance optimization. Currently, while the Py...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: e system monitoring, only a much coarser granularity is required. Let's build the Ultimate Better Observability (cite: [Feature]: Even Better Observability https://github.com/vllm-project/vllm/issues/3616). Related RPCs...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ch Profiler is very useful for profiling vLLM, but it can only monitor a small number of requests and is not suitable for monitoring online systems. Furthermore, it introduces significant overhead because it operates at...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: s divide the pipeline into three(four) stages: - maybe add download for multimodal models - preprocessing - engine_call - postprocessing. This will become the coarsest-grained tracking level. The tracker in entrypoints...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
