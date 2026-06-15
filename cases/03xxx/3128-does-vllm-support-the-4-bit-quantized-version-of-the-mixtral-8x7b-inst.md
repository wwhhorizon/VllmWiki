# vllm-project/vllm#3128: Does vLLM support the 4-bit quantized version of the Mixtral-8x7B-Instruct-v0.1 model downloaded from Hugging Face

| 字段 | 值 |
| --- | --- |
| Issue | [#3128](https://github.com/vllm-project/vllm/issues/3128) |
| 状态 | closed |
| 标签 |  |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Does vLLM support the 4-bit quantized version of the Mixtral-8x7B-Instruct-v0.1 model downloaded from Hugging Face

### Issue 正文摘录

Hey guys, Does vLLM support the 4-bit quantized version of the Mixtral-8x7B-Instruct-v0.1 model downloaded from Hugging Face here https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1. According to the Hugging Face link above, we can switch over to the 4-bit version using this line of code: ``` + model = AutoModelForCausalLM.from_pretrained(model_id, load_in_4bit=True, device_map="auto") ``` This is urgent so I would really appreciate any help on this.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Does vLLM support the 4-bit quantized version of the Mixtral-8x7B-Instruct-v0.1 model downloaded from Hugging Face Hey guys, Does vLLM support the 4-bit quantized version of the Mixtral-8x7B-Instruct-v0.1 model download...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: LM support the 4-bit quantized version of the Mixtral-8x7B-Instruct-v0.1 model downloaded from Hugging Face Hey guys, Does vLLM support the 4-bit quantized version of the Mixtral-8x7B-Instruct-v0.1 model downloaded from...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: Does vLLM support the 4-bit quantized version of the Mixtral-8x7B-Instruct-v0.1 model downloaded from Hugging Face Hey guys, Does vLLM support the 4-bit quantized version of the Mixtral-8x7B-Instruct-v0.1 model download...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
