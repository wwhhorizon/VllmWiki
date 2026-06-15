# vllm-project/vllm#6363: [Bug]: Combine flashinfer with chunked prefill, LLM's answers become nonsense

| 字段 | 值 |
| --- | --- |
| Issue | [#6363](https://github.com/vllm-project/vllm/issues/6363) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Combine flashinfer with chunked prefill, LLM's answers become nonsense

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug 1.flashinfer + chunked prefill outputs garbage 2.missing support of copy / swap blocks with flashinfer backend?

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Combine flashinfer with chunked prefill, LLM's answers become nonsense bug ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug 1.flashinfer + chunked prefill outp...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: infer + chunked prefill outputs garbage 2.missing support of copy / swap blocks with flashinfer backend?
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Combine flashinfer with chunked prefill, LLM's answers become nonsense bug ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug 1.flashinfer + chunked prefill outp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
