# vllm-project/vllm#460: streaming does not begin until entire response is completed

| 字段 | 值 |
| --- | --- |
| Issue | [#460](https://github.com/vllm-project/vllm/issues/460) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> streaming does not begin until entire response is completed

### Issue 正文摘录

i'm starting the openai server and making a python post request with `stream=True`. but the results are not starting to be streamed until after the response is completely finished. ``` import requests import json url = "..." headers = {"Content-Type": "application/json"} data = { "model": "...", "prompt": "....", "max_tokens": 108, "temperature": 0, "stream": True, } response = requests.post(url, headers=headers, data=json.dumps(data)) for x in response: print(x) ``` here's the code. nothing starts printing until a few seconds after the request is posted. thanks!

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ing to be streamed until after the response is completely finished. ``` import requests import json url = "..." headers = {"Content-Type": "application/json"} data = { "model": "...", "prompt": "....", "max_tokens": 108...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: l = "..." headers = {"Content-Type": "application/json"} data = { "model": "...", "prompt": "....", "max_tokens": 108, "temperature": 0, "stream": True, } response = requests.post(url, headers=headers, data=json.dumps(d...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: is completed bug i'm starting the openai server and making a python post request with `stream=True`. but the results are not starting to be streamed until after the response is completely finished. ``` import requests i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
