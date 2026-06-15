# vllm-project/vllm#874: Served fastapi model locally but got error while deploying it

| 字段 | 值 |
| --- | --- |
| Issue | [#874](https://github.com/vllm-project/vllm/issues/874) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Served fastapi model locally but got error while deploying it

### Issue 正文摘录

I am using [api_server.py](https://github.dev/vllm-project/vllm/blob/main/vllm/entrypoints/openai/api_server.py). It works perfectly locally. But when deploying it in production, I got error stating: ```NameError: tokenizer not defined```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Served fastapi model locally but got error while deploying it I am using [api_server.py](https://github.dev/vllm-project/vllm/blob/main/vllm/entrypoints/openai/api_server.py). It works perfectly locally. But when deploy...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
