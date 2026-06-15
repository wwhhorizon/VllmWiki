# vllm-project/vllm#7490: [Feature]: need to be able to load tiny models with vllm for testing - PagedAttention forces large models

| 字段 | 值 |
| --- | --- |
| Issue | [#7490](https://github.com/vllm-project/vllm/issues/7490) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: need to be able to load tiny models with vllm for testing - PagedAttention forces large models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When one writes unit tests one can't use large models. It appears that vllm doesn't let one use tiny models because of PagedAttention. For 99% of testing use-cases PagedAttention makes no difference whatsoever as we want to test functionality and not speed. Currently PagedAttention causes a problem requiring at least 64 len of each head requiring hidden_dim to be at least 256 which leads to a larger model which is slower to download and run CI against. ``` E ValueError: Head size 8 is not supported by PagedAttention. Supported head sizes are: [64, 80, 96, 112, 120, 128, 192, 256]. ``` ### Alternatives I don't see any way to disable PagedAttention and switch to normal attention which has no shape limitations. Thank you! ### Additional context _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: st 256 which leads to a larger model which is slower to download and run CI against. ``` E ValueError: Head size 8 is not supported by PagedAttention. Supported head sizes are: [64, 80, 96, 112, 120, 128, 192, 256]. ```...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: need to be able to load tiny models with vllm for testing - PagedAttention forces large models feature request ### 🚀 The feature, motivation and pitch When one writes unit tests one can't use large models. It...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: odels with vllm for testing - PagedAttention forces large models feature request ### 🚀 The feature, motivation and pitch When one writes unit tests one can't use large models. It appears that vllm doesn't let one use ti...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Feature]: need to be able to load tiny models with vllm for testing - PagedAttention forces large models feature request ### 🚀 The feature, motivation and pitch When one writes unit tests one can't use large models. It...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
