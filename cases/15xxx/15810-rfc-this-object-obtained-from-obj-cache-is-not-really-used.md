# vllm-project/vllm#15810: [RFC]: this object obtained from obj cache is not really used

| 字段 | 值 |
| --- | --- |
| Issue | [#15810](https://github.com/vllm-project/vllm/issues/15810) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: this object obtained from obj cache is not really used

### Issue 正文摘录

### Motivation. weird code snippet: seq_group_metadata = self._seq_group_metadata_cache[ self.cache_id].get_object() seq_group_metadata.seq_data.clear() seq_group_metadata.block_tables.clear() later, seq_group_metadata is assigned to another new object. ### Proposed Change. remove ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: not really used RFC;stale ### Motivation. weird code snippet: seq_group_metadata = self._seq_group_metadata_cache[ self.cache_id].get_object() seq_group_metadata.seq_data.clear() seq_group_metadata.block_tables.clear()...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [RFC]: this object obtained from obj cache is not really used RFC;stale ### Motivation. weird code snippet: seq_group_metadata = self._seq_group_metadata_cache[ self.cache_id].get_object() seq_group_metadata.seq_data.cl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
