# vllm-project/vllm#3581: [Performance]: Poor performance of vllm on AWQ

| 字段 | 值 |
| --- | --- |
| Issue | [#3581](https://github.com/vllm-project/vllm/issues/3581) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Poor performance of vllm on AWQ

### Issue 正文摘录

### Proposal to improve performance https://github.com/InternLM/lmdeploy/tree/main This project is twice faster than vllm with AWQ int4 ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) _No response_

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ernLM/lmdeploy/tree/main This project is twice faster than vllm with AWQ int4 ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you thin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Performance]: Poor performance of vllm on AWQ performance;stale ### Proposal to improve performance https://github.com/InternLM/lmdeploy/tree/main This project is twice faster than vllm with AWQ int4 ### Report of perf...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: oject is twice faster than vllm with AWQ int4 ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) _No response_

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
