# vllm-project/vllm#23589: [CI]: Investigate use of CPU backend for subset of tests

| 字段 | 值 |
| --- | --- |
| Issue | [#23589](https://github.com/vllm-project/vllm/issues/23589) |
| 状态 | closed |
| 标签 | ci/build;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI]: Investigate use of CPU backend for subset of tests

### Issue 正文摘录

Many of the tests are concerned with frontend parts of the system (like the API sever) and/or backend-agnostic aspects. For these it could be preferable to use the CPU back-end / image, along with tiny models. This may be faster and would help to reduce the consumed GPU-hours since these tests could be scheduled on CPU-only workers.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI]: Investigate use of CPU backend for subset of tests ci/build;stale Many of the tests are concerned with frontend parts of the system (like the API sever) and/or backend-agnostic aspects. For these it could be prefer
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [CI]: Investigate use of CPU backend for subset of tests ci/build;stale Many of the tests are concerned with frontend parts of the system (like the API sever) and/or backend-agnostic aspects. For these it could be prefe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: it could be preferable to use the CPU back-end / image, along with tiny models. This may be faster and would help to reduce the consumed GPU-hours since these tests could be scheduled on CPU-only workers.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [CI]: Investigate use of CPU backend for subset of tests ci/build;stale Many of the tests are concerned with frontend parts of the system (like the API sever) and/or backend-agnostic aspects. For these it could be prefe...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI]: Investigate use of CPU backend for subset of tests ci/build;stale Many of the tests are concerned with frontend parts of the system (like the API sever) and/or backend-agnostic aspects. For these it could be prefe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
