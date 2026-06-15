# vllm-project/vllm#37084: Core Engine: Weight Loading Cleanup - Standardize load_weights API

| 字段 | 值 |
| --- | --- |
| Issue | [#37084](https://github.com/vllm-project/vllm/issues/37084) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Core Engine: Weight Loading Cleanup - Standardize load_weights API

### Issue 正文摘录

## Description This issue tracks the effort to standardize the `load_weights` API across all models in vLLM, as outlined in the [vLLM Roadmap Q1 2026 (Issue 32455)]. ### Problem Currently, most models implement their own imperative `load_weights` methods. This leads to: * Massive code duplication (e.g., fusing `q_proj`, `k_proj`, `v_proj` into `qkv_proj`). * Fragility when adding support for new formats like TorchAO or FP8 KV scales. * Complexity in MoE models routing expert weights to local shards. ### Proposed Solution Decouple model architecture definitions from the mechanics of weight loading by expanding the capabilities of `AutoWeightsLoader` and `WeightsMapper`. ### Tasks - [x] Enhance `AutoWeightsLoader` to support `stacked_params_mapping` and `expert_params_mapping`. - [x] Centralize FP8 / KV scale remapping logic within the loader. - [x] Migrate Tier 1 standard architectures (starting with `LlamaForCausalLM`) to use the new declarative loader. - [ ] Migrate Tier 2 MoE models. - [ ] Migrate Tier 3 highly custom models. - [ ] Enforce strict loader compliance and update documentation.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: issue tracks the effort to standardize the `load_weights` API across all models in vLLM, as outlined in the [vLLM Roadmap Q1 2026 (Issue 32455)]. ### Problem Currently, most models implement their own imperative `load_w...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: support for new formats like TorchAO or FP8 KV scales. * Complexity in MoE models routing expert weights to local shards. ### Proposed Solution Decouple model architecture definitions from the mechanics of weight loadin...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: roj`). * Fragility when adding support for new formats like TorchAO or FP8 KV scales. * Complexity in MoE models routing expert weights to local shards. ### Proposed Solution Decouple model architecture definitions from...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ng expert weights to local shards. ### Proposed Solution Decouple model architecture definitions from the mechanics of weight loading by expanding the capabilities of `AutoWeightsLoader` and `WeightsMapper`. ### Tasks -...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: new formats like TorchAO or FP8 KV scales. * Complexity in MoE models routing expert weights to local shards. ### Proposed Solution Decouple model architecture definitions from the mechanics of weight loading by expandi...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
