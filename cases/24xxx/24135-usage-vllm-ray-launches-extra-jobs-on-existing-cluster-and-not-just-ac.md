# vllm-project/vllm#24135: [Usage]: vllm+ray launches extra jobs on existing cluster, and not just actors

| 字段 | 值 |
| --- | --- |
| Issue | [#24135](https://github.com/vllm-project/vllm/issues/24135) |
| 状态 | open |
| 标签 | usage;ray;unstale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: vllm+ray launches extra jobs on existing cluster, and not just actors

### Issue 正文摘录

### Your current environment Trinity-RFT ### How would you like to use vllm I ran Trinity-RFT with vllm/ray and surprisingly found that vllm launches secondary Ray jobs, not just secondary actors OP: - https://github.com/modelscope/Trinity-RFT/issues/237 Is it expected? What is the reasoning behind this choice? Thanks! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ks! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: secondary Ray jobs, not just secondary actors OP: - https://github.com/modelscope/Trinity-RFT/issues/237 Is it expected? What is the reasoning behind this choice? Thanks! ### Before submitting a new issue... - [x] Make...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: launches extra jobs on existing cluster, and not just actors usage;ray;unstale ### Your current environment Trinity-RFT ### How would you like to use vllm I ran Trinity-RFT with vllm/ray and surprisingly found that vllm...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
