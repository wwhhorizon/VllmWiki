# vllm-project/vllm#38523: [Feature]: Support `routed_experts` export in disaggregated Prefill/Decode serving

| 字段 | 值 |
| --- | --- |
| Issue | [#38523](https://github.com/vllm-project/vllm/issues/38523) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support `routed_experts` export in disaggregated Prefill/Decode serving

### Issue 正文摘录

### 🚀 The feature, motivation and pitch `enable_return_routed_experts` works for single-instance deployments, but it does not work end-to-end in disaggregated Prefill/Decode (PD) serving today. The current routed-experts implementation is based on local shared memory and local KV slot mapping, while the PD path only transfers `kv_transfer_params`. As a result, routed expert data produced on the prefill instance is not transferred to the decode instance, and the final response cannot return a complete routed-expert trace for the whole request. It would be helpful if vLLM could officially support routed-experts export in PD deployments, for example by: - carrying prefill-side routed expert data across the PD boundary - merging prefill and decode routed experts in the final output - exposing an optional `routed_experts` field in the response schema This would make `enable_return_routed_experts` usable for MoE debugging, router replay, and expert-load analysis in PD deployments as well. ### Alternatives An out-of-tree implementation can patch this behavior by serializing prefill routed experts into `kv_transfer_params`, merging them on the decode/serving side, and aggregating routed e...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: Support `routed_experts` export in disaggregated Prefill/Decode serving feature request ### 🚀 The feature, motivation and pitch `enable_return_routed_experts` works for single-instance deployments, but it doe...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Feature]: Support `routed_experts` export in disaggregated Prefill/Decode serving feature request ### 🚀 The feature, motivation and pitch `enable_return_routed_experts` works for single-instance deployments, but it doe...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: uted-experts implementation is based on local shared memory and local KV slot mapping, while the PD path only transfers `kv_transfer_params`. As a result, routed expert data produced on the prefill instance is not trans...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: pert trace for the whole request. It would be helpful if vLLM could officially support routed-experts export in PD deployments, for example by: - carrying prefill-side routed expert data across the PD boundary - merging...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ow. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
