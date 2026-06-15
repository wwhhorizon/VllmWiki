# vllm-project/vllm#2057: Tip: After upgrading NVIDIA driver to 536, inference performance drop down 28%

| 字段 | 值 |
| --- | --- |
| Issue | [#2057](https://github.com/vllm-project/vllm/issues/2057) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Tip: After upgrading NVIDIA driver to 536, inference performance drop down 28%

### Issue 正文摘录

I use vllm in WSL2, and after upgrade NVIDIA driver, benchmarks drop down. before: Total time: 774.99 s Throughput: 1.03 requests/s Average latency: 334.06 s Average latency per token: 1.32 s Average latency per output token: 7.88 s After: Total time: 1079.68 s Throughput: 0.74 requests/s Average latency: 507.70 s Average latency per token: 2.05 s Average latency per output token: 12.27 s more info: https://github.com/vllm-project/vllm/issues/1935

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: mance drop down 28% I use vllm in WSL2, and after upgrade NVIDIA driver, benchmarks drop down. before: Total time: 774.99 s Throughput: 1.03 requests/s Average latency: 334.06 s Average latency per token: 1.32 s Average...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ver, benchmarks drop down. before: Total time: 774.99 s Throughput: 1.03 requests/s Average latency: 334.06 s Average latency per token: 1.32 s Average latency per output token: 7.88 s After: Total time: 1079.68 s Throu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
