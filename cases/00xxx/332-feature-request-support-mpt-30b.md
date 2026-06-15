# vllm-project/vllm#332: feature request: support mpt-30b

| 字段 | 值 |
| --- | --- |
| Issue | [#332](https://github.com/vllm-project/vllm/issues/332) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> feature request: support mpt-30b

### Issue 正文摘录

[MPT-30b]( https://huggingface.co/mosaicml/mpt-30b), the lastest model from Mosaic is setting benchmarks for being the current best single GPU LLM outthere. Would be really cool to see mpt-30b & mpt-30b-instruct support by vLLM

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: feature request: support mpt-30b new-model [MPT-30b]( https://huggingface.co/mosaicml/mpt-30b), the lastest model from Mosaic is setting benchmarks for being the current best single GPU LLM outthere. Would be really coo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 0b new-model [MPT-30b]( https://huggingface.co/mosaicml/mpt-30b), the lastest model from Mosaic is setting benchmarks for being the current best single GPU LLM outthere. Would be really cool to see mpt-30b & mpt-30b-ins...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: feature request: support mpt-30b new-model [MPT-30b]( https://huggingface.co/mosaicml/mpt-30b), the lastest model from Mosaic is setting benchmarks for being the current best single GPU LLM outthere. Would be really coo...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
