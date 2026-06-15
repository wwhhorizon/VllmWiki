# vllm-project/vllm#6809: [Misc]: call for help to fix tensorizer tests

| 字段 | 值 |
| --- | --- |
| Issue | [#6809](https://github.com/vllm-project/vllm/issues/6809) |
| 状态 | closed |
| 标签 |  |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: call for help to fix tensorizer tests

### Issue 正文摘录

### Anything you want to discuss about vllm. The tensorizer feature, introduced in https://github.com/vllm-project/vllm/pull/3476 , has been flaky recently. An example failure: https://buildkite.com/vllm/fastcheck/builds/1061#0190ec55-50c1-4cf2-8380-bd7238e99cea We call for help from the community, to fix the tests. Ideally, maybe the author of that PR, @sangstar . We will mark it as flaky and non-blocking for tests first. If we cannot fix it in weeks, then we need to consider removing the test.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: t/vllm/pull/3476 , has been flaky recently. An example failure: https://buildkite.com/vllm/fastcheck/builds/1061#0190ec55-50c1-4cf2-8380-bd7238e99cea We call for help from the community, to fix the tests. Ideally, maybe...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ybe the author of that PR, @sangstar . We will mark it as flaky and non-blocking for tests first. If we cannot fix it in weeks, then we need to consider removing the test.
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Misc]: call for help to fix tensorizer tests ### Anything you want to discuss about vllm. The tensorizer feature, introduced in https://github.com/vllm-project/vllm/pull/3476 , has been flaky recently. An example failu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
