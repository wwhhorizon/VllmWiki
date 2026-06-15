# vllm-project/vllm#29486: [Performance]: Add optimized fused-moe kernels for low bit quantized gguf models

| 字段 | 值 |
| --- | --- |
| Issue | [#29486](https://github.com/vllm-project/vllm/issues/29486) |
| 状态 | open |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Add optimized fused-moe kernels for low bit quantized gguf models

### Issue 正文摘录

### Proposal to improve performance GGML is widely used for serving large MoE models (like Kimi-k2, Qwen3-moe, and Deepseek-v3) in memory-limited setups. The main drawback is that tools like Ollama and llama.cpp don't scale well for high-concurrency online serving. By adding optimized fused MoE kernels that support low-bit quantized GGUF models, we can significantly enhance vLLM, making it the preferred platform for serving these models. At first, we only needs to support the following formats, which are widely used by unsloth: * Q2_K * Q2_K_L * Q3_K_M * Q3_K_S I'm glad to help to support it ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Performance]: Add optimized fused-moe kernels for low bit quantized gguf models performance;stale ### Proposal to improve performance GGML is widely used for serving large MoE models (like Kimi-k2, Qwen3-moe, and Deepse...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Performance]: Add optimized fused-moe kernels for low bit quantized gguf models performance;stale ### Proposal to improve performance GGML is widely used for serving large MoE models (like Kimi-k2, Qwen3-moe, and Deeps...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: _K_M * Q3_K_S I'm glad to help to support it ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The ou...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: only needs to support the following formats, which are widely used by unsloth: * Q2_K * Q2_K_L * Q3_K_M * Q3_K_S I'm glad to help to support it ### Report of performance regression _No response_ ### Misc discussion on p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
