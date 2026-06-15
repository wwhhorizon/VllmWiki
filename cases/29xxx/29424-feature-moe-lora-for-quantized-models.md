# vllm-project/vllm#29424: [Feature]: MoE LoRA for quantized models

| 字段 | 值 |
| --- | --- |
| Issue | [#29424](https://github.com/vllm-project/vllm/issues/29424) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: MoE LoRA for quantized models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch This issue tracks and records the LoRA support status for different quantization methods in vLLM. Current Support Status Quantization Method | LoRA Support | Test Model | Notes -- | -- | -- | -- MXFP4 | ✅ | gpt-oss-20b | FP8 | ✅ | qwen3-30b-a3b-fp8 | GPTQ | ✅ | qwen3-30b-a3b-gptq-int4 | AWQ | ✅ | qwen3-30b-a3b-awq | compressed_tensors| ✅ | qwen3-30b-a3b-w4a16 | Bitsandbytes | ❌ | qwen3-30b-a3b-bnb | Offline Quantization Bitsandbytes | ❌ | qwen3-30b-a3b | Online Quantization GGUF | ❌ | qwen3-30b-a3b-gguf | ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Feature]: MoE LoRA for quantized models feature request;stale ### 🚀 The feature, motivation and pitch This issue tracks and records the LoRA support status for different quantization methods in vLLM. Current Support St...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: MoE LoRA for quantized models feature request;stale ### 🚀 The feature, motivation and pitch This issue tracks and records the LoRA support status for different quantization methods in vLLM. Current Support St...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: MoE LoRA for quantized models feature request;stale ### 🚀 The feature, motivation and pitch This issue tracks and records the LoRA support status for different quantization methods in vLLM. Current Support St...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Feature]: MoE LoRA for quantized models feature request;stale ### 🚀 The feature, motivation and pitch This issue tracks and records the LoRA support status for different quantization methods in vLLM. Current Support St...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
