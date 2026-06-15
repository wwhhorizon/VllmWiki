# vllm-project/vllm#23455: [CI]: Add timeouts to all tests

| 字段 | 值 |
| --- | --- |
| Issue | [#23455](https://github.com/vllm-project/vllm/issues/23455) |
| 状态 | closed |
| 标签 | ci/build |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI]: Add timeouts to all tests

### Issue 正文摘录

A common failure mode is a test getting stuck, which consumes the GPU resources until the top-level buildkite timeout of 3 hours. As a first step we should set timeouts for each of the top-level tests based on measured/expected typical running time. Even better would be more granular timeouts but it might be better to hold off doing this until more test restructuring has been done.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI]: Add timeouts to all tests ci/build A common failure mode is a test getting stuck, which consumes the GPU resources until the top-level buildkite timeout of 3 hours. As a first step we should set timeouts for each o
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI]: Add timeouts to all tests ci/build A common failure mode is a test getting stuck, which consumes the GPU resources until the top-level buildkite timeout of 3 hours. As a first step we should set timeouts for each...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
