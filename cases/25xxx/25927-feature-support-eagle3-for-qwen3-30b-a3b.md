# vllm-project/vllm#25927: [Feature]: Support EAGLE3 for Qwen3-30B-A3B

| 字段 | 值 |
| --- | --- |
| Issue | [#25927](https://github.com/vllm-project/vllm/issues/25927) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support EAGLE3 for Qwen3-30B-A3B

### Issue 正文摘录

### 🚀 The feature, motivation and pitch As far as I know, there's no support for Qwen3 MoE model. When I tried to load trained draft model via Specforge, below error returns. ```RuntimeError: Model does not support EAGLE3 interface but aux_hidden_state_outputs was requested``` Simiar issue : https://github.com/vllm-project/vllm/issues/25134 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Support EAGLE3 for Qwen3-30B-A3B feature request;stale ### 🚀 The feature, motivation and pitch As far as I know, there's no support for Qwen3 MoE model. When I tried to load trained draft model via Specforge,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Support EAGLE3 for Qwen3-30B-A3B feature request;stale ### 🚀 The feature, motivation and pitch As far as I know, there's no support for Qwen3 MoE model. When I tried to load trained draft model via Specforge,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: re, motivation and pitch As far as I know, there's no support for Qwen3 MoE model. When I tried to load trained draft model via Specforge, below error returns. ```RuntimeError: Model does not support EAGLE3 interface bu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
