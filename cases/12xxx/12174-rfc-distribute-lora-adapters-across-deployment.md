# vllm-project/vllm#12174: [RFC]: Distribute LoRA adapters across deployment

| 字段 | 值 |
| --- | --- |
| Issue | [#12174](https://github.com/vllm-project/vllm/issues/12174) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Distribute LoRA adapters across deployment

### Issue 正文摘录

### Motivation. # Production LoRA serving This RFC lays out the current limitations in online LoRA serving, potential solutions, and a proposal for implementation. ## Context What we would like to offer SaaS products is a way to serve a single, multi-replica deployment of an LLM, where multiple tenants can each load or unload their own LoRA adapters for that LLM as needed without requiring downtime or redeployment. However, the only "non-development" way to serve LoRA adapters for online inference with vLLM today is to tell vLLM about them ahead of time with the `--lora-modules` CLI argument. This presents a problem for products that want to adopt vLLM for multi-tenant LoRA serving, as the only way to load a new adapter is to redeploy the entire service. There is a "development mode" method to dynamically load LoRA adapters: Setting `VLLM_ALLOW_RUNTIME_LORA_UPDATING=True` will enable the `/v1/load_lora_adapter` and `/v1/unload_lora_adapter` endpoints, which can be used to load or unload new LoRA adapters at runtime. However this is currently inappropriate for production use, because it neither: - Ensures the adapter is loaded across all replicas of the deployment - Guarantees that...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: that the LoRA adapters in question are either: 1. To be downloaded from HF Hub, or 2. Available on disk to the vLLM process The problem described here is tracking the metadata of which adapters should be loaded at any p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ly at the vLLM level, and have an external routing component ensure that requests are only routed to replicas which have the adapter loaded. For example, [kserve/modelmesh-serving](https://github.com/kserve/modelmesh-se...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: to the problem - Increases deployment complexity - Introduces deployment dependency on a third party component - Would collide with other routing strategies like - session aware routing - prefill/decode disaggregation #...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: pting generic URLs in `/v1/load_lora_adapter` payloads - Accepting a tar archive upload in `/v1/load/lora_adapter`, etc. ### Proposed Change. ## General Solution Ideas ### Option 1: Handle externally with smart routing...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: : - Distributed data stores like etcd are well-understood and production-tested - Backup and restore operations are relatively easy for service operators - Logic can be wrapped in atomic transactions to ensure consisten...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
