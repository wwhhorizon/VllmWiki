# vllm-project/vllm#4424: [Misc]: Odd number GPU utilization?

| 字段 | 值 |
| --- | --- |
| Issue | [#4424](https://github.com/vllm-project/vllm/issues/4424) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Odd number GPU utilization?

### Issue 正文摘录

### Anything you want to discuss about vllm. Currently tp will not work on odd number of gpus, nor on the number that cannot divide 40 (e.g. 6 gpus). However, it is unavoidable to have these kinds of configurations in some situations. What are some ways to keep the left-out gpu(s) from being completely idle currently? Are there any plans to solve or circumvent this problem?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s) from being completely idle currently? Are there any plans to solve or circumvent this problem?
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: vide 40 (e.g. 6 gpus). However, it is unavoidable to have these kinds of configurations in some situations. What are some ways to keep the left-out gpu(s) from being completely idle currently? Are there any plans to sol...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Misc]: Odd number GPU utilization? stale ### Anything you want to discuss about vllm. Currently tp will not work on odd number of gpus, nor on the number that cannot divide 40 (e.g. 6 gpus). However, it is unavoidable...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
