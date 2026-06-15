# vllm-project/vllm#1446: How to set model quantization to int4 when calling the api interface?

| 字段 | 值 |
| --- | --- |
| Issue | [#1446](https://github.com/vllm-project/vllm/issues/1446) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to set model quantization to int4 when calling the api interface?

### Issue 正文摘录

I am using the api vllm/entrypoints/openai/api_server.py without setting the parameters for model quantification. I tried --quantition as "int4" but it didn't work. My model is llama2

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: How to set model quantization to int4 when calling the api interface? I am using the api vllm/entrypoints/openai/api_server.py without setting the parameters for model quantification. I tried --quantition as "int4" but...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: How to set model quantization to int4 when calling the api interface? I am using the api vllm/entrypoints/openai/api_server.py without setting the parameters for model quantification. I tried --quantition as "int4" but...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
