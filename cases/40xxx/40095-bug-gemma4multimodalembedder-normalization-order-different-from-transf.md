# vllm-project/vllm#40095: [Bug]: Gemma4MultimodalEmbedder normalization order different from Transformers, causing bad audio inference

| 字段 | 值 |
| --- | --- |
| Issue | [#40095](https://github.com/vllm-project/vllm/issues/40095) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Gemma4MultimodalEmbedder normalization order different from Transformers, causing bad audio inference

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Gemma4MultimodalEmbedder in gemma4_mm.py has different normalization order from the implementation in Transformers. In vllm, the order is: Linear → RMSNorm(text_dim) In transformers, the order is RMSNorm(multimodal_dim) → Linear This caused regression of ASR accuracy in a short audio clip, generating hallucinations. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ransformers, the order is RMSNorm(multimodal_dim) → Linear This caused regression of ASR accuracy in a short audio clip, generating hallucinations. ### Before submitting a new issue... - [x] Make sure you already search...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Gemma4MultimodalEmbedder normalization order different from Transformers, causing bad audio inference bug ### Your current environment ### 🐛 Describe the bug Gemma4MultimodalEmbedder in gemma4_mm.py has different...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: rder is RMSNorm(multimodal_dim) → Linear This caused regression of ASR accuracy in a short audio clip, generating hallucinations. ### Before submitting a new issue... - [x] Make sure you already searched for relevant is...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: caused regression of ASR accuracy in a short audio clip, generating hallucinations. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bott...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
