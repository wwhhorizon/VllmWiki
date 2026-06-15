# vllm-project/vllm#30896: [Feature]: fused GEMM +collectives helion kernel

| 字段 | 值 |
| --- | --- |
| Issue | [#30896](https://github.com/vllm-project/vllm/issues/30896) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: fused GEMM +collectives helion kernel

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Breaking down the task: - Hopper: -making sure it is running (all-gather+gemm) - integated into vLLM - add quantization support. - benchmarking - testing on other hardware. Using this: https://github.com/vllm-project/vllm/pull/29051/files ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: stale ### 🚀 The feature, motivation and pitch Breaking down the task: - Hopper: -making sure it is running (all-gather+gemm) - integated into vLLM - add quantization support. - benchmarking - testing on other hardware....
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Feature]: fused GEMM +collectives helion kernel feature request;stale ### 🚀 The feature, motivation and pitch Breaking down the task: - Hopper: -making sure it is running (all-gather+gemm) - integated into vLLM - add q...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: fused GEMM +collectives helion kernel feature request;stale ### 🚀 The feature, motivation and pitch Breaking down the task: - Hopper: -making sure it is running (all-gather+gemm) - integated into vLLM - add q...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: er+gemm) - integated into vLLM - add quantization support. - benchmarking - testing on other hardware. Using this: https://github.com/vllm-project/vllm/pull/29051/files ### Alternatives _No response_ ### Additional cont...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: sure it is running (all-gather+gemm) - integated into vLLM - add quantization support. - benchmarking - testing on other hardware. Using this: https://github.com/vllm-project/vllm/pull/29051/files ### Alternatives _No r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
