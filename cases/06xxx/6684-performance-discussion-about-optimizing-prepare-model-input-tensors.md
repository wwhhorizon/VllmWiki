# vllm-project/vllm#6684: [Performance]: Discussion about optimizing _prepare_model_input_tensors

| 字段 | 值 |
| --- | --- |
| Issue | [#6684](https://github.com/vllm-project/vllm/issues/6684) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel |
| 子分类 |  |
| Operator 关键词 | cuda;kernel |
| 症状 |  |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Performance]: Discussion about optimizing _prepare_model_input_tensors

### Issue 正文摘录

### Misc discussion on performance Checking #6164, _prepare_model_input_tensors has been refactored for the purpose of performance improvement. I investigated the performance of _prepare_model_input_tensors with respect to different batch sizes, input sequence length, output sequence length and tensor parallel nums through running benchmark_latency.py. I found a directly proportional relationship between the time duration of _prepare_model_input_tensors and batch sizes (aka seq_group), which is a obvious operation that can be speeded up through parallelizing the loop in _prepare_model_input_tensors. Here comes my questions related to the follow up mentioned in #6164: 1. What will the design of "Parallelize the loop ```for seq_group_metadata in seq_group_metadata_list``` " to speed up? Using threadpool? 2. Are we going to implement a cuda kernel that can "Remove the loop for seq_id in seq_ids in ModelRunnerInputBuilder._add_seq_group()"? 3. When will these follow-up optimizations be available? I would like to know if I can give contributions.

## 现有链接修复摘要

#6164 [Core] Refactor _prepare_model_input_tensors - take 2

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: h running benchmark_latency.py. I found a directly proportional relationship between the time duration of _prepare_model_input_tensors and batch sizes (aka seq_group), which is a obvious operation that can be speeded up...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: length, output sequence length and tensor parallel nums through running benchmark_latency.py. I found a directly proportional relationship between the time duration of _prepare_model_input_tensors and batch sizes (aka s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ernel that can "Remove the loop for seq_id in seq_ids in ModelRunnerInputBuilder._add_seq_group()"? 3. When will these follow-up optimizations be available? I would like to know if I can give contributions. performance...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 164: 1. What will the design of "Parallelize the loop ```for seq_group_metadata in seq_group_metadata_list``` " to speed up? Using threadpool? 2. Are we going to implement a cuda kernel that can "Remove the loop for seq...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Performance]: Discussion about optimizing _prepare_model_input_tensors performance;stale ### Misc discussion on performance Checking #6164, _prepare_model_input_tensors has been refactored for the purpose of performanc...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#6164](https://github.com/vllm-project/vllm/pull/6164) | mentioned | 0.45 | [Core] Refactor _prepare_model_input_tensors - take 2 | ensors. here comes my questions related to the follow up mentioned in #6164: 1. what will the design of "parallelize the loop ```for seq_group_metadata in seq_group_metadata_list`… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
