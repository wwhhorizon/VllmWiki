# vllm-project/vllm#27917: [Bug]: Potential Out-of-bounds in moe_align_sum_kernels.cu

| 字段 | 值 |
| --- | --- |
| Issue | [#27917](https://github.com/vllm-project/vllm/issues/27917) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | moe |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;moe |
| 症状 |  |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Potential Out-of-bounds in moe_align_sum_kernels.cu

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug While performing static analysis on CUDA kernels, I identified potential out-of-bounds accesses in the moe_align_block_size kernels. #### 1. sorted_token_ids[rank_post_pad] in moe_align_block_size_small_batch_expert_kernel https://github.com/vllm-project/vllm/blob/a00d6254e998be472d8df9dc590784d6facf8d85/csrc/moe/moe_align_sum_kernels.cu#L261-L265 The rank_post_pad may exceed the bounds of sorted_token_ids, leading to invalid memory access. index: ```rank_post_pad = tokens_cnts[num_experts * threadIdx.x + topk_ids[i]] + cumsum[topk_ids[i]]``` Example Scenario: ``` i = 0 topk_ids[0] = 7 cumsum[7] = 488 tokens_cnts[7] = 4 threadIdx.x = 0 expert_ids.shape = [31] block_size = 16 sorted_token_ids.shape = [492] ``` #### 2. sorted_token_ids[rank_post_pad] in count_and_sort_expert_tokens_kernel https://github.com/vllm-project/vllm/blob/a00d6254e998be472d8df9dc590784d6facf8d85/csrc/moe/moe_align_sum_kernels.cu#L170-L176 The computed rank_post_pad exceeds the valid range of sorted_token_ids, causing out-of-bounds access. ```rank_post_pad=cumsum_buffer[topk_ids[i]]+1``` Example Scenario: ``` expert_ids.shape = [241] i = 0 topk_ids[0] = 7 cu...

## 现有链接修复摘要

#27923 [Bugfix] Potential Out-of-bounds in moe_align_sum_kernels.cu

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ironment ### 🐛 Describe the bug While performing static analysis on CUDA kernels, I identified potential out-of-bounds accesses in the moe_align_block_size kernels. #### 1. sorted_token_ids[rank_post_pad] in moe_align_b...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: Potential Out-of-bounds in moe_align_sum_kernels.cu bug;stale ### Your current environment ### 🐛 Describe the bug While performing static analysis on CUDA kernels, I identified potential out-of-bounds accesses in...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: lots of frequently asked questions. performance moe cuda;kernel;moe env_dependency;shape #27923 [Bugfix] Potential Out-of-bounds in moe_align_sum_kernels.cu Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: kernels, I identified potential out-of-bounds accesses in the moe_align_block_size kernels. #### 1. sorted_token_ids[rank_post_pad] in moe_align_block_size_small_batch_expert_kernel https://github.com/vllm-project/vllm/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Potential Out-of-bounds in moe_align_sum_kernels.cu bug;stale ### Your current environment ### 🐛 Describe the bug While performing static analysis on CUDA kernels, I identified potential out-of-bounds accesses in...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#27923](https://github.com/vllm-project/vllm/pull/27923) | closes_keyword | 0.95 | [Bugfix] Potential Out-of-bounds in moe_align_sum_kernels.cu | Fixes #27917. This ensures the MoE alignment CUDA kernels guard against invalid expert IDs and cap per-expert offsets to their padded ranges. This keeps writes to `sorted_token_id |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
