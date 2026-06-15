# vllm-project/vllm#19429: [Usage]: 如何使用 vllm 进行跨模态的离线推理

| 字段 | 值 |
| --- | --- |
| Issue | [#19429](https://github.com/vllm-project/vllm/issues/19429) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: 如何使用 vllm 进行跨模态的离线推理

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm 如题，比如我微调了一个 gemma3-4b-it 。现在我希望离线推理，输入为 多轮对话（system，user，assistant都有），并且包括图片，我要怎么实现呢 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 实现呢 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: hon collect_env.py` ``` ### How would you like to use vllm 如题，比如我微调了一个 gemma3-4b-it 。现在我希望离线推理，输入为 多轮对话（system，user，assistant都有），并且包括图片，我要怎么实现呢 ### Before submitting a new issue... - [x] Make sure you already searched f...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: hon collect_env.py` ``` ### How would you like to use vllm 如题，比如我微调了一个 gemma3-4b-it 。现在我希望离线推理，输入为 多轮对话（system，user，assistant都有），并且包括图片，我要怎么实现呢 ### Before submitting a new issue... - [x] Make sure you already searched f...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
