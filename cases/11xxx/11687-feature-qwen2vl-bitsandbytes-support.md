# vllm-project/vllm#11687: [Feature]:  Qwen2VL bitsandbytes support

| 字段 | 值 |
| --- | --- |
| Issue | [#11687](https://github.com/vllm-project/vllm/issues/11687) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]:  Qwen2VL bitsandbytes support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi, I tried to use unsloth/QVQ-72B-Preview-bnb-4bit but received the message Model Qwen2VLForConditionalGeneration does not support BitsAndBytes quantization yet. model= LLM(model= unsloth/QVQ-72B-Preview-bnb-4bit, gpu_memory_utilization=0.95, max_num_seqs=32, tensor_parallel_size=torch.cuda.device_count(), quantization="bitsandbytes", load_format="bitsandbytes", dtype=torch.bfloat16, enforce_eager=True, max_model_len=4096, ) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: sage Model Qwen2VLForConditionalGeneration does not support BitsAndBytes quantization yet. model= LLM(model= unsloth/QVQ-72B-Preview-bnb-4bit, gpu_memory_utilization=0.95, max_num_seqs=32, tensor_parallel_size=torch.cud...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Qwen2VL bitsandbytes support feature request ### 🚀 The feature, motivation and pitch Hi, I tried to use unsloth/QVQ-72B-Preview-bnb-4bit but received the message Model Qwen2VLForConditionalGeneration does not...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ry_utilization=0.95, max_num_seqs=32, tensor_parallel_size=torch.cuda.device_count(), quantization="bitsandbytes", load_format="bitsandbytes", dtype=torch.bfloat16, enforce_eager=True, max_model_len=4096, ) ### Alternat...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: re request ### 🚀 The feature, motivation and pitch Hi, I tried to use unsloth/QVQ-72B-Preview-bnb-4bit but received the message Model Qwen2VLForConditionalGeneration does not support BitsAndBytes quantization yet. model...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Qwen2VL bitsandbytes support feature request ### 🚀 The feature, motivation and pitch Hi, I tried to use unsloth/QVQ-72B-Preview-bnb-4bit but received the message Model Qwen2VLForConditionalGeneration does not...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
