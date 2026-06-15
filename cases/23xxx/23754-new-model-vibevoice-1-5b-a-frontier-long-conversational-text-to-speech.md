# vllm-project/vllm#23754: [New Model]: VibeVoice-1.5B : A Frontier Long Conversational Text-to-Speech Model

| 字段 | 值 |
| --- | --- |
| Issue | [#23754](https://github.com/vllm-project/vllm/issues/23754) |
| 状态 | closed |
| 标签 | new-model;stale;multi-modality |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: VibeVoice-1.5B : A Frontier Long Conversational Text-to-Speech Model

### Issue 正文摘录

### The model to consider. https://huggingface.co/microsoft/VibeVoice-1.5B https://github.com/microsoft/VibeVoice This model is an auto-regressive architecture with multimodal inputs and outputs, which leverages a diffusion head together with a VAE for processing. The design provides a general-purpose interface that unifies multimodal generation and understanding. VibeVoice has become highly popular, and many users are interested in deploying it as an API backend. If vLLM could support this model, it would be extremely valuable for the community. ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting the model you want? Transformers need to handle not only discrete text tokens, but also continuous multimodal tokens. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: VibeVoice-1.5B : A Frontier Long Conversational Text-to-Speech Model new-model;stale;multi-modality ### The model to consider. https://huggingface.co/microsoft/VibeVoice-1.5B https://github.com/microsoft/Vi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: highly popular, and many users are interested in deploying it as an API backend. If vLLM could support this model, it would be extremely valuable for the community. ### The closest model vllm already supports. _No respo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: https://github.com/microsoft/VibeVoice This model is an auto-regressive architecture with multimodal inputs and outputs, which leverages a diffusion head together with a VAE for processing. The design provides a general...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ice-1.5B : A Frontier Long Conversational Text-to-Speech Model new-model;stale;multi-modality ### The model to consider. https://huggingface.co/microsoft/VibeVoice-1.5B https://github.com/microsoft/VibeVoice This model...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
