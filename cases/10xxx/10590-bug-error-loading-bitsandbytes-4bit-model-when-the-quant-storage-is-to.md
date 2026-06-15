# vllm-project/vllm#10590: [Bug]: Error loading bitsandbytes 4bit model when the quant_storage is torch.bfloat16

| 字段 | 值 |
| --- | --- |
| Issue | [#10590](https://github.com/vllm-project/vllm/issues/10590) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Error loading bitsandbytes 4bit model when the quant_storage is torch.bfloat16

### Issue 正文摘录

## Error loading bitsandbytes 4bit model when the quant_storage is torch.bfloat16 To reproduce: ```python load a llama2-7b load_in_4bit = True, bnb_4bit_quant_storage = torch.bfloat16 with lora after training, do merge_and_unload save_pretrained now load the model using VLLM causes error: assert the param_data.shape == loaded_weight.shape ```

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Error loading bitsandbytes 4bit model when the quant_storage is torch.bfloat16 bug;stale ## Error loading bitsandbytes 4bit model when the quant_storage is torch.bfloat16 To reproduce: ```python load a llama2-7b...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Error loading bitsandbytes 4bit model when the quant_storage is torch.bfloat16 bug;stale ## Error loading bitsandbytes 4bit model when the quant_storage is torch.bfloat16 To reproduce: ```python load a llama2-7b...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ing bitsandbytes 4bit model when the quant_storage is torch.bfloat16 To reproduce: ```python load a llama2-7b load_in_4bit = True, bnb_4bit_quant_storage = torch.bfloat16 with lora after training, do merge_and_unload sa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ing bitsandbytes 4bit model when the quant_storage is torch.bfloat16 bug;stale ## Error loading bitsandbytes 4bit model when the quant_storage is torch.bfloat16 To reproduce: ```python load a llama2-7b load_in_4bit = Tr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
