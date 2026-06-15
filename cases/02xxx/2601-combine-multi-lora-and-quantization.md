# vllm-project/vllm#2601: Combine multi-LoRA and quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#2601](https://github.com/vllm-project/vllm/issues/2601) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Combine multi-LoRA and quantization

### Issue 正文摘录

There is no fundamental reason why multi-LoRA cannot work with quantized models. We will most likely want to keep LoRA's unquantized and dequantize the base model output before applying LoRAs with punica kernels. That seems to be the pattern present in other projects too. _Originally posted by @Yard1 in https://github.com/vllm-project/vllm/issues/1804#issuecomment-1872638416_

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: Combine multi-LoRA and quantization stale There is no fundamental reason why multi-LoRA cannot work with quantized models. We will most likely want to keep LoRA's unquantized and dequantize the base model output before...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: There is no fundamental reason why multi-LoRA cannot work with quantized models. We will most likely want to keep LoRA's unquantized and dequantize the base model output before applying LoRAs with punica kernels. That s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Combine multi-LoRA and quantization stale There is no fundamental reason why multi-LoRA cannot work with quantized models. We will most likely want to keep LoRA's unquantized and dequantize the base model output before...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
