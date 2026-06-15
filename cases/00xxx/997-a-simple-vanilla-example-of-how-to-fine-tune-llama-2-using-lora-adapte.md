# vllm-project/vllm#997: a simple vanilla example of how to fine tune Llama 2 using Lora adapters for vLLM inference 

| 字段 | 值 |
| --- | --- |
| Issue | [#997](https://github.com/vllm-project/vllm/issues/997) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> a simple vanilla example of how to fine tune Llama 2 using Lora adapters for vLLM inference 

### Issue 正文摘录

Is anybody kind enough to create a simple vanilla example of how to fine tune Llama 2 using Lora adapters such that it to be later used with vLLM for inference. There is a bit of confusion of whether or not to use quantization when loading the model for fine tuning, apparently vLLM does not work with quantized models. Also which LoraConfig "target_modules" work with vLLM? Also should the adapter be merged? A simple vanilla example would really help a lot.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: a simple vanilla example of how to fine tune Llama 2 using Lora adapters for vLLM inference Is anybody kind enough to create a simple vanilla example of how to fine tune Llama 2 using Lora adapters such that it to be la...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: vLLM for inference. There is a bit of confusion of whether or not to use quantization when loading the model for fine tuning, apparently vLLM does not work with quantized models. Also which LoraConfig "target_modules" w...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
