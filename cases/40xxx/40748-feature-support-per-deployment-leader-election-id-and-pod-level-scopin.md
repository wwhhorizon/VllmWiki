# vllm-project/vllm#40748: [Feature]: Support per-deployment leader election ID and pod-level  scoping for LoRA adapters in multi-deployment namespace setups

| 字段 | 值 |
| --- | --- |
| Issue | [#40748](https://github.com/vllm-project/vllm/issues/40748) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support per-deployment leader election ID and pod-level  scoping for LoRA adapters in multi-deployment namespace setups

### Issue 正文摘录

### 🚀 The feature, motivation and pitch are running multiple vLLM serving deployments (e.g., an H100 variant and a non-H100 variant) for the same model in a single Kubernetes namespace. In this setup, two problems arise: Problem 1: All LoRA controllers share a single hardcoded leader election lease All lmstack-lora-controller instances deployed across multiple Helm releases in the same namespace compete for the same hardcoded lease key (4549d26f.vllm.ai). Once one controller acquires the lease, all others are permanently blocked from reconciling — even though each controller is intended to manage adapters for its own Helm release. # vllm-gemma4-e4b-it-h100-lora-controller log (stuck for 4+ hours) I0423 19:11:47 leaderelection.go:257] attempting to acquire leader lease vllm/4549d26f.vllm.ai... The active controller does reconcile all LoraAdapter CRs in the namespace, which leads directly to Problem 2. Problem 2: Wrong pod selected when multiple deployments share the same model label When two Helm releases share the same modelSpec.name (e.g., both use gemma4-e4b-it because they serve the same model on different hardware), both pods receive the same model=gemma4-e4b-it label. The con...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: .ai). Once one controller acquires the lease, all others are permanently blocked from reconciling — even though each controller is intended to manage adapters for its own Helm release. # vllm-gemma4-e4b-it-h100-lora-con...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ation and pitch are running multiple vLLM serving deployments (e.g., an H100 variant and a non-H100 variant) for the same model in a single Kubernetes namespace. In this setup, two problems arise: Problem 1: All LoRA co...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: deployments (e.g., an H100 variant and a non-H100 variant) for the same model in a single Kubernetes namespace. In this setup, two problems arise: Problem 1: All LoRA controllers share a single hardcoded leader election...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ext The use case of running multiple hardware tiers (e.g., H100 for low-latency inference, L40s for cost-efficient batch inference) for the same model in a single namespace is increasingly common in production LLM servi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: troller acquires the lease, all others are permanently blocked from reconciling — even though each controller is intended to manage adapters for its own Helm release. # vllm-gemma4-e4b-it-h100-lora-controller log (stuck...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
