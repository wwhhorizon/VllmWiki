# vllm-project/vllm#1584: ValueError: Double free! PhysicalTokenBlock(device=Device.GPU, block_number=1859, ref_count=0) is already freed.

| 字段 | 值 |
| --- | --- |
| Issue | [#1584](https://github.com/vllm-project/vllm/issues/1584) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> ValueError: Double free! PhysicalTokenBlock(device=Device.GPU, block_number=1859, ref_count=0) is already freed.

### Issue 正文摘录

Using Beam Search this Error can occur, if it is a large prompt. Workaround: in VLLM Core block_manager.py I returned 0 instead of the exception and beam search works: ` def free(self, block: PhysicalTokenBlock) -> None: if block.ref_count == 0: return 0 raise ValueError(f"Double free! {block} is already freed.") block.ref_count -= 1 if block.ref_count == 0: self.free_blocks.append(block)`

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: vice.GPU, block_number=1859, ref_count=0) is already freed. Using Beam Search this Error can occur, if it is a large prompt. Workaround: in VLLM Core block_manager.py I returned 0 instead of the exception and beam searc...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ValueError: Double free! PhysicalTokenBlock(device=Device.GPU, block_number=1859, ref_count=0) is already freed. Using Beam Search this Error can occur, if it is a large prompt. Workaround: in VLLM Core block_manager.py...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
