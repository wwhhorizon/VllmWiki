# vllm-project/vllm#181: Can vllm serving clients by using multiple model instances?

| 字段 | 值 |
| --- | --- |
| Issue | [#181](https://github.com/vllm-project/vllm/issues/181) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Can vllm serving clients by using multiple model instances?

### Issue 正文摘录

Based on the examples, vllm can launch a server with a single model instances. Can vllm serving clients by using multiple model instances? With multiple model instances, the sever will dispatch the requests to different instances to reduce the overhead.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: multiple model instances? With multiple model instances, the sever will dispatch the requests to different instances to reduce the overhead.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Can vllm serving clients by using multiple model instances? Based on the examples, vllm can launch a server with a single model instances. Can vllm serving clients by using multiple model instances? With multiple model...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: el instances? With multiple model instances, the sever will dispatch the requests to different instances to reduce the overhead.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
