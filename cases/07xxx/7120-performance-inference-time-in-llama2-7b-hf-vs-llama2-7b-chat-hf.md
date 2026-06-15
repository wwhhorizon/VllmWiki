# vllm-project/vllm#7120: [Performance]: Inference time in Llama2-7b-hf vs. Llama2-7b-chat-hf

| 字段 | 值 |
| --- | --- |
| Issue | [#7120](https://github.com/vllm-project/vllm/issues/7120) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Inference time in Llama2-7b-hf vs. Llama2-7b-chat-hf

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression For the same query, the stats are: **Llama2-7b-hf model:** 47.52s/it, est. speed input: 4.76 toks/s, output: 42.09 toks/s **Llama2-7b-chat-hf model:** 2.20it/s, est. speed input: 496.52 toks/s, output: 30.76 toks/s What leads to such a big difference? ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Performance]: Inference time in Llama2-7b-hf vs. Llama2-7b-chat-hf performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression For the same query, the stats are: **Llama2-7b...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: mance]: Inference time in Llama2-7b-hf vs. Llama2-7b-chat-hf performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression For the same query, the stats are: **Llama2-7b-hf mod...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: roposal to improve performance _No response_ ### Report of performance regression For the same query, the stats are: **Llama2-7b-hf model:** 47.52s/it, est. speed input: 4.76 toks/s, output: 42.09 toks/s **Llama2-7b-cha...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
