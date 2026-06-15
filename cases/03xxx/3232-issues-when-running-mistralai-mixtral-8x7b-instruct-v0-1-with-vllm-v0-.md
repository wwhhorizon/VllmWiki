# vllm-project/vllm#3232: Issues when running mistralai/Mixtral-8x7B-Instruct-v0.1 with vllm:v0.3.2.

| 字段 | 值 |
| --- | --- |
| Issue | [#3232](https://github.com/vllm-project/vllm/issues/3232) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Issues when running mistralai/Mixtral-8x7B-Instruct-v0.1 with vllm:v0.3.2.

### Issue 正文摘录

Hello I am trying deploy mistralai/Mixtral-8x7B-Instruct-v0.1 model using vllm:0.3.2 but there seems to be some issue. For some reason I am getting the error: **Permission denied: ./triton** . I deployed the same model with vllm: 0.2.6 and the deployment works perfectly fine. I am also attaching the screenshot of the error. Any help would be highly appreciated.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: me issue. For some reason I am getting the error: **Permission denied: ./triton** . I deployed the same model with vllm: 0.2.6 and the deployment works perfectly fine. I am also attaching the screenshot of the error. An...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: lso attaching the screenshot of the error. Any help would be highly appreciated.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: . stale Hello I am trying deploy mistralai/Mixtral-8x7B-Instruct-v0.1 model using vllm:0.3.2 but there seems to be some issue. For some reason I am getting the error: **Permission denied: ./triton** . I deployed the sam...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: sues when running mistralai/Mixtral-8x7B-Instruct-v0.1 with vllm:v0.3.2. stale Hello I am trying deploy mistralai/Mixtral-8x7B-Instruct-v0.1 model using vllm:0.3.2 but there seems to be some issue. For some reason I am...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
