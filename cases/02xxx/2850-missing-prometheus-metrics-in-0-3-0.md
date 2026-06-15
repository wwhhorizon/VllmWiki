# vllm-project/vllm#2850: Missing prometheus metrics in `0.3.0`

| 字段 | 值 |
| --- | --- |
| Issue | [#2850](https://github.com/vllm-project/vllm/issues/2850) |
| 状态 | closed |
| 标签 |  |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Missing prometheus metrics in `0.3.0`

### Issue 正文摘录

First of all, thanks for the great open source library! The docs promise a few more additional metrics that I'm not seeing in vLLM 0.3.0, have these been removed? I.e. if I hit `/metrics` of the OpenAI API server for a deployed model... you'll see no `vllm:time_to_first_token_seconds` or `vllm:time_per_output_token_seconds` or `vllm:e2e_request_latency_seconds`

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: emoved? I.e. if I hit `/metrics` of the OpenAI API server for a deployed model... you'll see no `vllm:time_to_first_token_seconds` or `vllm:time_per_output_token_seconds` or `vllm:e2e_request_latency_seconds`
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: irst_token_seconds` or `vllm:time_per_output_token_seconds` or `vllm:e2e_request_latency_seconds`
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: en_seconds` or `vllm:time_per_output_token_seconds` or `vllm:e2e_request_latency_seconds`

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
