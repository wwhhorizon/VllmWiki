# vllm-project/vllm#2228: how to add history in /vllm/entrypoints/api_server.py？

| 字段 | 值 |
| --- | --- |
| Issue | [#2228](https://github.com/vllm-project/vllm/issues/2228) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> how to add history in /vllm/entrypoints/api_server.py？

### Issue 正文摘录

hi everyone, could you please help me take a look at this question? how to add history in /vllm/entrypoints/api_server.py？ If the request includes prompt and histroy，such as : {"prompt": "What floor do I live on？"， "history": [["Please remember, I live on the 10th floor","ok, I will remember that" ]]"} How should I add history to the prompt? Is it using a template? Doesn't each model have a different template?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: should I add history to the prompt? Is it using a template? Doesn't each model have a different template?
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: question? how to add history in /vllm/entrypoints/api_server.py？ If the request includes prompt and histroy，such as : {"prompt": "What floor do I live on？"， "history": [["Please remember, I live on the 10th floor","ok,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
