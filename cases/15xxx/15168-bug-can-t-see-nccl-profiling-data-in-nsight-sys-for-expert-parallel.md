# vllm-project/vllm#15168: [Bug]: Can't see NCCL profiling data in nsight sys for expert parallel

| 字段 | 值 |
| --- | --- |
| Issue | [#15168](https://github.com/vllm-project/vllm/issues/15168) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Can't see NCCL profiling data in nsight sys for expert parallel

### Issue 正文摘录

### Your current environment I am curious why I can't see NCCL run with the EP in deepseekV3 MoE in vLLM 0.8.0, is a common issue or just my issue? ### 🐛 Describe the bug I am curious why I can't see NCCL run with the EP in deepseekV3 MoE in vLLM 0.8.0, is a common issue or just my issue? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: Can't see NCCL profiling data in nsight sys for expert parallel bug;stale ### Your current environment I am curious why I can't see NCCL run with the EP in deepseekV3 MoE in vLLM 0.8.0, is a common issue or just...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Can't see NCCL profiling data in nsight sys for expert parallel bug;stale ### Your current environment I am curious why I can't see NCCL run with the EP in deepseekV3 MoE in vLLM 0.8.0, is a common issue or just...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ue? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ug]: Can't see NCCL profiling data in nsight sys for expert parallel bug;stale ### Your current environment I am curious why I can't see NCCL run with the EP in deepseekV3 MoE in vLLM 0.8.0, is a common issue or just my...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
