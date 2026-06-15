# vllm-project/vllm#33169: [Feature]: Add environment variable support for configuring NIXL disaggregation backend

| 字段 | 值 |
| --- | --- |
| Issue | [#33169](https://github.com/vllm-project/vllm/issues/33169) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add environment variable support for configuring NIXL disaggregation backend

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Until recently, NIXL only supported UCX as the transport backend for disaggregated use cases. With the introduction of additional backends(plugins) like LIBFABRIC, users can now configure the backend via the kv_transfer_config.kv_connector_extra_config parameter (https://github.com/vllm-project/vllm/blob/main/vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py#L867). Currently, switching between backends requires modifying the `kv_transfer_config` parameter. This can be challenging in environments where: - Backend selection needs to be dynamic based on the deployment environment - Multiple frameworks built on top of vLLM (Ray, Dynamo, etc.) each manage configuration differently I suggest we Introduce a new environment variable `VLLM_NIXL_DISAGGREGATION_BACKEND` that allows users to configure the NIXL backend for disaggregation. This would: - Provide a simpler, environment-based configuration method - Work alongside the existing kv_transfer_config parameter (not replace it) - Enable easier backend switching across different deployment scenarios without code changes This will simplify configuration management across different enviro...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ent variable support for configuring NIXL disaggregation backend feature request;stale ### 🚀 The feature, motivation and pitch Until recently, NIXL only supported UCX as the transport backend for disaggregated use cases...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: e]: Add environment variable support for configuring NIXL disaggregation backend feature request;stale ### 🚀 The feature, motivation and pitch Until recently, NIXL only supported UCX as the transport backend for disaggr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Add environment variable support for configuring NIXL disaggregation backend feature request;stale ### 🚀 The feature, motivation and pitch Until recently, NIXL only supported UCX as the transport backend for...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
