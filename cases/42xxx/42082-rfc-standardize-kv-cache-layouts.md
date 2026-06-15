# vllm-project/vllm#42082: [RFC]: Standardize KV-cache Layouts

| 字段 | 值 |
| --- | --- |
| Issue | [#42082](https://github.com/vllm-project/vllm/issues/42082) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Standardize KV-cache Layouts

### Issue 正文摘录

# Motivation Right now attention backends can semantically different and physically different KV-cache layouts. This leads to messy KV-connector code (i.e. lots of `is_mamba` and `is_mla` flags), and creates a tight coupling between KV-connector and the attention backends, e.g. https://github.com/vllm-project/vllm/blob/4140faa4a51d42cb9618949bee28fd47682f611c/vllm/v1/attention/backends/flash_attn.py#L152-L171 This also leads to other related bugs like: https://github.com/vllm-project/vllm/pull/41657#issuecomment-4400641394 More details in: https://docs.google.com/document/d/1-TnWZf8jI6nWgE-xaQkgsWy130CVUqqt1NYqY-mAOe4/edit?usp=sharing # Proposed Change ## Standard Logical Shape ``` [num_layers_slots, num_blocks, num_heads, num_states, ] ``` Where: - **num\_states** — token positions per block (or 1 for recurrent state) - **num\_heads** — heads (or 1 for headless backends like MLA) - **\ ** — backend-specific, always contiguous Every backend maps to this shape: | Backend | num\_states | num\_heads | state\_content | | :---- | :---- | :---- | :---- | | GQA | `block_size` | `num_kv_heads` | `[2, head_dim]` | | DeepSeek V4 (c4a, 1 layer type example) | `block_size/4` | 1 | `[latent_si...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 7: [RFC]: Standardize KV-cache Layouts RFC # Motivation Right now attention backends can semantically different and physically different KV-cache layouts. This leads to messy KV-connector code (i.e. lots of `is_mamba` and...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [RFC]: Standardize KV-cache Layouts RFC # Motivation Right now attention backends can semantically different and physically different KV-cache layouts. This leads to messy KV-connector code (i.e. lots of `is_mamba` and...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: RFC]: Standardize KV-cache Layouts RFC # Motivation Right now attention backends can semantically different and physically different KV-cache layouts. This leads to messy KV-connector code (i.e. lots of `is_mamba` and `...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ** — heads (or 1 for headless backends like MLA) - **\ ** — backend-specific, always contiguous Every backend maps to this shape: | Backend | num\_states | num\_heads | state\_content | | :---- | :---- | :---- | :---- |...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: t_size]` | | Mamba2 Conv | 1 | 1 | `[conv_dim/tp, kernel-1]` | | Mamba2 SSM | 1 | `num_heads` | `[head_dim, state_size]` | --- ### Stride Order: Logical Shape vs Physical Layout The **semantic shape** is always `[layer_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
