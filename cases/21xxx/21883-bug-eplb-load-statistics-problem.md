# vllm-project/vllm#21883: [Bug]: EPLB load statistics problem

| 字段 | 值 |
| --- | --- |
| Issue | [#21883](https://github.com/vllm-project/vllm/issues/21883) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: EPLB load statistics problem

### Issue 正文摘录

### Your current environment A bug in load statistics: load statistics are collected during expert selection. However, only the top k experts for the current token that are routed to the local node are counted. The load of experts routed to other nodes is not counted. ### 🐛 Describe the bug https://github.com/vllm-project/vllm/blob/555e7225bcb9cdf9b037ce064e48987dbc3e13a0/vllm/model_executor/layers/fused_moe/layer.py#L1336 ``` if expert_map is not None: topk_ids_local = expert_map[topk_ids] topk_ids_flatten = topk_ids_local.flatten() else: topk_ids_flatten = topk_ids.flatten() # Should be equivalent to: # ``` # topk_ids_masked = topk_ids_local[topk_ids_local >= 0] # expert_load_view += topk_ids_masked.bincount( # minlength=expert_load_view.shape[0]) # ``` # We use `scatter_add_` since `bincount` cannot be compiled # Performance optimization: # `masked_fill` is significantly faster than `masked_select` invalid_mask = topk_ids_flatten < 0 # Replace invalid expert ids with 0 (just a dummy position) # to avoid out-of-bounds errors in scatter_add_ index = topk_ids_flatten.masked_fill_(invalid_mask, 0) # `src` is the valid mask, which is 1 for valid and 0 for invalid src = ~invalid_mask...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: nment A bug in load statistics: load statistics are collected during expert selection. However, only the top k experts for the current token that are routed to the local node are counted. The load of experts routed to o...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: # ``` # We use `scatter_add_` since `bincount` cannot be compiled # Performance optimization: # `masked_fill` is significantly faster than `masked_select` invalid_mask = topk_ids_flatten < 0 # Replace invalid expert ids...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: topk_ids_flatten = topk_ids_local.flatten() else: topk_ids_flatten = topk_ids.flatten() # Should be equivalent to: # ``` # topk_ids_masked = topk_ids_local[topk_ids_local >= 0] # expert_load_view += t
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: com/vllm-project/vllm/blob/555e7225bcb9cdf9b037ce064e48987dbc3e13a0/vllm/model_executor/layers/fused_moe/layer.py#L1336 ``` if expert_map is not None: topk_ids_local = expert_map[topk_ids] topk_ids_flatten = topk_ids_lo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
