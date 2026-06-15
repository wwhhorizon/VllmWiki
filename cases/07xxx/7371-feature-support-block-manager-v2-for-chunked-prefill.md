# vllm-project/vllm#7371: [Feature]: Support block manager v2 for chunked prefill

| 字段 | 值 |
| --- | --- |
| Issue | [#7371](https://github.com/vllm-project/vllm/issues/7371) |
| 状态 | closed |
| 标签 | help wanted;feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support block manager v2 for chunked prefill

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Chunked prefill currently doesn't work with block manager v2. Add `use_v2_block_manager=True` to https://github.com/vllm-project/vllm/blob/main/tests/basic_correctness/test_chunked_prefill.py#L48 to reproduce the error: ``` def append_token_ids(self, block_index: int, token_ids: List[int]) -> None: > block = self._blocks[block_index] E IndexError: list index out of range ``` ### Alternatives Use block manager v1 ### Additional context cc @rkooo567 @cadedaniel

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support block manager v2 for chunked prefill help wanted;feature request ### 🚀 The feature, motivation and pitch Chunked prefill currently doesn't work with block manager v2. Add `use_v2_block_manager=True` t...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ct/vllm/blob/main/tests/basic_correctness/test_chunked_prefill.py#L48 to reproduce the error: ``` def append_token_ids(self, block_index: int, token_ids: List[int]) -> None: > block = self._blocks[block_index] E IndexEr...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Feature]: Support block manager v2 for chunked prefill help wanted;feature request ### 🚀 The feature, motivation and pitch Chunked prefill currently doesn't work with block manager v2. Add `use_v2_block_manager=True` t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: v2_block_manager=True` to https://github.com/vllm-project/vllm/blob/main/tests/basic_correctness/test_chunked_prefill.py#L48 to reproduce the error: ``` def append_token_ids(self, block_index: int, token_ids: List[int])...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
