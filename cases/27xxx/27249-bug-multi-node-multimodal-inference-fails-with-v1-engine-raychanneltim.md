# vllm-project/vllm#27249: [Bug]: Multi-node Multimodal Inference Fails with V1 Engine: `RayChannelTimeoutError` and `EngineDeadError`

| 字段 | 值 |
| --- | --- |
| Issue | [#27249](https://github.com/vllm-project/vllm/issues/27249) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;frontend_api;model_support;multimodal_vlm |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Multi-node Multimodal Inference Fails with V1 Engine: `RayChannelTimeoutError` and `EngineDeadError`

### Issue 正文摘录

## Summary When running multimodal models (vision-language models) in a multi-node distributed environment, vLLM's V1 engine consistently fails with `RayChannelTimeoutError` followed by `EngineDeadError`. This issue occurs in both v0.9.2 (with `VLLM_USE_V1=1`) and v0.11.0 (which defaults to V1 engine). The V0 engine works correctly under the same configuration. **Key Observations:** - Workers hang indefinitely during model execution - no output is ever produced - NCCL communication initializes successfully - Increasing timeouts does not resolve the issue ## Environment ### Hardware Configuration - **Nodes**: 2 nodes - **GPUs**: 8x NVIDIA H100 80GB HBM3 per node (16 GPUs total) - **GPU Topology**: All GPUs connected via NVLink (NV18) - **Network**: InfiniBand disabled (`NCCL_IB_DISABLE=1`), using Ethernet (ens3f0, ens1f0) - **CPU**: Intel Xeon Platinum 8468 - **NVIDIA Driver**: 550.163.01 ### Software Configuration - **CUDA**: 12.8.93 - **NCCL**: 2.25.1-1 (v0.9.2), 2.27.3 (v0.11.0) - **PyTorch**: 2.7.0+cu128 (v0.9.2), 2.8.0+cu128 (v0.11.0) - **vLLM**: v0.9.2, v0.11.0 ### Test Matrix #### meta-llama/Llama-4-Maverick-17B-128E-Instruct | vLLM Version | Engine | Status | | ------------...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Multi-node Multimodal Inference Fails with V1 Engine: `RayChannelTimeoutError` and `EngineDeadError` bug;stale ## Summary When running multimodal models (vision-language models) in a multi-node distributed enviro...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: M3 per node (16 GPUs total) - **GPU Topology**: All GPUs connected via NVLink (NV18) - **Network**: InfiniBand disabled (`NCCL_IB_DISABLE=1`), using Ethernet (ens3f0, ens1f0) - **CPU**: Intel Xeon Platinum 8468 - **NVID...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ### Hardware Configuration - **Nodes**: 2 nodes - **GPUs**: 8x NVIDIA H100 80GB HBM3 per node (16 GPUs total) - **GPU Topology**: All GPUs connected via NVLink (NV18) - **Network**: InfiniBand disabled (`NCCL_IB_DISABLE...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: Fails with V1 Engine: `RayChannelTimeoutError` and `EngineDeadError` bug;stale ## Summary When running multimodal models (vision-language models) in a multi-node distributed environment, vLLM's V1 engine consistently fa...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: iled | | v0.11.0 | V1 (default) | ❌ Failed | ## Steps to Reproduce 1. **Setup multi-node environment** with 2 nodes, each with 8 GPUs 2. **Configure vLLM** with the following settings: ```bash VLLM_USE_V1=1 # For v0.9.2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
