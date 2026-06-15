# vllm-project/vllm#27909: [Bug]: Potential Out-of-bounds in cache_kernels.cu

| 字段 | 值 |
| --- | --- |
| Issue | [#27909](https://github.com/vllm-project/vllm/issues/27909) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache |
| 子分类 |  |
| Operator 关键词 | cuda;kernel |
| 症状 |  |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Potential Out-of-bounds in cache_kernels.cu

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug While performing static analysis on CUDA kernels, I identified potential out-of-bounds accesses in the gather_and_maybe_dequant_cache kernel in cache_kernels.cu. **1. batch_block_table[pid]** https://github.com/vllm-project/vllm/blob/a00d6254e998be472d8df9dc590784d6facf8d85/csrc/cache_kernels.cu#L968-L969 batch_block_table[pid] may lead to an out-of-bounds access. ```block_table``` has shape: ```[1, u0]``` ``` index = batch_offset + offset + pid = blockIdx.x * block_table_stride + seq_starts[bid] / block_size + pid = blockIdx.x * u0 + seq_starts[blockIdx.x] / 64 + pid ``` Example Scenario ``` batch_block_table.shape: [1, 2] blockIdx.x: 0 blockIdx.y: 0 seq_starts[0]: 128 pid: 0 ``` Under these conditions, batch_block_table[pid] accesses invalid memory due to an out-of-bounds index. **2. batch_block_table[full_blocks_end]** https://github.com/vllm-project/vllm/blob/a00d6254e998be472d8df9dc590784d6facf8d85/csrc/cache_kernels.cu#L978-L979 Similarly, batch_block_table[full_blocks_end] may also lead to an out-of-bounds access. Example Scenario ``` batch_block_table.shape: [1, 2] blockIdx.x: 0 blockIdx.y: 0 seq_starts[0]: 128 cu_seq_len...

## 现有链接修复摘要

#28760 [Bugfix][cache_kernels]: Fix OOB in cache_kernels.cu | #34393 [Kernel]: Unify MLA cache gather into single gather_cache entry point

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: s, I identified potential out-of-bounds accesses in the gather_and_maybe_dequant_cache kernel in cache_kernels.cu. **1. batch_block_table[pid]** https://github.com/vllm-project/vllm/blob/a00d6254e998be472d8df9dc590784d6...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ironment ### 🐛 Describe the bug While performing static analysis on CUDA kernels, I identified potential out-of-bounds accesses in the gather_and_maybe_dequant_cache kernel in cache_kernels.cu. **1. batch_block_table[pi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: he gather_and_maybe_dequant_cache kernel in cache_kernels.cu. **1. batch_block_table[pid]** https://github.com/vllm-project/vllm/blob/a00d6254e998be472d8df9dc590784d6facf8d85/csrc/cache_kernels.cu#L968-L969 batch_block_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: equently asked questions. performance attention_kv_cache cuda;kernel env_dependency;shape #28760 [Bugfix][cache_kernels]: Fix OOB in cache_kernels.cu | #34393 [Kernel]: Unify MLA cache gather into single gather_cache en...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Potential Out-of-bounds in cache_kernels.cu bug;stale ### Your current environment ### 🐛 Describe the bug While performing static analysis on CUDA kernels, I identified potential out-of-bounds accesses in the gat...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#28760](https://github.com/vllm-project/vllm/pull/28760) | closes_keyword | 0.95 | [Bugfix][cache_kernels]: Fix OOB in cache_kernels.cu | fixes a potential out-of-bounds (OOB) memory access in the gather_and_maybe_dequant_cache CUDA kernel, as originally reported in Issue #27909. The bug was identified by static ana |
| [#34393](https://github.com/vllm-project/vllm/pull/34393) | mentioned | 0.6 | [Kernel]: Unify MLA cache gather into single gather_cache entry point | - test_gather_cache_oob — boundary check for block_table OOB (Issue #27909) - test_gather_cache_token_major_zero_tokens_noop — zero-token early exit - test_gather_cache_batch_major |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
