# vllm-project/vllm#1343: about vllm healthy check on k8s

| 字段 | 值 |
| --- | --- |
| Issue | [#1343](https://github.com/vllm-project/vllm/issues/1343) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> about vllm healthy check on k8s

### Issue 正文摘录

Deploying vllm on k8s For service stability, healthy check is configured 1. TCP check 2. real llm request 3. healthy check api 1. tcp is a little simple 2. real request relative resource consumption Can we add a simple calculation to provide check as follows ``` @app.get("/healthz") async def health_check(): """Health check""" # a simple compute ``` if it works, I would like to contribute this pr

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: eck on k8s Deploying vllm on k8s For service stability, healthy check is configured 1. TCP check 2. real llm request 3. healthy check api 1. tcp is a little simple 2. real request relative resource consumption Can we ad...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: service stability, healthy check is configured 1. TCP check 2. real llm request 3. healthy check api 1. tcp is a little simple 2. real request relative resource consumption Can we add a simple calculation to provide che...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
