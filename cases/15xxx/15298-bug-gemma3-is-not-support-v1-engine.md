# vllm-project/vllm#15298: [Bug]: Gemma3 is not support V1 Engine

| 字段 | 值 |
| --- | --- |
| Issue | [#15298](https://github.com/vllm-project/vllm/issues/15298) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Gemma3 is not support V1 Engine

### Issue 正文摘录

### Your current environment I put together a build from main on 03/20/2025. ### 🐛 Describe the bug Can you make V1 Engine support for Gemma3? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: not support V1 Engine bug ### Your current environment I put together a build from main on 03/20/2025. ### 🐛 Describe the bug Can you make V1 Engine support for Gemma3? ### Before submitting a new issue... - [x] Make su...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: a3? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Gemma3 is not support V1 Engine bug ### Your current environment I put together a build from main on 03/20/2025. ### 🐛 Describe the bug Can you make V1 Engine support for Gemma3? ### Before submitting a new issue...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: Gemma3 is not support V1 Engine bug ### Your current environment I put together a build from main on 03/20/2025. ### 🐛 Describe the bug Can you make V1 Engine support for Gemma3? ### Before submitting a new issue...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
