# vllm-project/vllm#2094: How can I deployment multi model？

| 字段 | 值 |
| --- | --- |
| Issue | [#2094](https://github.com/vllm-project/vllm/issues/2094) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How can I deployment multi model？

### Issue 正文摘录

If I have a model, it can not only deployment on single gpu, but also deployment on two gpu by tensor parallel. Now I want deployment the model on two gpu and every gpu load a whole model not tensor parallel. How can I use vllm start command. For example, model = model_0 + model_1 , tensor parallel means gpu_0 : model_0 , gpu_1 : model_1, I want gpu_0 : model, gpu_1 : model

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: How can I deployment multi model？ If I have a model, it can not only deployment on single gpu, but also deployment on two gpu by tensor parallel. Now I want deployment the model on two gpu and every gpu load a whole mod...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
