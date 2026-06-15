# vllm-project/vllm#6643: [Bug] [SpecDecode] Speculative metrics very unlikely to get logged

| 字段 | 值 |
| --- | --- |
| Issue | [#6643](https://github.com/vllm-project/vllm/issues/6643) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] [SpecDecode] Speculative metrics very unlikely to get logged

### Issue 正文摘录

### Your current environment n/a ### 🐛 Describe the bug After merging #6578, the `AsyncMetricsCollector` now respects the time interval between collecting speculative decoding metrics. It now collects the metrics every 5 seconds, instead of continuously collecting them. While this is the desired behaviour, I now see that in practice, we are never logging the speculative decoding stats. This is because, in order to get logged, the speculative decoding stats need to happen to be collected in exactly the same step that we decide to log the output (which is controlled by a [different time interval](https://github.com/vllm-project/vllm/blob/89c1c6a196e80536bb392c422e7f34439b1f3104/vllm/engine/metrics.py#L382-L384)). In practice, this does not seem to happen using the default settings.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug] [SpecDecode] Speculative metrics very unlikely to get logged bug ### Your current environment n/a ### 🐛 Describe the bug After merging #6578, the `AsyncMetricsCollector` now respects the time interval between coll...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: stats need to happen to be collected in exactly the same step that we decide to log the output (which is controlled by a [different time interval](https://github.com/vllm-project/vllm/blob/89c1c6a196e80536bb392c422e7f34...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
