# vllm-project/vllm#16473: [Performance]: Stability Concerns with LLaMA-4 Models After Extended Uptime (llama-4 models stability on h100 gpus)

| 字段 | 值 |
| --- | --- |
| Issue | [#16473](https://github.com/vllm-project/vllm/issues/16473) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | fp8 |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Stability Concerns with LLaMA-4 Models After Extended Uptime (llama-4 models stability on h100 gpus)

### Issue 正文摘录

### Proposal to improve performance Hi all, I wanted to check if anyone else has encountered stability issues with the LLaMA-4 models over extended periods of time. In our setup, the model functions as expected immediately after deployment or a restart. However, after approximately 24 to 36 hours, it stops responding to inference requests. I’ve verified that the underlying node conditions (including GPU health, memory, and system resources) remain healthy during this time. This behavior is consistent across restarts, where the model becomes unresponsive after running for a day or more. Is this a known issue with the current version of the model or vLLM backend? Has anyone else experienced similar behavior or found a workaround? Appreciate any insights. ### Report of performance regression Here is the config for this model which i deployed "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8". apiVersion: apps/v1 kind: Deployment metadata: annotations: deployment.kubernetes.io/revision: "4" meta.helm.sh/release-name: llama-4-maverick-instruct-fp8 meta.helm.sh/release-namespace: llms creationTimestamp: "2025-04-06T11:41:41Z" generation: 8 labels: app.kubernetes.io/instance: llama-4-ma...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: after running for a day or more. Is this a known issue with the current version of the model or vLLM backend? Has anyone else experienced similar behavior or found a workaround? Appreciate any insights. ### Report of pe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Performance]: Stability Concerns with LLaMA-4 Models After Extended Uptime (llama-4 models stability on h100 gpus) performance;stale ### Proposal to improve performance Hi all, I wanted to check if anyone else has enco...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: s model which i deployed "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8". apiVersion: apps/v1 kind: Deployment metadata: annotations: deployment.kubernetes.io/revision: "4" meta.helm.sh/release-name: llama-4-maveric...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: fter Extended Uptime (llama-4 models stability on h100 gpus) performance;stale ### Proposal to improve performance Hi all, I wanted to check if anyone else has encountered stability issues with the LLaMA-4 models over e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: s with LLaMA-4 Models After Extended Uptime (llama-4 models stability on h100 gpus) performance;stale ### Proposal to improve performance Hi all, I wanted to check if anyone else has encountered stability issues with th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
