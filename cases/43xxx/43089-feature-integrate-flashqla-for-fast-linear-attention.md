# vllm-project/vllm#43089: [Feature]: Integrate FlashQLA for fast linear attention

| 字段 | 值 |
| --- | --- |
| Issue | [#43089](https://github.com/vllm-project/vllm/issues/43089) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Integrate FlashQLA for fast linear attention

### Issue 正文摘录

### 🚀 The feature, motivation and pitch https://github.com/QwenLM/FlashQLA was published by the Qwen team recently which promises a fast implementation of `chunk_gated_delta_rule` used in Qwen3.5 / Qwen3.6. It might be useful to integrate it into vllm to speedup models using linear attention. ### Alternatives Currently vllm uses either a customised version of https://github.com/fla-org/flash-linear-attention/ or https://github.com/flashinfer-ai/flashinfer for GDN. [Their benchmarks](https://github.com/QwenLM/FlashQLA#benchmark) promise to outperform these alternatives. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ture request ### 🚀 The feature, motivation and pitch https://github.com/QwenLM/FlashQLA was published by the Qwen team recently which promises a fast implementation of `chunk_gated_delta_rule` used in Qwen3.5 / Qwen3.6....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ttention/ or https://github.com/flashinfer-ai/flashinfer for GDN. [Their benchmarks](https://github.com/QwenLM/FlashQLA#benchmark) promise to outperform these alternatives. ### Additional context _No response_ ### Befor...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: https://github.com/fla-org/flash-linear-attention/ or https://github.com/flashinfer-ai/flashinfer for GDN. [Their benchmarks](https://github.com/QwenLM/FlashQLA#benchmark) promise to outperform these alternatives. ### A...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ar attention. ### Alternatives Currently vllm uses either a customised version of https://github.com/fla-org/flash-linear-attention/ or https://github.com/flashinfer-ai/flashinfer for GDN. [Their benchmarks](https://git...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
