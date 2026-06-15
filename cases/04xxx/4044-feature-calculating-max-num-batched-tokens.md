# vllm-project/vllm#4044: [Feature]: Calculating `max_num_batched_tokens`

| 字段 | 值 |
| --- | --- |
| Issue | [#4044](https://github.com/vllm-project/vllm/issues/4044) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Calculating `max_num_batched_tokens`

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently the user is required to determine `max_num_batched_tokens`, otherwise it will be by default `max(max_model_len, 2048)`. However, the user does not receive any guideline to determine the number. If the number is too small, it will result in suboptimal throughput due to small batch size. If the number is too big, it will left few memory for KV cache, resulting in small `num_gpu_blocks` and frequent offloading or recomputation. ### Alternatives `max_num_batched_tokens` should be calculated in `determine_num_available_blocks` if the user does not explicitly specify it. ### Additional context _No response_

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: small batch size. If the number is too big, it will left few memory for KV cache, resulting in small `num_gpu_blocks` and frequent offloading or recomputation. ### Alternatives `max_num_batched_tokens` should be calcula...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: calculated in `determine_num_available_blocks` if the user does not explicitly specify it. ### Additional context _No response_
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: not receive any guideline to determine the number. If the number is too small, it will result in suboptimal throughput due to small batch size. If the number is too big, it will left few memory for KV cache, resulting i...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: o big, it will left few memory for KV cache, resulting in small `num_gpu_blocks` and frequent offloading or recomputation. ### Alternatives `max_num_batched_tokens` should be calculated in `determine_num_available_block...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: rmine `max_num_batched_tokens`, otherwise it will be by default `max(max_model_len, 2048)`. However, the user does not receive any guideline to determine the number. If the number is too small, it will result in subopti...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
