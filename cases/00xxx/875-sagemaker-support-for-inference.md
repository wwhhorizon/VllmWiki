# vllm-project/vllm#875: Sagemaker support for inference

| 字段 | 值 |
| --- | --- |
| Issue | [#875](https://github.com/vllm-project/vllm/issues/875) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Sagemaker support for inference

### Issue 正文摘录

Hi, I am trying to test the throughout using vLLMs while inference. I am using amazon sagemaker. My typical notebook example is this one - https://github.com/huggingface/notebooks/blob/5ef609e9078e6248d73f28106e60ddafa9359db1/sagemaker/24_train_bloom_peft_lora/sagemaker-notebook.ipynb . Are there any resources which I can use as reference to deploy an endpoint using Vllm on sagemaker?

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: books/blob/5ef609e9078e6248d73f28106e60ddafa9359db1/sagemaker/24_train_bloom_peft_lora/sagemaker-notebook.ipynb . Are there any resources which I can use as reference to deploy an endpoint using Vllm on sagemaker?
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: sagemaker. My typical notebook example is this one - https://github.com/huggingface/notebooks/blob/5ef609e9078e6248d73f28106e60ddafa9359db1/sagemaker/24_train_bloom_peft_lora/sagemaker-notebook.ipynb . Are there any res...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Sagemaker support for inference Hi, I am trying to test the throughout using vLLMs while inference. I am using amazon sagemaker. My typical notebook example is this one - https://github.com/huggingface/notebooks/blob/5e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
