# vllm-project/vllm#1463: Error when launching a FastAPI server with mistral AWQ model

| 字段 | 值 |
| --- | --- |
| Issue | [#1463](https://github.com/vllm-project/vllm/issues/1463) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Error when launching a FastAPI server with mistral AWQ model

### Issue 正文摘录

When I try to launch a mistral model server like the following: python -m vllm.entrypoints.api_server --model TheBloke/Mistral-7B-OpenOrca-AWQ I get this error: ``` File "/usr/local/lib/python3.10/site-packages/vllm/model_executor/models/mistral.py", line 388, in load_weights param = state_dict[name] KeyError: 'model.layers.0.mlp.down_proj.qweight' ``` I've gotten this same error with a few other AWQ mistral variants I've attempted.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Error when launching a FastAPI server with mistral AWQ model When I try to launch a mistral model server like the following: python -m vllm.entrypoints.api_server --model TheBloke/Mistral-7B-OpenOrca-AWQ I get this erro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
