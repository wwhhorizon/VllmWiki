# vllm-project/vllm#4210: Performance Regression between v0.4.0 and v0.4.1

| 字段 | 值 |
| --- | --- |
| Issue | [#4210](https://github.com/vllm-project/vllm/issues/4210) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Performance Regression between v0.4.0 and v0.4.1

### Issue 正文摘录

### Anything you want to discuss about vllm. #3550 seems to reduce throughput of vLLM Before: Throughput: 20.13 requests/s, 10308.29 tokens/s After: Throughput: 17.67 requests/s, 9048.03 tokens/s (reported by @esmeetu and @youkaichao)

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: Performance Regression between v0.4.0 and v0.4.1 performance ### Anything you want to discuss about vllm. #3550 seems to reduce throughput of vLLM Before: Throughput: 20.13 requests/s, 10308.29 tokens/s After: Throughpu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: /s After: Throughput: 17.67 requests/s, 9048.03 tokens/s (reported by @esmeetu and @youkaichao)
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: lm. #3550 seems to reduce throughput of vLLM Before: Throughput: 20.13 requests/s, 10308.29 tokens/s After: Throughput: 17.67 requests/s, 9048.03 tokens/s (reported by @esmeetu and @youkaichao)

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
