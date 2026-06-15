# vllm-project/vllm#27278: args.hf_split is overriden even when set causing some dataset to not be actually supported

| 字段 | 值 |
| --- | --- |
| Issue | [#27278](https://github.com/vllm-project/vllm/issues/27278) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> args.hf_split is overriden even when set causing some dataset to not be actually supported

### Issue 正文摘录

https://github.com/vllm-project/vllm/blob/aa1356ec53a65a79a0027e8c265c76d84de8c046/vllm/benchmarks/datasets.py#L1680 using the dataset `openslr/librispeech_asr` ``` Raise ValueError(f"Bad split: {split}. Available splits: {list(splits_generators)}") ValueError: Bad split: train. Available splits: ['test.clean', 'test.other', 'train.clean.100', 'train.clean.360', 'train.other.500', 'validation.clean', 'validation.other'] ```

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: com/vllm-project/vllm/blob/aa1356ec53a65a79a0027e8c265c76d84de8c046/vllm/benchmarks/datasets.py#L1680 using the dataset `openslr/librispeech_asr` ``` Raise ValueError(f"Bad split: {split}. Available splits: {list(splits...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: args.hf_split is overriden even when set causing some dataset to not be actually supported stale https://github.com/vllm-project/vllm/blob/aa1356ec53a65a79a0027e8c265c76d84de8c046/vllm/benchmarks/datasets.py#L1680 using...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: verriden even when set causing some dataset to not be actually supported stale https://github.com/vllm-project/vllm/blob/aa1356ec53a65a79a0027e8c265c76d84de8c046/vllm/benchmarks/datasets.py#L1680 using the dataset `open...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
