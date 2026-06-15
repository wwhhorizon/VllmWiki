# vllm-project/vllm#3906: [Bug]: Error with OpenAI server: API request failed with status code 400

| 字段 | 值 |
| --- | --- |
| Issue | [#3906](https://github.com/vllm-project/vllm/issues/3906) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Error with OpenAI server: API request failed with status code 400

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug I encountered an error with the OpenAI server: [openai_api_compatible] Error: API request failed with status code 400: {"object":"error","message":"[{'type': 'string_type', 'loc': ('body', 'messages', 2, 'function_call'), 'msg': 'Input should be a valid string', 'input': {'name': 'function call', 'arguments': '{}'}, 'url': '[https://errors.pydantic.dev/2.6/v/string_type'}]","type":"BadRequestError","param":null,"code":400](https://errors.pydantic.dev/2.6/v/string_type'%7D%5D%22,%22type%22:%22BadRequestError%22,%22param%22:null,%22code%22:400)}

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Error with OpenAI server: API request failed with status code 400 bug ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug I encountered an error with the OpenAI s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
