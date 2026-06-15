# vllm-project/vllm#10697: [Usage]:  4 Bit Finetuned Mistral Model 

| 字段 | 值 |
| --- | --- |
| Issue | [#10697](https://github.com/vllm-project/vllm/issues/10697) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:  4 Bit Finetuned Mistral Model 

### Issue 正文摘录

### Your current environment I have finetuned the Mistral 0.3 7B 4bit model using unsloth and deployed in vllm Issue is the result from unsloth Inference is not completely matching vllm result. Is there any any additional parameters in vllm to replicate the results. ### How would you like to use vllm Command used to deploy in vllm: vllm serve final_model_mistral_4bit_merged16_new --gpu-memory-utilization 0.9 --max-model-len 10240 --quantization "bitsandbytes" --load-format "bitsandbytes" --chat_template /vllm/examples/template_alpaca.jinja ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: 4 Bit Finetuned Mistral Model usage;stale ### Your current environment I have finetuned the Mistral 0.3 7B 4bit model using unsloth and deployed in vllm Issue is the result from unsloth Inference is not complet...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: _4bit_merged16_new --gpu-memory-utilization 0.9 --max-model-len 10240 --quantization "bitsandbytes" --load-format "bitsandbytes" --chat_template /vllm/examples/template_alpaca.jinja ### Before submitting a new issue......
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ja ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ent environment I have finetuned the Mistral 0.3 7B 4bit model using unsloth and deployed in vllm Issue is the result from unsloth Inference is not completely matching vllm result. Is there any any additional parameters...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: 4 Bit Finetuned Mistral Model usage;stale ### Your current environment I have finetuned the Mistral 0.3 7B 4bit model using unsloth and deployed in vllm Issue is the result from unsloth Inference is not complet...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
