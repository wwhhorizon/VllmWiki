# vllm-project/vllm#29263: [Feature]: Enable flash attention (and/or FlashMLA) for AMD GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#29263](https://github.com/vllm-project/vllm/issues/29263) |
| 状态 | closed |
| 标签 | feature request;rocm |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Enable flash attention (and/or FlashMLA) for AMD GPUs

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In [this page from flash-attention](https://github.com/Dao-AILab/flash-attention?tab=readme-ov-file#amd-rocm-support), I checked that the upstream `flash-attention` currently has composable_kernel (for newer AMD GPUs) and WIP triton (for older RNDA GPUs, etc.) implementations. As well as [flash MLA](https://github.com/deepseek-ai/FlashMLA?tab=readme-ov-file#amd-instinct). Is it possible to enable `vllm.vllm_flash_attn._vllm_fa2_C` and more modules for AMD GPUs? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Feature]: Enable flash attention (and/or FlashMLA) for AMD GPUs feature request;rocm ### 🚀 The feature, motivation and pitch In [this page from flash-attention](https://github.com/Dao-AILab/flash-attention?tab=readme-o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ]: Enable flash attention (and/or FlashMLA) for AMD GPUs feature request;rocm ### 🚀 The feature, motivation and pitch In [this page from flash-attention](https://github.com/Dao-AILab/flash-attention?tab=readme-ov-file#a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Enable flash attention (and/or FlashMLA) for AMD GPUs feature request;rocm ### 🚀 The feature, motivation and pitch In [this page from flash-attention](https://github.com/Dao-AILab/flash-attention?tab=readme-o...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
