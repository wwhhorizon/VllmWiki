# vllm-project/vllm#29992: [Bug]: vLLM cold start on MOE models not optimal

| 字段 | 值 |
| --- | --- |
| Issue | [#29992](https://github.com/vllm-project/vllm/issues/29992) |
| 状态 | closed |
| 标签 | bug;torch.compile;startup-ux |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM cold start on MOE models not optimal

### Issue 正文摘录

### Your current environment main ### 🐛 Describe the bug Previously, for dense models, with FX graph splitting, vLLM produces 3 unique graphs. (the model is split at the attention operator). The graph split ends up producing ~50 graphs, and we only needed to compile 3 unique graphs out of the 50. Looking at a tlparse for llama4 maverick, which is an MOE model: - every other layer has a MOE (instead of an nn.Linear feedforward) - this means there should be at most cc @ProExpertProg Also, this potentially has implications for switching to inductor graph partition. Depending on what model we were actually benchmarking (I hope we were benchmarking a dense model?) the compile time speedup/slowdown number might change after this. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: vLLM cold start on MOE models not optimal bug;torch.compile;startup-ux ### Your current environment main ### 🐛 Describe the bug Previously, for dense models, with FX graph splitting, vLLM produces 3 unique graphs...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: vLLM cold start on MOE models not optimal bug;torch.compile;startup-ux ### Your current environment main ### 🐛 Describe the bug Previously, for dense models, with FX graph splitting, vLLM produces 3 unique graphs...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: vLLM cold start on MOE models not optimal bug;torch.compile;startup-ux ### Your current environment main ### 🐛 Describe the bug Previously, for dense models, with FX graph splitting, vLLM produces 3 unique graphs...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ng to inductor graph partition. Depending on what model we were actually benchmarking (I hope we were benchmarking a dense model?) the compile time speedup/slowdown number might change after this. ### Before submitting...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: is. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
