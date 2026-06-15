# vllm-project/vllm#29508: [Feature]: Conformance test for Gateway API Inference Extension

| 字段 | 值 |
| --- | --- |
| Issue | [#29508](https://github.com/vllm-project/vllm/issues/29508) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Conformance test for Gateway API Inference Extension

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The Gateway API Inference Extension projects defines a [model server protocol](https://github.com/kubernetes-sigs/gateway-api-inference-extension/tree/main/docs/proposals/003-model-server-protocol) which it uses to do intelligent request scheduling, such as scheduling requests based on kv cache utilization of vLLM. Yet rapid vllm developments can break that protocol, leading to degraded performance, e.g., https://github.com/vllm-project/vllm/pull/18354/ renamed the `gpu_cache_usage_perc` metric to `kv_cache_usage_perc`. To prevent such breaking changes, we should add CI conformance tests with owners/contacts. If such changes must happen, the contacts should be notified and migration/mitigation plans should be discussed. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Conformance test for Gateway API Inference Extension feature request;stale ### 🚀 The feature, motivation and pitch The Gateway API Inference Extension projects defines a [model server protocol](https://github...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: `kv_cache_usage_perc`. To prevent such breaking changes, we should add CI conformance tests with owners/contacts. If such changes must happen, the contacts should be notified and migration/mitigation plans should be dis...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: do intelligent request scheduling, such as scheduling requests based on kv cache utilization of vLLM. Yet rapid vllm developments can break that protocol, leading to degraded performance, e.g., https://github.com/vllm-p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ation and pitch The Gateway API Inference Extension projects defines a [model server protocol](https://github.com/kubernetes-sigs/gateway-api-inference-extension/tree/main/docs/proposals/003-model-server-protocol) which...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
