# vllm-project/vllm#7941: [Bug]: def _schedule_running(...) the seqs num of budget not updated

| 字段 | 值 |
| --- | --- |
| Issue | [#7941](https://github.com/vllm-project/vllm/issues/7941) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: def _schedule_running(...) the seqs num of budget not updated

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug def _schedule_running(...): while running_queue: 。。。 while not self._can_append_slots(seq_group): budget.subtract_num_batched_tokens(seq_group.request_id, num_running_tokens) num_running_seqs = seq_group.get_max_num_running_seqs() budget.subtract_num_seqs(seq_group.request_id, num_running_seqs) ... else: ... budget.add_num_batched_tokens(seq_group.request_id, num_running_tokens) ... In the above code，if “not self._can_append_slots(seq_group)” is True，the tokens num of budget will be updated in else branch,it is right(because seqs had been updated in _schedule_default). but if “not self._can_append_slots(seq_group)” is False, budget will subtract tokens and seqs num of current seq_group（now budget has no trace of seq_group）, In the next while loop, when _can_append_slots is True, else branch just update tokens of seq_group, Is seqs of budget missing? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: def _schedule_running(...) the seqs num of budget not updated bug;stale ### Your current environment ### 🐛 Describe the bug def _schedule_running(...): while running_queue: 。。。 while not self._can_append_slots(se...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: unning_queue: 。。。 while not self._can_append_slots(seq_group): budget.subtract_num_batched_tokens(seq_group.request_id, num_running_tokens) num_running_seqs = seq_group.get_max
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ng? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
