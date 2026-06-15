# vllm-project/vllm#27656: [Bug]: Potential out-of-bounds access in paged_attention_v1.cu and paged_attention_v2.cu

| 字段 | 值 |
| --- | --- |
| Issue | [#27656](https://github.com/vllm-project/vllm/issues/27656) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache |
| 子分类 | memory |
| Operator 关键词 | attention;cuda |
| 症状 |  |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Potential out-of-bounds access in paged_attention_v1.cu and paged_attention_v2.cu

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm performing static analysis on CUDA programs and have identified potential out-of-bounds access in paged_attention_v1.cu and paged_attention_v2.cu. ### block_tables[block_idx ] https://github.com/vllm-project/vllm/blob/a00d6254e998be472d8df9dc590784d6facf8d85/csrc/attention/attention_kernels.cuh#L252-L253 https://github.com/vllm-project/vllm/blob/a00d6254e998be472d8df9dc590784d6facf8d85/csrc/attention/attention_kernels.cuh#L389-L390 The shape of block_tables is: ``` [num_seqs, max_num_blocks_per_seq] ``` However, block_idx may exceed ```num_seqs*max_num_blocks_per_seq-1```. **Example Scenario** ``` num_seqs = 2 max_num_blocks_per_seq = 2 blockIdx.y = 1 seq_lens[1] = 256 threadIdx.x = 0 ``` During the second iteration, the computed index block_idx becomes 4, which is out of bounds for block_tables (whose valid range is [0, 3] in this case). ### *max_logits_ptr In paged_attention_v2, ```*max_logits_ptr ``` may also lead to an out-of-bounds access. https://github.com/vllm-project/vllm/blob/a00d6254e998be472d8df9dc590784d6facf8d85/csrc/attention/attention_kernels.cuh#L344-L352 The shape of max_logits is: ``` [batch_size, 32, 2] ``...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nvironment ### 🐛 Describe the bug I'm performing static analysis on CUDA programs and have identified potential out-of-bounds access in paged_attention_v1.cu and paged_attention_v2.cu. ### block_tables[block_idx ] https...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ently asked questions. performance attention_kv_cache attention;cuda env_dependency;shape Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: f-bounds access in paged_attention_v1.cu and paged_attention_v2.cu. ### block_tables[block_idx ] https://github.com/vllm-project/vllm/blob/a00d6254e998be472d8df9dc590784d6facf8d85/csrc/attention/attention_kernels.cuh#L2...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: -of-bounds access in paged_attention_v1.cu and paged_attention_v2.cu bug;stale ### Your current environment ### 🐛 Describe the bug I'm performing static analysis on CUDA programs and have identified potential out-of-bou...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance attention_kv_cache attention;cuda env_dependency;shape Your current envir...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
