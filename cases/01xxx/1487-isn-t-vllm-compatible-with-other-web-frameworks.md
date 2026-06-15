# vllm-project/vllm#1487: Isn't vllm compatible with other web frameworks?

| 字段 | 值 |
| --- | --- |
| Issue | [#1487](https://github.com/vllm-project/vllm/issues/1487) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Isn't vllm compatible with other web frameworks?

### Issue 正文摘录

**_Dear author, At the bottom I used the flask framework to build the web service, but there were some strange phenomena (below). Isn't vllm compatible with other web frameworks?_** **phenomena** : ①The first request to enter can be reasoned normally; ②Second request, vllm directly calls abort_request; ③ After subsequent requests are Received, vllm prints a log saying Received request, but no more inference is performed. **MY ENV: flask rtx4090 vllm0.2.0 python3.8 cuda11.8**

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: g Received request, but no more inference is performed. **MY ENV: flask rtx4090 vllm0.2.0 python3.8 cuda11.8**
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: frameworks? **_Dear author, At the bottom I used the flask framework to build the web service, but there were some strange phenomena (below). Isn't vllm compatible with other web frameworks?_** **phenomena** : ①The firs...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: llm compatible with other web frameworks?_** **phenomena** : ①The first request to enter can be reasoned normally; ②Second request, vllm directly calls abort_request; ③ After subsequent requests are Received, vllm print...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
