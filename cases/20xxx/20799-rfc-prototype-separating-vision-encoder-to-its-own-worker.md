# vllm-project/vllm#20799: [RFC]: Prototype Separating Vision Encoder to Its Own Worker

| 字段 | 值 |
| --- | --- |
| Issue | [#20799](https://github.com/vllm-project/vllm/issues/20799) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Prototype Separating Vision Encoder to Its Own Worker

### Issue 正文摘录

### Motivation. In the current multi-modality support within vLLM, the vision encoder (e.g., Qwen_vl) and the language model decoder run within the same worker process. While this tightly coupled architecture is simple to implement, it introduces several challenges in terms of scalability, resource utilization, and flexibility: 1. **Resource Contention:** The vision encoder is often a compute and memory-intensive task. When processing high-resolution images or performing complex preprocessing, it competes for valuable GPU resources with the language model's prefill and decode stages, potentially increasing the overall latency of request processing. 2. **Scalability Issues:** The workload characteristics of vision processing and text generation are different. In some scenarios, image processing might be the bottleneck (e.g., a high volume of concurrent image inputs), while in others, text generation is the bottleneck (e.g., long text outputs). A unified worker model cannot scale these two different workloads independently. 3. **Inflexible Architecture:** The coupled architecture makes advanced optimizations difficult. For example, we cannot assign different types of hardware resour...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [RFC]: Prototype Separating Vision Encoder to Its Own Worker RFC;stale ### Motivation. In the current multi-modality support within vLLM, the vision encoder (e.g., Qwen_vl) and the language model decoder run within the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: he current multi-modality support within vLLM, the vision encoder (e.g., Qwen_vl) and the language model decoder run within the same worker process. While this tightly coupled architecture is simple to implement, it int...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ge model's prefill and decode stages, potentially increasing the overall latency of request processing. 2. **Scalability Issues:** The workload characteristics of vision processing and text generation are different. In...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ct stages by specialized worker pools. --- **1. Request Ingestion and Dispatch to Vision Stage** 1.1. **Request Entry:** A multi-modal request, containing both image and text data, is sent via the `API Server` to the sy...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: l decoder run within the same worker process. While this tightly coupled architecture is simple to implement, it introduces several challenges in terms of scalability, resource utilization, and flexibility: 1. **Resourc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
