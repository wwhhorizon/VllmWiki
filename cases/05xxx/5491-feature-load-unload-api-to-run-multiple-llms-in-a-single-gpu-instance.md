# vllm-project/vllm#5491: [Feature]: load/unload API to run multiple LLMs in a single GPU instance

| 字段 | 值 |
| --- | --- |
| Issue | [#5491](https://github.com/vllm-project/vllm/issues/5491) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: load/unload API to run multiple LLMs in a single GPU instance

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The feature request is to add support for a load/unload endpoint/API in vLLM to dynamically load and unload multiple LLMs within a single GPU instance. This feature aims to enhance resource utilization and scalability by allowing concurrent operation of multiple LLMs on the same GPU. The load/unload endpoint in vLLM facilitates: - Increased Resource Utilization: Enables concurrent operation of multiple LLMs on a single GPU, optimizing computational resources and system efficiency. - Enhanced Scalability: Allows dynamic model loading and unloading based on demand, adapting to varying workloads and user requirements. - Improved Cost-effectiveness: Maximizes throughput and performance without additional hardware investments, ideal for organizations with budget constraints. ### Alternatives Alternatively, providing an API for manual model unloading offers finer control over resource management. ### Additional context - models here in my context are mainly small LLM (<= 10B). - Several community members have raised issue to [unload models](https://github.com/vllm-project/vllm/issues/3281) or [release GPU memory](https://github.com/vllm-project/vl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: on of multiple LLMs on the same GPU. The load/unload endpoint in vLLM facilitates: - Increased Resource Utilization: Enables concurrent operation of multiple LLMs on a single GPU, optimizing computational resources and...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: agement. ### Additional context - models here in my context are mainly small LLM (<= 10B). - Several community members have raised issue to [unload models](https://github.com/vllm-project/vllm/issues/3281) or [release G...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ad models](https://github.com/vllm-project/vllm/issues/3281) or [release GPU memory](https://github.com/vllm-project/vllm/issues/1908) in vLLM. While workarounds exist, their efficacy is inconsistent. It is hoped that o...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: resources and system efficiency. - Enhanced Scalability: Allows dynamic model loading and unloading based on demand, adapting to varying workloads and user requirements. - Improved Cost-effectiveness: Maximizes throughp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ]: load/unload API to run multiple LLMs in a single GPU instance feature request ### 🚀 The feature, motivation and pitch The feature request is to add support for a load/unload endpoint/API in vLLM to dynamically load a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
