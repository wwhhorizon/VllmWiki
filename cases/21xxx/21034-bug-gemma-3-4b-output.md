# vllm-project/vllm#21034: [Bug]: gemma 3 4b output

| 字段 | 值 |
| --- | --- |
| Issue | [#21034](https://github.com/vllm-project/vllm/issues/21034) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: gemma 3 4b output

### Issue 正文摘录

### Your current environment docker vllm v0.9.2 ### 🐛 Describe the bug In v0.9.2, outputs of gemma 3 4b is wrong. But v0.9.1 work true. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: gemma 3 4b output bug ### Your current environment docker vllm v0.9.2 ### 🐛 Describe the bug In v0.9.2, outputs of gemma 3 4b is wrong. But v0.9.1 work true. ### Before submitting a new issue... - [x] Make sure y...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ue. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: gemma 3 4b output bug ### Your current environment docker vllm v0.9.2 ### 🐛 Describe the bug In v0.9.2, outputs of gemma 3 4b is wrong. But v0.9.1 work true. ### Before submitting a new issue... - [x] Make sure y...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: gemma 3 4b output bug ### Your current environment docker vllm v0.9.2 ### 🐛 Describe the bug In v0.9.2, outputs of gemma 3 4b is wrong. But v0.9.1 work true. ### Before submitting a new issue... - [x] Make sure y...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
