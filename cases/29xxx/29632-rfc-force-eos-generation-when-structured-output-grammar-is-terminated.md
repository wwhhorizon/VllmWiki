# vllm-project/vllm#29632: [RFC]: Force EOS generation when Structured Output Grammar is terminated

| 字段 | 值 |
| --- | --- |
| Issue | [#29632](https://github.com/vllm-project/vllm/issues/29632) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Force EOS generation when Structured Output Grammar is terminated

### Issue 正文摘录

### Motivation. In the current V1 implementation of structured outputs, when a grammar is fully satisfied (i.e., `grammar.is_terminated()` returns `True`), the `StructuredOutputManager` [releases all constraints by filling the bitmask with `_full_mask` (allowing all tokens)](https://github.com/vllm-project/vllm/blob/35657bcd7a5fd7a7af1aa1b19d78eb8973ec79c1/vllm/v1/structured_output/__init__.py#L160-L172). This behavior can be problematic if the model does not immediately predict an EOS token after completing the structured output. In such cases, the model continues to generate unstructured text (hallucinations or repetitions) until it hits `max_tokens` or a stop string. This wastes compute and requires users to manually manage stop strings for every grammar. ### Proposed Change. I propose modifying `_fill_bitmasks` in __init__.py. When `apply_bitmask` is True and the grammar is terminated, we should explicitly mask out all tokens *except* the EOS token(s). This forces the model to stop immediately after satisfying the grammar constraints. I have prototyped a fix that modifies `_fill_bitmasks` to handle the termination state explicitly: ```python def _fill_bitmasks( self, batch: li...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ter the structure is complete. This is often unreliable, especially with smaller models or complex schemas. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the ch...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: . In such cases, the model continues to generate unstructured text (hallucinations or repetitions) until it hits `max_tokens` or a stop string. This wastes compute and requires users to manually manage stop strings for...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: grammar.fill_bitmask(self._grammar_bitmask, index) else: # Grammar is terminated: Force EOS generation self._grammar_bitmask[index].fill_(0) for eos_token_id in self.eos_token_ids: self._g
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: _output/__init__.py#L160-L172). This behavior can be problematic if the model does not immediately predict an EOS token after completing the structured output. In such cases, the model continues to generate unstructured...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ]: Force EOS generation when Structured Output Grammar is terminated RFC;stale ### Motivation. In the current V1 implementation of structured outputs, when a grammar is fully satisfied (i.e., `grammar.is_terminated()` r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
