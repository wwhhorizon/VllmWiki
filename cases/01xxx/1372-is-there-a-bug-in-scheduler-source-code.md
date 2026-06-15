# vllm-project/vllm#1372: Is there a bug in Scheduler source code?

| 字段 | 值 |
| --- | --- |
| Issue | [#1372](https://github.com/vllm-project/vllm/issues/1372) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Is there a bug in Scheduler source code?

### Issue 正文摘录

**In the follow codes, while scheduler enter the branch of "while not self.block_manager.can_append_slot(seq_group):" with "self.running == True", the pre fetch seq_group will be passed in the scheduler?** # Reserve new token slots for the running sequence groups. running: List[SequenceGroup] = [] preempted: List[SequenceGroup] = [] while self.running: seq_group = self.running.pop(0) while not self.block_manager.can_append_slot(seq_group): if self.running: # Preempt the lowest-priority sequence groups. victim_seq_group = self.running.pop(-1) self._preempt(victim_seq_group, blocks_to_swap_out) preempted.append(victim_seq_group) else: # No other sequence groups can be preempted. # Preempt the current sequence group. self._preempt(seq_group, blocks_to_swap_out) preempted.append(seq_group) break else: # Append new slots to the sequence group. self._append_slot(seq_group, blocks_to_copy) running.append(seq_group) self.running = running

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: In the follow codes, while scheduler enter the branch of "while not self.block_manager.can_append_slot(seq_group):" with "self.running == True", the pre fetch seq_group will be passed in the scheduler?** # Reserve new t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Is there a bug in Scheduler source code? **In the follow codes, while scheduler enter the branch of "while not self.block_manager.can_append_slot(seq_group):" with "self.running == True", the pre fetch seq_group will be...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
