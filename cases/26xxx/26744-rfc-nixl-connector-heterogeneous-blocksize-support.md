# vllm-project/vllm#26744: [RFC]: Nixl Connector Heterogeneous BlockSize support

| 字段 | 值 |
| --- | --- |
| Issue | [#26744](https://github.com/vllm-project/vllm/issues/26744) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Nixl Connector Heterogeneous BlockSize support

### Issue 正文摘录

### Motivation. To support scenarios when prefill and decode have their own preferred block_size. Ex: Prefill with CUDA(16 as block_size) and decode with Intel Gaudi(128 as block_size) ### Proposed Change. **edition2(latest proposal)** - update add_remote_agent to prepare xfer_buffer with **local block_size** - update read_block to map remote_block_ids/local_block_ids - update in get_finished for necessary pos-process One liner: Always using larger block_size as copy unit, do post processing after receiving to split/merge blocks Reason: For HND, memory is contiguous as block0_head0, block0_head1,... block1_head0, block1_head1.. Copy multiple blocks will leads to post-processing work after receiving case1: prefill Block_size case2: prefill block_size > decode blocksize == old proposal => proved wrong after hands on (not working for HND) --- Scenario1: prefill blk_size // decode blk_size = 1/4; prefill TP // decode TP = 1/2 Potential Overhead: Redundant blocks will be read when req num_tokens can't be divided by local_block_size. For example, remote block_size is 4, local block_size is 16, req_num_tokens=24, total 6 blocks used in remote. while total 2 blocks used in local which tak...

## 现有链接修复摘要

#26759 [NIXL] heterogeneous block_size support

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: [RFC]: Nixl Connector Heterogeneous BlockSize support RFC;stale ### Motivation. To support scenarios when prefill and decode have their own preferred block_size. Ex: Prefill with CUDA(16 as block_size) and decode with I...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: prefill and decode have their own preferred block_size. Ex: Prefill with CUDA(16 as block_size) and decode with Intel Gaudi(128 as block_size) ### Proposed Change. **edition2(latest proposal)** - update add_remote_agent...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC]: Nixl Connector Heterogeneous BlockSize support RFC;stale ### Motivation. To support scenarios when prefill and decode have their own preferred block_size. Ex: Prefill with CUDA(16 as block_size) and decode with I...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: l block_size => using remote block_size will need significant change for build_connector_metadata and workflow. --- Scenario2: prefill blk_size // decode blk_size = 4; prefill TP // decode TP = 1/2 Potential Overhead: r...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: e with Intel Gaudi(128 as block_size) ### Proposed Change. **edition2(latest proposal)** - update add_remote_agent to prepare xfer_buffer with **local block_size** - update read_block to map remote_block_ids/local_block...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#26759](https://github.com/vllm-project/vllm/pull/26759) | mentioned | 0.6 | [NIXL] heterogeneous block_size support | decode with Intel Gaudi(128 as block_size) More details describe in #26744 ### Current status: - Prefill BlockSize < DecodeBlockSize - NHD => accuracy is good - HND => accura |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
