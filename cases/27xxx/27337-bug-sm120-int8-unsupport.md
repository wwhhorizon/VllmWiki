# vllm-project/vllm#27337: [Bug]: SM120 int8 unsupport

| 字段 | 值 |
| --- | --- |
| Issue | [#27337](https://github.com/vllm-project/vllm/issues/27337) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: SM120 int8 unsupport

### Issue 正文摘录

### My environment * rtx-5090 * cuda-12.8 ### 🐛 Describe the bug Int8_gemm unsupported ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: SM120 int8 unsupport bug;stale ### My environment * rtx-5090 * cuda-12.8 ### 🐛 Describe the bug Int8_gemm unsupported ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues,
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: # My environment * rtx-5090 * cuda-12.8 ### 🐛 Describe the bug Int8_gemm unsupported ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bot...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: SM120 int8 unsupport bug;stale ### My environment * rtx-5090 * cuda-12.8 ### 🐛 Describe the bug Int8_gemm unsupported ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
