# vllm-project/vllm#457: Support Kuberenetes for Distributed Serving

| 字段 | 值 |
| --- | --- |
| Issue | [#457](https://github.com/vllm-project/vllm/issues/457) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support Kuberenetes for Distributed Serving

### Issue 正文摘录

Only having support for ray for distributed inference will significantly reduce adoption of this tool if it truly is more performant than TGI. TGI can be run as a black-box image on Kubernetes with support for sharded models and vLLM should support this as well.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Support Kuberenetes for Distributed Serving feature request;stale Only having support for ray for distributed inference will significantly reduce adoption of this tool if it truly is more performant than TGI. TGI can be...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: I can be run as a black-box image on Kubernetes with support for sharded models and vLLM should support this as well.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
