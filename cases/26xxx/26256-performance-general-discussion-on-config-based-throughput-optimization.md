# vllm-project/vllm#26256: [Performance]: General Discussion on Config-based Throughput Optimization in Server Mode

| 字段 | 值 |
| --- | --- |
| Issue | [#26256](https://github.com/vllm-project/vllm/issues/26256) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: General Discussion on Config-based Throughput Optimization in Server Mode

### Issue 正文摘录

### Proposal to improve performance Under the server mode `vllm serve`, there are cases where the requests "stream" into the server. For example, there can be 1 request arriving at vllm per second, while vllm takes 10 seconds to produce the answer if this is the only request. However, as vllm server waits for the request stream to form a batched inference, it usually does nothing until the stream stops. Is there anything we can tune in the `vllm serve` command to optimize this? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Performance]: General Discussion on Config-based Throughput Optimization in Server Mode performance;stale ### Proposal to improve performance Under the server mode `vllm serve`, there are cases where the requests "stre...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ssion on Config-based Throughput Optimization in Server Mode performance;stale ### Proposal to improve performance Under the server mode `vllm serve`, there are cases where the requests "stream" into the server. For exa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Performance]: General Discussion on Config-based Throughput Optimization in Server Mode performance;stale ### Proposal to improve performance Under the server mode `vllm serve`, there are cases where the requests "stre...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
