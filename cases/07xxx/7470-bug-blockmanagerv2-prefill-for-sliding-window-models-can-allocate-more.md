# vllm-project/vllm#7470: [Bug] [BlockManagerV2]: Prefill for sliding window models can allocate more blocks than sliding window size

| 字段 | 值 |
| --- | --- |
| Issue | [#7470](https://github.com/vllm-project/vllm/issues/7470) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] [BlockManagerV2]: Prefill for sliding window models can allocate more blocks than sliding window size

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi there, I'm new to vllm and I may have missed something, but in BlockManagerV2, I only see consideration of the sliding window in the can_allocate function, like the following code snippet: ``` def can_allocate(self, seq_group: SequenceGroup) -> AllocStatus: # other code ... if self.max_block_sliding_window is not None: num_required_blocks = min(num_required_blocks, self.max_block_sliding_window) # other code ... ``` But I don't see any consideration of the sliding window when actually performing the allocation. Is this by design or a potential bug? If it's by design, I'm wondering about a scenario where the entire prompt requires 4 blocks, but the number of free blocks is only 3. In this case, if max_block_sliding_window=3, the can_allocate function would return True, but when it comes to the actual allocation, there wouldn't be enough space for the tokens in the 4th block. Is this a known issue or something that is handled differently? Any help would be greatly appreciated! 😊

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug] [BlockManagerV2]: Prefill for sliding window models can allocate more blocks than sliding window size bug;stale ### Your current environment ### 🐛 Describe the bug Hi there, I'm new to vllm and I may have missed s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: r something that is handled differently? Any help would be greatly appreciated! 😊
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug] [BlockManagerV2]: Prefill for sliding window models can allocate more blocks than sliding window size bug;stale ### Your current environment ### 🐛 Describe the bug Hi there, I'm new to vllm and I may have missed s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug] [BlockManagerV2]: Prefill for sliding window models can allocate more blocks than sliding window size bug;stale ### Your current environment ### 🐛 Describe the bug Hi there, I'm new to vllm and I may have missed s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
