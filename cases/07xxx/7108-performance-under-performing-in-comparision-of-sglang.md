# vllm-project/vllm#7108: [Performance]: under performing in comparision of sglang

| 字段 | 值 |
| --- | --- |
| Issue | [#7108](https://github.com/vllm-project/vllm/issues/7108) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: under performing in comparision of sglang

### Issue 正文摘录

### Proposal to improve performance vLLm is under performing in comparison with sglang. There is something which need optimization for better performance. ### Report of performance regression https://lmsys.org/blog/2024-07-25-sglang-llama3/ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: port of performance regression https://lmsys.org/blog/2024-07-25-sglang-llama3/ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Performance]: under performing in comparision of sglang performance;stale ### Proposal to improve performance vLLm is under performing in comparison with sglang. There is something which need optimization for better pe...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ich need optimization for better performance. ### Report of performance regression https://lmsys.org/blog/2024-07-25-sglang-llama3/ ### Misc discussion on performance _No response_ ### Your current environment (if you t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
