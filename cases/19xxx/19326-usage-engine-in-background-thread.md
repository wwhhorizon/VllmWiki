# vllm-project/vllm#19326: [Usage]: Engine in background thread

| 字段 | 值 |
| --- | --- |
| Issue | [#19326](https://github.com/vllm-project/vllm/issues/19326) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Engine in background thread

### Issue 正文摘录

I try to use vllm in my project, and I notice "Engine in background thread is experimental on VLLM_USE_V1=1. Falling back to V0 Engine". After commenting on the judgment statement for this piece of code, my project is working properly. I want to know why this feature is experimental in V1，and when support officially in V1. Thanks.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ant to know why this feature is experimental in V1，and when support officially in V1. Thanks.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Engine in background thread usage;stale I try to use vllm in my project, and I notice "Engine in background thread is experimental on VLLM_USE_V1=1. Falling back to V0 Engine". After commenting on the judgment...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
