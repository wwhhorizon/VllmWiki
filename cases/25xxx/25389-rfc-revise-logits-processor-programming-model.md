# vllm-project/vllm#25389: [RFC]: Revise Logits Processor Programming Model

| 字段 | 值 |
| --- | --- |
| Issue | [#25389](https://github.com/vllm-project/vllm/issues/25389) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Revise Logits Processor Programming Model

### Issue 正文摘录

### Motivation. The purpose of this work is to hide details of the vLLM engine implementation from logits processor implementors; currently the vLLM logits processor programming model requires the logits processor implementor to consider complex bookkeeping details about persistent batch state changes. The proposed changes decrease the amount of bookkeeping related to batch ordering which the implementor must consider, by taking advantage of upcoming changes to the vLLM model runner. This change impacts 1. How existing builtin logits processors based on `LogitsProcessor` base class (min-p, logits bias, and min tokens) are implemented 2. How new builtin logits processors would be implemented 3. How custom logits processors would be implemented There are still some logits processors hard-coded into the vLLM engine implementation - this interface change is a prerequisite for porting these hard-coded logits processors to become subclasses of `LogitsProcessor`. #### Current logits processor programming model Currently, to define a logits processor, you must subclass `vllm.v1.sample.logits_processor.LogitsProcessor` and define (at minimum) the following methods: * `__init__(self, vllm_c...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [RFC]: Revise Logits Processor Programming Model RFC;stale ### Motivation. The purpose of this work is to hide details of the vLLM engine implementation from logits processor implementors; currently the vLLM logits proc...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: hanges what is the highest-logit-value token ID for a given request), `False` if the logits processor may modify argmax * `is_argmax_invariant()` is evaluated once at startup; if `True`, vLLM will skip applying this log...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: Revise Logits Processor Programming Model RFC;stale ### Motivation. The purpose of this work is to hide details of the vLLM engine implementation from logits processor implementors; currently the vLLM logits proc...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: the logits processor may modify argmax * `is_argmax_invariant()` is evaluated once at startup; if `True`, vLLM will skip applying this logits processor in a given step when all requests use greedy sampling * `update_sta...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: logits processors in-place or out-of-place; in-place is more memory-efficient * `is_argmax_invariant(self) -> bool`: * Return `True` if the logits processor is argmax invariant (never changes what is the highest-logit-v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
