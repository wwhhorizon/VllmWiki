# vllm-project/vllm#24116: [Feature]: Optimize EPLB Rearrange Experts

| 字段 | 值 |
| --- | --- |
| Issue | [#24116](https://github.com/vllm-project/vllm/issues/24116) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Optimize EPLB Rearrange Experts

### Issue 正文摘录

### 🚀 The feature, motivation and pitch - Rearrange experts can take 15s during wide EP (EP=32) setups - This blocks the server for much too long - We need some way to improve this. Ideas include (a) making it async, (b) serializing the state, or (c) making things faster with direct optimization ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Optimize EPLB Rearrange Experts feature request;stale ### 🚀 The feature, motivation and pitch - Rearrange experts can take 15s during wide EP (EP=32) setups - This blocks the server for much too long - We nee...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: h - Rearrange experts can take 15s during wide EP (EP=32) setups - This blocks the server for much too long - We need some way to improve this. Ideas include (a) making it async, (b) serializing the state, or (c) making...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Feature]: Optimize EPLB Rearrange Experts feature request;stale ### 🚀 The feature, motivation and pitch - Rearrange experts can take 15s during wide EP (EP=32) setups - This blocks the server for much too long - We nee...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
