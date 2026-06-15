# vllm-project/vllm#23529: [Usage]: DP Support in Fully SPMD Execution for Offline Inference

| 字段 | 值 |
| --- | --- |
| Issue | [#23529](https://github.com/vllm-project/vllm/issues/23529) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: DP Support in Fully SPMD Execution for Offline Inference

### Issue 正文摘录

### How would you like to use vllm I want to use DP in Fully SPMD Execution for Offline Inference. Does test_torchrun_example.py currently support DP? related code: https://github.com/vllm-project/vllm/blob/main/tests/distributed/test_torchrun_example.py#L29 related RFC: https://github.com/vllm-project/vllm/issues/11400 related issue: https://github.com/volcengine/verl/issues/3190 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 190 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: DP Support in Fully SPMD Execution for Offline Inference usage;stale ### How would you like to use vllm I want to use DP in Fully SPMD Execution for Offline Inference. Does test_torchrun_example.py currently su...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: lm I want to use DP in Fully SPMD Execution for Offline Inference. Does test_torchrun_example.py currently support DP? related code: https://github.com/vllm-project/vllm/blob/main/tests/distributed/test_torchrun_example...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
