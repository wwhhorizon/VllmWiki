# vllm-project/vllm#7306: [Bug]: CI will not run `fastcheck` if `ready` label is applied

| 字段 | 值 |
| --- | --- |
| Issue | [#7306](https://github.com/vllm-project/vllm/issues/7306) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: CI will not run `fastcheck` if `ready` label is applied

### Issue 正文摘录

This is problematic as CI looks like it ran all tests but only ran the /pr/ ones

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: CI will not run `fastcheck` if `ready` label is applied bug This is problematic as CI looks like it ran all tests but only ran the /pr/ ones
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: dy` label is applied bug This is problematic as CI looks like it ran all tests but only ran the /pr/ ones

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
