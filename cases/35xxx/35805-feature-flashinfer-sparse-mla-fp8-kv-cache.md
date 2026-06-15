# vllm-project/vllm#35805: [Feature]: FlashInfer Sparse MLA + FP8 KV Cache

| 字段 | 值 |
| --- | --- |
| Issue | [#35805](https://github.com/vllm-project/vllm/issues/35805) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: FlashInfer Sparse MLA + FP8 KV Cache

### Issue 正文摘录

### 🚀 The feature, motivation and pitch [Initial support](https://github.com/vllm-project/vllm/pull/33451) only works with BF16 KV Cache ### Alternatives FlashMLA Sparse works fine and supports FP8 but perf is worse for some concurrencies ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Feature]: FlashInfer Sparse MLA + FP8 KV Cache feature request ### 🚀 The feature, motivation and pitch [Initial support](https://github.com/vllm-project/vllm/pull/33451) only works with BF16 KV Cache ### Alternatives F...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: FlashInfer Sparse MLA + FP8 KV Cache feature request ### 🚀 The feature, motivation and pitch [Initial support](https://github.com/vllm-project/vllm/pull/33451) only works with BF16 KV Cache ### Alternatives F...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: A Sparse works fine and supports FP8 but perf is worse for some concurrencies ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Feature]: FlashInfer Sparse MLA + FP8 KV Cache feature request ### 🚀 The feature, motivation and pitch [Initial support](https://github.com/vllm-project/vllm/pull/33451) only works with BF16 KV Cache ### Alternatives F...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
