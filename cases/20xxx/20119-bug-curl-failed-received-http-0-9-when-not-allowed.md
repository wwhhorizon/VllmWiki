# vllm-project/vllm#20119: [Bug]: Curl failed: Received HTTP/0.9 when not allowed

| 字段 | 值 |
| --- | --- |
| Issue | [#20119](https://github.com/vllm-project/vllm/issues/20119) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Curl failed: Received HTTP/0.9 when not allowed

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Issue Description:** In a data-parallel scenario, when the --data-parallel-rpc-port argument value conflicts with the vLLM HTTP service port, the service starts without any error logs despite the port collision. **Actual Behavior:** When clients send requests, they only receive the error message: "Received HTTP/0.9 when not allowed". **Expected Behavior:** The vLLM service should either: Detect the port conflict during startup and fail with a clear error message, or Dynamically handle the conflict by selecting an alternative port. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Curl failed: Received HTTP/0.9 when not allowed bug;stale ### Your current environment ### 🐛 Describe the bug **Issue Description:** In a data-parallel scenario, when the --data-parallel-rpc-port argument value c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rt. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
