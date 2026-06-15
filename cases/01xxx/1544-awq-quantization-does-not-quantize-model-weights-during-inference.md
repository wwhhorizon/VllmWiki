# vllm-project/vllm#1544: AWQ quantization does not quantize model weights during inference

| 字段 | 值 |
| --- | --- |
| Issue | [#1544](https://github.com/vllm-project/vllm/issues/1544) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> AWQ quantization does not quantize model weights during inference

### Issue 正文摘录

I am trying to use the AWQ quantization to load a quantized model. However, during inference time, the model weight is still mapped to float16 and int32. In `./vllm/engine/arg_utils.py`, we cannot set the `dtype` to int4. And in `awq.py`, `get_supported_act_dtypes() `only supports `torch.half`. Any plan to fix this issue?

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: AWQ quantization does not quantize model weights during inference I am trying to use the AWQ quantization to load a quantized model. However, during inference time, the model weight is still mapped to float16 and int32....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: AWQ quantization does not quantize model weights during inference I am trying to use the AWQ quantization to load a quantized model. However, during inference time, the model weight is still mapped to float16 and int32....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
