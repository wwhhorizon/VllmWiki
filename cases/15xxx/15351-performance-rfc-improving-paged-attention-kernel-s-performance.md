# vllm-project/vllm#15351: [Performance][RFC]: Improving  paged attention kernel's performance

| 字段 | 值 |
| --- | --- |
| Issue | [#15351](https://github.com/vllm-project/vllm/issues/15351) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache |
| 子分类 |  |
| Operator 关键词 | attention;cuda;kernel |
| 症状 |  |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance][RFC]: Improving  paged attention kernel's performance

### Issue 正文摘录

### Proposal to improve performance ## Motivation This issue would like to introduce a new kernel to improve the performance for paged attention, especially for `GQA`. ## Background For the paged attention benchmark: `python benchmarks/kernels/benchmark_paged_attention.py`, I found it use `GQA` to do inference, its `num-query-heads` is **64** by default, and `num-kv-heads` is **8** by default. Therefore **8** heads of a query will share a same head in key or value, but the current `v2` kernel organized thread blocks in such a grid: `(num_heads, num_seqs, max_num_partitions)`. Under such scenario, we could image that the different thread blocks with `blockIdx.x` as **1, 2, .. 8**, the indices are also the `query_head_idx`, will load same data in the **0th** head for both key and value, so it means we may load the key and value into different L1 cache or registers in different SMs up to **8** times, it's a **huge waste!!!** We could see there is **>800 MB** traffic between L1 and L2 cache, but both the key and value should be processed are only **64 MB**. ![Image](https://github.com/user-attachments/assets/0329a2bf-5a46-4f2f-9d60-ab481fae2b14) ## Optimization I supposed we could int...

## 现有链接修复摘要

#15353 [Kernel] introducing paged attention v3

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: troduce a new kernel to improve the performance for paged attention, especially for `GQA`. ## Background For the paged attention benchmark: `python benchmarks/kernels/benchmark_paged_attention.py`, I found it use `GQA`...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: load the key and value into different L1 cache or registers in different SMs up to **8** times, it's a **huge waste!!!** We could see there is **>800 MB** traffic between L1 and L2 cache, but both the key and value shou...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: attention, especially for `GQA`. ## Background For the paged attention benchmark: `python benchmarks/kernels/benchmark_paged_attention.py`, I found it use `GQA` to do inference, its `num-query-heads` is **64** by defaul...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: same head in key or value, but the current `v2` kernel organized thread blocks in such a grid: `(num_heads, num_seqs, max_num_partitions)`. Under such scenario, we could image that the different thread blocks with `bloc...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: heads=64, num_kv_heads=8, head_size=128, block_size=16, use_alibi=False, dtype='half', seed=0, profile=False, kv_cache_dtype='auto', custom_paged_attn=False) Warming up... Kernel running time: 443.387 us ``` ### V3 - op...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#15353](https://github.com/vllm-project/vllm/pull/15353) | closes_keyword | 0.95 | [Kernel] introducing paged attention v3 | FIX #15351 Please see details in the issue. |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
