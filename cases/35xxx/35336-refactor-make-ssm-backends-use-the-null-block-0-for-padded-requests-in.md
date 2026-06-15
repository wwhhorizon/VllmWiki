# vllm-project/vllm#35336: [Refactor]: Make SSM backends use the null block (0) for padded requests instead of -1

| 字段 | 值 |
| --- | --- |
| Issue | [#35336](https://github.com/vllm-project/vllm/issues/35336) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Refactor]: Make SSM backends use the null block (0) for padded requests instead of -1

### Issue 正文摘录

Currently we fill the block table with -1's in the GPU model runner for padded requests for mamba/ssm backends: https://github.com/vllm-project/vllm/blob/c97234c08b42326cf1e5ef024d9ac8441e0848b1/vllm/v1/worker/gpu_model_runner.py#L1778-L1780 To match the fact that the mamba kernels use [PAD_SLOT_ID](https://github.com/vllm-project/vllm/blob/c97234c08b42326cf1e5ef024d9ac8441e0848b1/vllm/v1/attention/backends/utils.py#L44) to indicate an unused block in the block table (for padded requests). https://github.com/vllm-project/vllm/blob/c97234c08b42326cf1e5ef024d9ac8441e0848b1/vllm/model_executor/layers/mamba/ops/mamba_ssm.py#L495 The -1 (indicated by `PAD_SLOT_ID=-1`) is intended to be used with the slot_mapping not the block table which already reserves block 0 as the "null block". We should update the padding to use `0` to align with the concept of the null block and avoid having to clamp: https://github.com/vllm-project/vllm/blob/c97234c08b42326cf1e5ef024d9ac8441e0848b1/vllm/v1/attention/backends/mla/indexer.py#L352-L356 NOTE: there seems to be many places in the ssm code paths that implicitly assume that padded blocks are -1, we will have to thoroughly test models that use ssm back...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Refactor]: Make SSM backends use the null block (0) for padded requests instead of -1 feature request Currently we fill the block table with -1's in the GPU model runner for padded requests for mamba/ssm backends: http...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Refactor]: Make SSM backends use the null block (0) for padded requests instead of -1 feature request Currently we fill the block table with -1's in the GPU model runner for padded requests for mamba/ssm backends: http...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 356 NOTE: there seems to be many places in the ssm code paths that implicitly assume that padded blocks are -1, we will have to thoroughly test models that use ssm backends like mamba, mamba2, gdn attention etc.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Refactor]: Make SSM backends use the null block (0) for padded requests instead of -1 feature request Currently we fill the block table with -1's in the GPU model runner for padded requests for mamba/ssm backends: http...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: for padded requests instead of -1 feature request Currently we fill the block table with -1's in the GPU model runner for padded requests for mamba/ssm backends: https://github.com/vllm-project/vllm/blob/c97234c08b42326...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
