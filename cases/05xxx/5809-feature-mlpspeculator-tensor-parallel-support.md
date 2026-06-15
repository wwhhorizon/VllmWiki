# vllm-project/vllm#5809: [Feature]: MLPSpeculator Tensor Parallel support

| 字段 | 值 |
| --- | --- |
| Issue | [#5809](https://github.com/vllm-project/vllm/issues/5809) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: MLPSpeculator Tensor Parallel support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch `MLPSpeculator`-based speculative decoding was recently added in https://github.com/vllm-project/vllm/pull/4947, but the initial integration only covers single GPU usage. There will soon be "speculator" models available for larger target models that require multiple GPUs so we would like to ensure that TP can be used. The first part of this issue would be testing it out in conjunction with https://github.com/vllm-project/vllm/pull/5414 and making necessary adjustments so that it will work with TP=1 for the speculator and TP=N for the target model. Following this we can look at having the speculator itself run with TP>1, but that may be more involved since it will require some distributed coordination of the sampling of each speculated token in the MLPSpeculator loop. It might be possible to avoid additional communication here by the having the sampler used by the speculator model use a dedicated `torch.Generator` for its sampling and doing this sampling in tandem across the ranks. @JRosenkranz already used `VocabParallelEmbedding` in the implementation so the model layers themselves should work fine. cc @cadedaniel @sirejdua @JRosenkranz @td...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: MLPSpeculator Tensor Parallel support feature request ### 🚀 The feature, motivation and pitch `MLPSpeculator`-based speculative decoding was recently added in https://github.com/vllm-project/vllm/pull/4947, b...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tegration only covers single GPU usage. There will soon be "speculator" models available for larger target models that require multiple GPUs so we would like to ensure that TP can be used. The first part of this issue w...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ke to ensure that TP can be used. The first part of this issue would be testing it out in conjunction with https://github.com/vllm-project/vllm/pull/5414 and making necessary adjustments so that it will work with TP=1 f...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
