# vllm-project/vllm#37077: [Feature][Cleanup]: Optimize token data structures (list[int] to numpy arrays)

| 字段 | 值 |
| --- | --- |
| Issue | [#37077](https://github.com/vllm-project/vllm/issues/37077) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][Cleanup]: Optimize token data structures (list[int] to numpy arrays)

### Issue 正文摘录

### Description This issue tracks the "Data structure clean up" task mentioned in the [vLLM Roadmap Q1 2026]. As outlined by @njhill in the roadmap, the goal is to improve efficiency for data structures that grow with the number of tokens and number of requests. This involves replacing inefficient Python structures, such as `list[int]` or dictionaries, with more performant alternatives like NumPy arrays. ### Expected Changes - Identify core engine components (e.g., `Sequence`, `SequenceGroup`, scheduler data structures) using `list[int]` for token IDs or logprobs. - Refactor these to use NumPy arrays or other memory-efficient and contiguous data structures. - Remove unnecessary dictionaries where simple objects or arrays suffice. I will be helping with this effort and will use this issue to track related PRs and discussions. Any pointers on the best places to start are welcome!

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: cy for data structures that grow with the number of tokens and number of requests. This involves replacing inefficient Python structures, such as `list[int]` or dictionaries, with more performant alternatives like NumPy...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 026]. As outlined by @njhill in the roadmap, the goal is to improve efficiency for data structures that grow with the number of tokens and number of requests. This involves replacing inefficient Python structures, such...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: robs. - Refactor these to use NumPy arrays or other memory-efficient and contiguous data structures. - Remove unnecessary dictionaries where simple objects or arrays suffice. I will be helping with this effort and will...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
