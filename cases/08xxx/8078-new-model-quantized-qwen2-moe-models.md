# vllm-project/vllm#8078: [New Model]: quantized Qwen2 MoE models 

| 字段 | 值 |
| --- | --- |
| Issue | [#8078](https://github.com/vllm-project/vllm/issues/8078) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: quantized Qwen2 MoE models 

### Issue 正文摘录

### The model to consider. [https://huggingface.co/Agnuxo/Qwen2-1.5B-Instruct_MOE_assistant-GGUF_8bit](url) ### The closest model vllm already supports. [https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/qwen2_moe.py](url) ### What's your difficulty of supporting the model you want? _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: quantized Qwen2 MoE models new-model;stale ### The model to consider. [https://huggingface.co/Agnuxo/Qwen2-1.5B-Instruct_MOE_assistant-GGUF_8bit](url) ### The closest model vllm already supports. [https://g...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [New Model]: quantized Qwen2 MoE models new-model;stale ### The model to consider. [https://huggingface.co/Agnuxo/Qwen2-1.5B-Instruct_MOE_assistant-GGUF_8bit](url) ### The closest model vllm already supports. [https://g...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [New Model]: quantized Qwen2 MoE models new-model;stale ### The model to consider. [https://huggingface.co/Agnuxo/Qwen2-1.5B-Instruct_MOE_assistant-GGUF_8bit](url) ### The closest model vllm already supports. [https://g...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: quantized Qwen2 MoE models new-model;stale ### The model to consider. [https://huggingface.co/Agnuxo/Qwen2-1.5B-Instruct_MOE_assistant-GGUF_8bit](url) ### The closest model vllm already supports. [https://g...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
