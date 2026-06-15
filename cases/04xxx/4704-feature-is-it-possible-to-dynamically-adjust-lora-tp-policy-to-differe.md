# vllm-project/vllm#4704: [Feature]: Is it possible to dynamically adjust lora tp policy to different situations ?

| 字段 | 值 |
| --- | --- |
| Issue | [#4704](https://github.com/vllm-project/vllm/issues/4704) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Is it possible to dynamically adjust lora tp policy to different situations ?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Thanks to the Full TP LoRA pr, now we can use S-LoRA's TP policy. However, this TP strategy provides some performance gains in the case of `long prefills`, while almost certainly introducing additional latency in the `decode` stage due to the new communication operation. Here is some profiling results, i test `qwen1.5 14b` with one LoRA model In this case, i test an end-to-end performance of `long prefill` + `short decode` Typically, we'll usually have a `long prefill`, but not always get a `short decode` every time So... is it possible to apply Full TP when `prefill` and Partial TP when `decode`? ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: e to dynamically adjust lora tp policy to different situations ? feature request;stale ### 🚀 The feature, motivation and pitch Thanks to the Full TP LoRA pr, now we can use S-LoRA's TP policy. However, this TP strategy...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: e case of `long prefills`, while almost certainly introducing additional latency in the `decode` stage due to the new communication operation. Here is some profiling results, i test `qwen1.5 14b` with one LoRA model In...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: the new communication operation. Here is some profiling results, i test `qwen1.5 14b` with one LoRA model In this case, i test an end-to-end performance of `long prefill` + `short decode` Typically, we'll usually have a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ance gains in the case of `long prefills`, while almost certainly introducing additional latency in the `decode` stage due to the new communication operation. Here is some profiling results, i test `qwen1.5 14b` with on...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
