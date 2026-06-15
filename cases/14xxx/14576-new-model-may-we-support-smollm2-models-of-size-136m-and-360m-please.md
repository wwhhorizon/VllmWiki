# vllm-project/vllm#14576: [New Model]: May we support smolLM2 models of size 136M and 360M please?

| 字段 | 值 |
| --- | --- |
| Issue | [#14576](https://github.com/vllm-project/vllm/issues/14576) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: May we support smolLM2 models of size 136M and 360M please?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I would love to use **vLLM** with the **SmolLM2** family of open-source compact language models (particularly the 135M and 360M-parameter variants). These smaller models are trained on large, high-quality corpora but require fewer resources at inference time compared to multi-billion-parameter models. Supporting them in vLLM would lower the barrier to entry for developers seeking lighter-weight solutions while benefiting from vLLM’s high-performance inference engine. **Key Points** - **SmolLM2** is a set of lightweight LLMs for on-device or resource-constrained environments. - Parameter sizes: **135M** (trained on 2T tokens) and **360M** (trained on 4T tokens). - Many potential users need smaller models for cost-efficient inference and memory-limited deployments. ### Alternatives ### Alternatives - Use manually converted weights for CPU-only usage or alternative inference frameworks. - Attempt partial support through existing scripts, but that may involve non-trivial modifications for GQA and RoPE handling. - Rely on bigger models, which defeats the purpose of smaller, more efficient LLMs. ### Additional context ### Additional context - The...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: May we support smolLM2 models of size 136M and 360M please? new-model ### 🚀 The feature, motivation and pitch I would love to use **vLLM** with the **SmolLM2** family of open-source compact language models...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: rs with **Grouped Query Attention (GQA)**. - Training + inference in **bfloat16**. - Ideal for on-device deployments or memory-limited servers. - Thank you for considering this enhancement! Let me know if I can provide...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [New Model]: May we support smolLM2 models of size 136M and 360M please? new-model ### 🚀 The feature, motivation and pitch I would love to use **vLLM** with the **SmolLM2** family of open-source compact language models...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: on 4T tokens). - Many potential users need smaller models for cost-efficient inference and memory-limited deployments. ### Alternatives ### Alternatives - Use manually converted weights for CPU-only usage or alternative...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: dering this enhancement! Let me know if I can provide further details or testing. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
