# vllm-project/vllm#29739: [Feature]: GGUF model with architecture qwen3vlmoe is not supported yet.

| 字段 | 值 |
| --- | --- |
| Issue | [#29739](https://github.com/vllm-project/vllm/issues/29739) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: GGUF model with architecture qwen3vlmoe is not supported yet.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch GGUF model with architecture qwen3vlmoe is not supported yet. ### Alternatives https://github.com/vllm-project/vllm/discussions/8341 ### Additional context File "/usr/local/lib/python3.12/dist-packages/transformers/modeling_gguf_pytorch_utils.py", line 431, in load_gguf_checkpoint https://huggingface.co/unsloth/Qwen3-VL-8B-Thinking-1M-GGUF ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: GGUF model with architecture qwen3vlmoe is not supported yet. feature request ### 🚀 The feature, motivation and pitch GGUF model with architecture qwen3vlmoe is not supported yet. ### Alternatives https://git...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Feature]: GGUF model with architecture qwen3vlmoe is not supported yet. feature request ### 🚀 The feature, motivation and pitch GGUF model with architecture qwen3vlmoe is not supported yet. ### Alternatives https://git...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ch_utils.py", line 431, in load_gguf_checkpoint https://huggingface.co/unsloth/Qwen3-VL-8B-Thinking-1M-GGUF ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the ch...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Feature]: GGUF model with architecture qwen3vlmoe is not supported yet. feature request ### 🚀 The feature, motivation and pitch GGUF model with architecture qwen3vlmoe is not supported yet. ### Alternatives https://git...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ]: GGUF model with architecture qwen3vlmoe is not supported yet. feature request ### 🚀 The feature, motivation and pitch GGUF model with architecture qwen3vlmoe is not supported yet. ### Alternatives https://github.com/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
