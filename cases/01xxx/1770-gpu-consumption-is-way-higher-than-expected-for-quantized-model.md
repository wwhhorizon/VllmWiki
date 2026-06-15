# vllm-project/vllm#1770: GPU consumption is way higher than expected for quantized model

| 字段 | 值 |
| --- | --- |
| Issue | [#1770](https://github.com/vllm-project/vllm/issues/1770) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> GPU consumption is way higher than expected for quantized model

### Issue 正文摘录

Hi Team, Python 3.10.x vLLM 0.2.2 autoawq 0.1.7 Firstly thanks for the blazing speed tool for LLM's. I have explored Llama2-7b-chat-hf, by using autoawq and created 4bit quantized model. Which is of around 3.6GB, but the GPU usage on T4 is way higher around 19GB. is there any configurations do i need to further setup. Following is my Langchain vLLM class instance ``` VLLM( model=model, callback_manager=callback_manager, ) ``` where model is the quantized model folder path. > attaching the GPU consumption ![image](https://github.com/vllm-project/vllm/assets/23114153/8d997627-caa1-4c30-ae73-e1013c23fe22) python3 is the only process running fastapi application which consumes the vLLM quantized Llama2-7b please share your suggestions

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: GPU consumption is way higher than expected for quantized model Hi Team, Python 3.10.x vLLM 0.2.2 autoawq 0.1.7 Firstly thanks for the blazing speed tool for LLM's. I have explored Llama2-7b-chat-hf, by using autoawq an...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: GPU consumption is way higher than expected for quantized model Hi Team, Python 3.10.x vLLM 0.2.2 autoawq 0.1.7 Firstly thanks for the blazing speed tool for LLM's. I have explored Llama2-7b-chat-hf, by using autoawq an...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
