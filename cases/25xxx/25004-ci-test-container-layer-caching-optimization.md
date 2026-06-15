# vllm-project/vllm#25004: [CI]: Test container layer caching optimization

| 字段 | 值 |
| --- | --- |
| Issue | [#25004](https://github.com/vllm-project/vllm/issues/25004) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI]: Test container layer caching optimization

### Issue 正文摘录

We should make sure that the layering/stages are such that the vllm python/docs code resides only in a very thin top layer and that changes to these don't affect lower layers. For example installing all dependencies in a separate command/layer (I _think_ we're already doing that, but we should verify that it's working as intended). Further we should ensure that the intermediate layers are pushed to the docker repo when building and also that remote layer caching is enabled/working when building. This should be complimentary to the other base-image reuse work @dougbtv is doing for https://github.com/vllm-project/vllm/issues/23588, and contributes to https://github.com/vllm-project/vllm/issues/24779. It should help with build time but also startup time on other workers pulling new images.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [CI]: Test container layer caching optimization feature request;stale We should make sure that the layering/stages are such that the vllm python/docs code resides only in a very thin top layer and that changes to these...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [CI]: Test container layer caching optimization feature request;stale We should make sure that the layering/stages are such that the vllm python/docs code resides only in a very thin top layer and that changes to these...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI]: Test container layer caching optimization feature request;stale We should make sure that the layering/stages are such that the vllm python/docs code resides only in a very thin top layer and that changes to these...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
