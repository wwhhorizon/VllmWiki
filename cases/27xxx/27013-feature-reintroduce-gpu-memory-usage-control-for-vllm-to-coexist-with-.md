# vllm-project/vllm#27013: [Feature]: Reintroduce GPU memory usage control for vLLM to coexist with other GPU-light tasks

| 字段 | 值 |
| --- | --- |
| Issue | [#27013](https://github.com/vllm-project/vllm/issues/27013) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Reintroduce GPU memory usage control for vLLM to coexist with other GPU-light tasks

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In previous versions, the gpu-memory-utilization parameter allowed limiting the fraction of GPU memory that vLLM would use. This feature was very useful in multi-model setups, for example when running a large LLM alongside other GPU-light applications or services on the same GPU. It would be great if this feature could be reintroduced, or if an alternative parameter could allow controlling GPU memory usage per model, so that vLLM can coexist with other GPU-light tasks without exhausting GPU resources. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ory usage control for vLLM to coexist with other GPU-light tasks feature request;stale ### 🚀 The feature, motivation and pitch In previous versions, the gpu-memory-utilization parameter allowed limiting the fraction of...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ature request;stale ### 🚀 The feature, motivation and pitch In previous versions, the gpu-memory-utilization parameter allowed limiting the fraction of GPU memory that vLLM would use. This feature was very useful in mul...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Feature]: Reintroduce GPU memory usage control for vLLM to coexist with other GPU-light tasks feature request;stale ### 🚀 The feature, motivation and pitch In previous versions, the gpu-memory-utilization parameter all...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: of GPU memory that vLLM would use. This feature was very useful in multi-model setups, for example when running a large LLM alongside other GPU-light applications or services on the same GPU. It would be great if this f...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
