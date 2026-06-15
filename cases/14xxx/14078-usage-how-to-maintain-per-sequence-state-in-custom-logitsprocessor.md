# vllm-project/vllm#14078: [Usage]: How to maintain per-sequence state in custom LogitsProcessor?

| 字段 | 值 |
| --- | --- |
| Issue | [#14078](https://github.com/vllm-project/vllm/issues/14078) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to maintain per-sequence state in custom LogitsProcessor?

### Issue 正文摘录

### Your current environment ```text vllm version: 0.7.1 ``` ### How would you like to use vllm ## Problem Description When implementing a custom LogitsProcessor that requires tracking per-sequence states (e.g., detecting trigger words and modifying sampling behavior afterward), there is no reliable way to identify sequences uniquely. Current attempts to use id(token_ids) or hash(tuple(token_ids)) fail because: - token_ids is a copy of the sequence’s token history passed to the processor, and its memory address (id) changes between steps. - Hashing token lists is unreliable because different sequences may share identical prefixes. This makes it impossible to maintain stable state tracking for individual sequences. ## Code Example ```python class Processor: def __init__(self, trigger_words: str): self.trigger_tokens = tokenizer.encode(trigger_words, add_special_tokens=False) self.states = {} def __call__(self, token_ids: list, logits: torch.Tensor) -> torch.Tensor: # Attempt to use token_ids as identifier seq_id = id(token_ids) # This changes between calls # seq_id = hash(tuple(token_ids)) # Also unreliable print(seq_id, end='\t') if seq_id not in self.states: self.states[seq_id] =...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: LogitsProcessor? usage;stale ### Your current environment ```text vllm version: 0.7.1 ``` ### How would you like to use vllm ## Problem Description When implementing a custom LogitsProcessor that requires tracking per-s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ge]: How to maintain per-sequence state in custom LogitsProcessor? usage;stale ### Your current environment ```text vllm version: 0.7.1 ``` ### How would you like to use vllm ## Problem Description When implementing a c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ce? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: lf.trigger_tokens = tokenizer.encode(trigger_words, add_special_tokens=False) self.states = {} def __call__(self, token_ids: list, logits: torch.Tensor) -> torch.Tensor: # Attempt to use token_ids as identifier seq_id =...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
