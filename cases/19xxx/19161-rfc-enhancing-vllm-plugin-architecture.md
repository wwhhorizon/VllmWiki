# vllm-project/vllm#19161: [RFC]: Enhancing vLLM Plugin Architecture

| 字段 | 值 |
| --- | --- |
| Issue | [#19161](https://github.com/vllm-project/vllm/issues/19161) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;ci_build;frontend_api;hardware_porting;model_support;moe |
| 子分类 | env_compat |
| Operator 关键词 | activation;operator |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Enhancing vLLM Plugin Architecture

### Issue 正文摘录

### Motivation. This RFC proposes changes to the vLLM plugin infrastructure to address compatibility issues, simplify out-of-tree code maintenance, and improve overall user experience. ### Problem Statement 1. **Registering and Dispatching Semi-Custom Operators:** - Vendors need a mechanism to register and dispatch custom implementations for generic layers like `RotaryEmbedding` and `RMSNorm` without modifying standard model code. - **Current Limitations:** - The existing [`forward_oot`](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/custom_op.py#L66-L69) method in `CustomOp` requires monkey-patching, which makes plugin code vulnerable to upstream changes. For example, [Ascend's RoPE](https://github.com/vllm-project/vllm-ascend/blob/main/vllm_ascend/ops/rotary_embedding.py#L273) implementation relies on layer properties that are not guaranteed, risking breakage with any refactor. - There is no straightforward way to dispatch new out-of-tree operators without altering model code, as seen with [AscendFusedMoE](https://github.com/vllm-project/vllm-ascend/blob/main/vllm_ascend/ops/fused_moe.py#L704) and custom [DeepSeek](https://github.com/vllm-project/vllm-ascend/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [RFC]: Enhancing vLLM Plugin Architecture RFC;stale ### Motivation. This RFC proposes changes to the vLLM plugin infrastructure to address compatibility issues, simplify out-of-tree code maintenance, and improve overall...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ve overall user experience. ### Problem Statement 1. **Registering and Dispatching Semi-Custom Operators:** - Vendors need a mechanism to register and dispatch custom implementations for generic layers like `RotaryEmbed...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [RFC]: Enhancing vLLM Plugin Architecture RFC;stale ### Motivation. This RFC proposes changes to the vLLM plugin infrastructure to address compatibility issues, simplify out-of-tree code maintenance, and improve overall...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: able - e.g. `vllm.v1.worker.gpu_input_batch.InputBatch`, `vllm.v1.sample.metadata.SamplingMetadata`, `vllm.sampling_params.SamplingType`) - Additionally: Lack of basic functionality checks for plugin compatibility in up...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: c layers like `RotaryEmbedding` and `RMSNorm` without modifying standard model code. - **Current Limitations:** - The existing [`forward_oot`](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/custom_op...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
