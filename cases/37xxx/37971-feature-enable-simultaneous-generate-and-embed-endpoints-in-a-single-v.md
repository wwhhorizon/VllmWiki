# vllm-project/vllm#37971: [Feature]: Enable simultaneous generate and embed endpoints in a single vLLM instance

| 字段 | 值 |
| --- | --- |
| Issue | [#37971](https://github.com/vllm-project/vllm/issues/37971) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Enable simultaneous generate and embed endpoints in a single vLLM instance

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Feature Request: Enable simultaneous `generate` and `embed` endpoints in a single vLLM instance As referenced in https://github.com/vllm-project/vllm/issues/11905, it would be highly beneficial to support running a single vLLM instance that exposes both `generate` and `embed` endpoints concurrently. Although this issue is marked as resolved via https://github.com/vllm-project/vllm/issues/33118, the current solution does not fully meet the expected use case. The workaround relies on using the `generate` endpoint to extract hidden states, which are written to disk (configured via `kv_connector_extra_config` and `shared_storage_path`). In this setup, the `embed` endpoint remains unavailable when the task is set to `generate`. This approach introduces additional complexity and overhead, and does not provide a true embedding API experience. ### Requested improvement Enable native support for the `embed` endpoint alongside the `generate` endpoint within the same vLLM instance. This would allow users to: - Generate text and compute embeddings without maintaining separate deployments - Use both base models and LoRA-adapted models seamlessly for b...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: `generate` endpoint to extract hidden states, which are written to disk (configured via `kv_connector_extra_config` and `shared_storage_path`). In this setup, the `embed` endpoint remains unavailable when the task is se...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ly for both tasks - Avoid disk-based intermediate steps and associated latency/overhead Such functionality would significantly simplify deployment and improve efficiency for applications that require both text generatio...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ps://github.com/vllm-project/vllm/issues/11905, it would be highly beneficial to support running a single vLLM instance that exposes both `generate` and `embed` endpoints concurrently. Although this issue is marked as r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ultaneous generate and embed endpoints in a single vLLM instance feature request ### 🚀 The feature, motivation and pitch ## Feature Request: Enable simultaneous `generate` and `embed` endpoints in a single vLLM instance...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
