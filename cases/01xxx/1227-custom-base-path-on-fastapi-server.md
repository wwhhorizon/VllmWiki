# vllm-project/vllm#1227: Custom base path on FastAPI server

| 字段 | 值 |
| --- | --- |
| Issue | [#1227](https://github.com/vllm-project/vllm/issues/1227) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Custom base path on FastAPI server

### Issue 正文摘录

Hello everyone, We have a situation here in which we are deploying our LLMs behind a ALB on AWS using path prefix, in this case it is deployed on a path that looks like `my.domain.com/my-model`. By default ALBs on AWS doesn't support path rewrite so it will forward the request to the API server including the `/my-model` on it, breaking the API because this URL doesn't exist there given that the API only listens in the `/generate` path. I implemented a custom API server here, but I think we could add an optional parameter (or ENV VAR) that we can use to set the base path of the server (or keep the default behavior if it is not there). I can open a PR doing this, but I wanted to confirm if this is something that makes sense for other people before I actually do this.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: in this case it is deployed on a path that looks like `my.domain.com/my-model`. By default ALBs on AWS doesn't support path rewrite so it will forward the request to the API server including the `/my-model` on it, break...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: default ALBs on AWS doesn't support path rewrite so it will forward the request to the API server including the `/my-model` on it, breaking the API because this URL doesn't exist there given that the API only listens in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
