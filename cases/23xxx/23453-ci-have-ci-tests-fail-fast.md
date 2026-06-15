# vllm-project/vllm#23453: [CI]: Have CI tests fail-fast

| 字段 | 值 |
| --- | --- |
| Issue | [#23453](https://github.com/vllm-project/vllm/issues/23453) |
| 状态 | closed |
| 标签 | ci/build |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI]: Have CI tests fail-fast

### Issue 正文摘录

It would be better (IMO) to abort upon the first failure than to run through all. This could be done at least per top level group (like "V1 Tests") but, or potentially abort the entire run. This is because a re-run is going to be needed regardless (either a fix pushed or the test retried), and it wastes a lot of resources to run the remaining tests.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI]: Have CI tests fail-fast ci/build It would be better (IMO) to abort upon the first failure than to run through all. This could be done at least per top level group (like "V1 Tests") but, or potentially abort the en...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI]: Have CI tests fail-fast ci/build It would be better (IMO) to abort upon the first failure than to run through all. This could be done at least per top level group (like "V1 Tests") but, or potentially abort the en...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
