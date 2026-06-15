# vllm-project/vllm#2413: out of memory running mixtral gptq model in vllm 0.2.7

| 字段 | 值 |
| --- | --- |
| Issue | [#2413](https://github.com/vllm-project/vllm/issues/2413) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> out of memory running mixtral gptq model in vllm 0.2.7

### Issue 正文摘录

https://github.com/vllm-project/vllm/assets/39525455/c6787334-8a22-4dd4-838a-9fff1a1e0a38 The model downloaded from https://huggingface.co/TheBloke/Mixtral-8x7B-Instruct-v0.1-GPTQ and it works well in vllm 0.2.6 but run out of memory using 0.2.7.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: out of memory running mixtral gptq model in vllm 0.2.7 https://github.com/vllm-project/vllm/assets/39525455/c6787334-8a22-4dd4-838a-9fff1a1e0a38 The model downloaded from https://huggingface.co/TheBloke/Mixtral-8x7B-Ins...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
