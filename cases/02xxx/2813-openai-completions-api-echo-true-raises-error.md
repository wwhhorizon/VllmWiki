# vllm-project/vllm#2813: openai completions api <echo=True> raises Error

| 字段 | 值 |
| --- | --- |
| Issue | [#2813](https://github.com/vllm-project/vllm/issues/2813) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> openai completions api <echo=True> raises Error

### Issue 正文摘录

hello, when i send echo=True through the openai completions api for an openai compatible vllm server with llama-2-7b-hf, i get an "[_client.py:1027] HTTP Request: POST ... 500 Internal Server Error" error. Any suggestions on how i can fix this or why this is happening? I want to know what the other parameters need to be for echo=True to work for [examples/openai_completion_client.py](https://github.com/vllm-project/vllm/blob/3711811b1d2956e83e626c72f0e1607f2dfbc8fb/examples/openai_completion_client.py#L18C1-L24C16). It works fine when echo=False

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ugh the openai completions api for an openai compatible vllm server with llama-2-7b-hf, i get an "[_client.py:1027] HTTP Request: POST ... 500 Internal Server Error" error. Any suggestions on how i can fix this or why t...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: les/openai_completion_client.py#L18C1-L24C16). It works fine when echo=False
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: patible vllm server with llama-2-7b-hf, i get an "[_client.py:1027] HTTP Request: POST ... 500 Internal Server Error" error. Any suggestions on how i can fix this or why this is happening? I want to know what the other...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
