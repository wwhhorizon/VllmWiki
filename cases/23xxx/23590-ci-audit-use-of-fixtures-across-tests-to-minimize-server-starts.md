# vllm-project/vllm#23590: [CI]: Audit use of fixtures across tests to minimize server starts

| 字段 | 值 |
| --- | --- |
| Issue | [#23590](https://github.com/vllm-project/vllm/issues/23590) |
| 状态 | closed |
| 标签 | ci/build;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI]: Audit use of fixtures across tests to minimize server starts

### Issue 正文摘录

Many tests use a server with the same configuration, or are testing something where it wouldn't matter if the server configuration was changed to be the same as other test(s). We should make sure that the fixtures are configured such that for these we re-use the running server as much as possible and don't stop/start a new vLLM instance for each test. In particular we should try to use package-scoped fixtures in preference to module-scoped, for example in https://github.com/vllm-project/vllm/tree/main/tests/entrypoints/openai. This is a cross-cutting item.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI]: Audit use of fixtures across tests to minimize server starts ci/build;stale Many tests use a server with the same configuration, or are testing something where it wouldn't matter if the server configuration was ch...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: imize server starts ci/build;stale Many tests use a server with the same configuration, or are testing something where it wouldn't matter if the server configuration was changed to be the same as other test(s). We shoul...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ]: Audit use of fixtures across tests to minimize server starts ci/build;stale Many tests use a server with the same configuration, or are testing something where it wouldn't matter if the server configuration was chang...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI]: Audit use of fixtures across tests to minimize server starts ci/build;stale Many tests use a server with the same configuration, or are testing something where it wouldn't matter if the server configuration was ch...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
