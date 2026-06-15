# vllm-project/vllm#4254: [Usage]: Including Sampling Params in a HTTP request

| 字段 | 值 |
| --- | --- |
| Issue | [#4254](https://github.com/vllm-project/vllm/issues/4254) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Including Sampling Params in a HTTP request

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` Ubuntu 20.04, python 3.9 ### How would you like to use vllm Currently, I use **aiohttp** to send asynchronous request to vllm backend for serving. Is there a way to include `SamplingParams` in the HTTP request? The following is how I send the request. ` async with aiohttp.ClientSession() as session: async with session.post(url, headers=headers, data=payload, timeout=300) as response: resp = await response.json() `

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: vllm Currently, I use **aiohttp** to send asynchronous request to vllm backend for serving. Is there a way to include `SamplingParams` in the HTTP request? The following is how I send the request. ` async with aiohttp.C...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Including Sampling Params in a HTTP request usage ### Your current environment ```text The output of `python collect_env.py` ``` Ubuntu 20.04, python 3.9 ### How would you like to use vllm Currently, I use **ai...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
