# vllm-project/vllm#21721: [Bug]: Unnecessary CPU block allocation during swap_out from GPU to CPU

| 字段 | 值 |
| --- | --- |
| Issue | [#21721](https://github.com/vllm-project/vllm/issues/21721) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Unnecessary CPU block allocation during swap_out from GPU to CPU

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In the swap_out function of vllm/core/block_manager.py, I observed that when this function is executed on a sequence group sharing the same prompt, CPU blocks are allocated for each sequence. This seems to result in unnecessary allocations. When allocating for GPU, physical block IDs are properly forked to prevent duplication, but during swap operations, duplicate allocations occur. I believe a separate deduplication algorithm should be implemented to prevent this issue. Here’s my hypothesis: when performing swap_out(sequence group a) on two sequence groups, a_1 and a_2, the process would execute as follows: Hypothesis: Sequence Group a: a_1 = [ i, love ] [ you, but ] [ the, dog ] a_2 = [ i, love ] [ you, however ] [ that, cat ] First iteration: Blocks: [ i, love ] [ you, but ] [ the, dog ] Call self.block_allocator.swap src_block_ids = GPU block ID list, e.g., [0, 15, 9] Call self._allocators[gpu].swap_out(blocks) Block objects’ block IDs for [ i, love ] [ you, but ] [ the, dog ] are all set to None [ you, but ] [ the, dog ] physical blocks are freed; [ i, love ] has refcount=1, so it’s not yet freed. Call self._allocators[cpu]....

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: Unnecessary CPU block allocation during swap_out from GPU to CPU bug;stale ### Your current environment ### 🐛 Describe the bug In the swap_out function of vllm/core/block_manager.py, I observed that when this fun...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ap. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: 9: 50} current_swap_mapping = {0: 29, 15: 17, 9: 50} Return from swap Block table's block ID list is updated to: physical_block_id_mapping = {(0, 29), (15, 17), (9, 50)} Second iteration: Blocks: [ i, love ] [ you, howe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: g]: Unnecessary CPU block allocation during swap_out from GPU to CPU bug;stale ### Your current environment ### 🐛 Describe the bug In the swap_out function of vllm/core/block_manager.py, I observed that when this functi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
