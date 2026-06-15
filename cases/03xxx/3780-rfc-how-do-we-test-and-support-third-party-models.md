# vllm-project/vllm#3780: [RFC] How do we test and support third-party models

| 字段 | 值 |
| --- | --- |
| Issue | [#3780](https://github.com/vllm-project/vllm/issues/3780) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC] How do we test and support third-party models

### Issue 正文摘录

### Anything you want to discuss about vllm. This RFC solicits the community's comments on how we test and support third-party models. Ideally, we can test the consistency between the models implemented in `vllm` and in `transformers`. However, apples to apples comparison is not always possible, because many acceleration techniques and faster computation kernels use low-precision floating point computation. Acceleration comes with loss of precision. Therefore, there are three types of cause for the difference bwteen `vllm` and `transformers`: 1. `vllm`'s intended implementation of new features, e.g. faster computation kernels 2. `vllm`'s implementation bug 3. `transformers`' bc-breaking changes Currently, we have consistency check for llama in our CI. It is difficult for us to test every supported model in every CI. And people may find bugfix in one model that can break another model, e.g. https://github.com/vllm-project/vllm/pull/3767 . To release the burden of vllm developers, I think we should only keep a "best-effort" promise on third-party models: - When users request a new model, a PR from the community comes out to support it. As long as the output is sensible, we can accep...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [RFC] How do we test and support third-party models RFC;stale ### Anything you want to discuss about vllm. This RFC solicits the community's comments on how we test and support third-party models. Ideally, we can test t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: els RFC;stale ### Anything you want to discuss about vllm. This RFC solicits the community's comments on how we test and support third-party models. Ideally, we can test the consistency between the models implemented in...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC] How do we test and support third-party models RFC;stale ### Anything you want to discuss about vllm. This RFC solicits the community's comments on how we test and support third-party models. Ideally, we can test t...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ause many acceleration techniques and faster computation kernels use low-precision floating point computation. Acceleration comes with loss of precision. Therefore, there are three types of cause for the difference bwte...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [RFC] How do we test and support third-party models RFC;stale ### Anything you want to discuss about vllm. This RFC solicits the community's comments on how we test and support third-party models. Ideally, we can test t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
