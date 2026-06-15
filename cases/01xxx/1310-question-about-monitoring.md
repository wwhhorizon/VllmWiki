# vllm-project/vllm#1310: Question about monitoring

| 字段 | 值 |
| --- | --- |
| Issue | [#1310](https://github.com/vllm-project/vllm/issues/1310) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Question about monitoring

### Issue 正文摘录

Hello, First of all, thank you for this great framework. I was using your `entrypoints.openai.api_server` implementation and I needed to use `monitoring` so I added ```python instrumentator = Instrumentator().instrument(app) @app.on_event("startup") async def _startup(): instrumentator.expose(app) ``` Would it be useful to add it to your codebase, it requires `prometheus-fastapi-instrumentator` so I was not sure. If it will be useful I can open a PR for this

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
