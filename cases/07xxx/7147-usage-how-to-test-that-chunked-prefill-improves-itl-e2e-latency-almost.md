# vllm-project/vllm#7147: [Usage]: How to test that chunked-prefill improves ITL/e2e latency almost 2X improvement at high QPS?

| 字段 | 值 |
| --- | --- |
| Issue | [#7147](https://github.com/vllm-project/vllm/issues/7147) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to test that chunked-prefill improves ITL/e2e latency almost 2X improvement at high QPS?

### Issue 正文摘录

### Your current environment ```text The performance of chunked-prefill. ``` ### How would you like to use vllm I saw that chunked-prefill improves ITL/e2e latency almost 2X improvement at high QPS from https://github.com/vllm-project/vllm/issues/3130. But in vllm-0.5.3 and two A100, I only almost improves 10~20%. Please tell me more test information, such as server-launch instruct 、client-request instruct、GPU setting el.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: How to test that chunked-prefill improves ITL/e2e latency almost 2X improvement at high QPS? usage;stale ### Your current environment ```text The performance of chunked-prefill. ``` ### How would you like to us...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Usage]: How to test that chunked-prefill improves ITL/e2e latency almost 2X improvement at high QPS? usage;stale ### Your current environment ```text The performance of chunked-prefill. ``` ### How would you like to us...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ps://github.com/vllm-project/vllm/issues/3130. But in vllm-0.5.3 and two A100, I only almost improves 10~20%. Please tell me more test information, such as server-launch instruct 、client-request instruct、GPU setting el.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: and two A100, I only almost improves 10~20%. Please tell me more test information, such as server-launch instruct 、client-request instruct、GPU setting el.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
