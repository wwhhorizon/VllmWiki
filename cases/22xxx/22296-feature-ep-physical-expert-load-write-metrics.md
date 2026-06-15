# vllm-project/vllm#22296: [Feature]:  EP physical expert load write metrics

| 字段 | 值 |
| --- | --- |
| Issue | [#22296](https://github.com/vllm-project/vllm/issues/22296) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]:  EP physical expert load write metrics

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When EP>1, it is desired to replicate the physical expert into the metrics. Compared to the logical expert, the physical expert can more clearly display the load situation of each card and can also be mapped back to the logical expert through a mapping table. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: EP physical expert load write metrics feature request;stale ### 🚀 The feature, motivation and pitch When EP>1, it is desired to replicate the physical expert into the metrics. Compared to the logical expert,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: of each card and can also be mapped back to the logical expert through a mapping table. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you alread...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Feature]: EP physical expert load write metrics feature request;stale ### 🚀 The feature, motivation and pitch When EP>1, it is desired to replicate the physical expert into the metrics. Compared to the logical expert,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
