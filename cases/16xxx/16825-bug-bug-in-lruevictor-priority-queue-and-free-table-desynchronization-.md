# vllm-project/vllm#16825: [Bug]: Bug in LRUEvictor: priority_queue and free_table desynchronization cause error

| 字段 | 值 |
| --- | --- |
| Issue | [#16825](https://github.com/vllm-project/vllm/issues/16825) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Bug in LRUEvictor: priority_queue and free_table desynchronization cause error

### Issue 正文摘录

### Your current environment vllm 0.7.3 ### 🐛 Describe the bug ### Your current environment vllm 0.7.3 ### 🐛 Describe the bug We encountered a bug in the LRUEvictor implementation when running VLLM (version 0.7.3) with the --preemption-mode swap flag. The issue arises due to desynchronization between self.priority_queue and self.free_table in the remove method. Add logging to evictor.py and prefix_caching_block.py to track block additions and removals. The issue by observing the following sequence: line 25: block (block_id=862 content_hash=4781171782003088483 num_hashed_tokens=768 last_accessed=-1) is added to self.free_table and self.priority_queue. (in add method) line 26: The block is removed from self.free_table but remains in self.priority_queue. (in remove method, only self.free_table is altered) line 28: The block is added again to self.free_table and self.priority_queue. (in add method) line 29: The block is removed from self.free_table, and the one added in line 25 is removed from self.priority_queue. (in evict method) line 31: block(block_id=862 content_hash=-1708738876872868168 num_hashed_tokens=192 last_accessed=-1) is added to self.free_table and self.priority_queue....

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ble in the remove method. Add logging to evictor.py and prefix_caching_block.py to track block additions and removals. The issue by observing the following sequence: line 25: block (block_id=862 content_hash=47811717820...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Bug in LRUEvictor: priority_queue and free_table desynchronization cause error bug;stale ### Your current environment vllm 0.7.3 ### 🐛 Describe the bug ### Your current environment vllm 0.7.3 ### 🐛 Describe the b...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: We encountered a bug in the LRUEvictor implementation when running VLLM (version 0.7.3) with the --preemption-mode swap flag. The issue arises due to desynchronization between self.priority_queue and self.free_table in...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: the right block to return, just like blow After making the change, we tested it and found no problems.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
