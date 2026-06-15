# vllm-project/vllm#40307: [Usage]: Using the Qwen3_5MoeForConditionalGeneration architecture of Qwen3.5-35B-A3B to train the LoRA model, but the training parameters fail to load consistently

| 字段 | 值 |
| --- | --- |
| Issue | [#40307](https://github.com/vllm-project/vllm/issues/40307) |
| 状态 | open |
| 标签 | usage |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Using the Qwen3_5MoeForConditionalGeneration architecture of Qwen3.5-35B-A3B to train the LoRA model, but the training parameters fail to load consistently

### Issue 正文摘录

### Your current environment I can load the LoRA normally using Hugging Face's generate function with expected results. However, when using vLLM for fine-tuning, it has no effect at all, and there are no error logs either. It only indicates that the visual layers were not loaded. ### How would you like to use vllm I use vllm0.19.0 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Using the Qwen3_5MoeForConditionalGeneration architecture of Qwen3.5-35B-A3B to train the LoRA model, but the training parameters fail to load consistently usage ### Your current environment I can load the LoRA...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Usage]: Using the Qwen3_5MoeForConditionalGeneration architecture of Qwen3.5-35B-A3B to train the LoRA model, but the training parameters fail to load consistently usage ### Your current environment I can load the LoRA...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Usage]: Using the Qwen3_5MoeForConditionalGeneration architecture of Qwen3.5-35B-A3B to train the LoRA model, but the training parameters fail to load consistently usage ### Your current environment I can load the LoRA...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
