# vllm-project/vllm#34763: [Performance]: Remove `batch_size` and `max_seq_len` padding when cuDNN is upgraded to 9.19

| 字段 | 值 |
| --- | --- |
| Issue | [#34763](https://github.com/vllm-project/vllm/issues/34763) |
| 状态 | open |
| 标签 | performance;unstale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Remove `batch_size` and `max_seq_len` padding when cuDNN is upgraded to 9.19

### Issue 正文摘录

### Proposal to improve performance After merging https://github.com/vllm-project/vllm/pull/34580 and: https://github.com/vllm-project/vllm/pull/34580/changes#diff-89b6b3d99f8961ecdc0cf8cf16b0f9e091a6227ee2a9bfb4f04b88043278e0e0R151 When Torch is upgraded, cuDNN will be also upgraded to 9.19 where we can use real `batch_size` and `max_seq_len` for non-cudaGraph path. cc @wangshangsam @ywang96 @Anerudhan @b-mu ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ded to 9.19 where we can use real `batch_size` and `max_seq_len` for non-cudaGraph path. cc @wangshangsam @ywang96 @Anerudhan @b-mu ### Report of performance regression _No response_ ### Misc discussion on performance _...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: . cc @wangshangsam @ywang96 @Anerudhan @b-mu ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The ou...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ` and `max_seq_len` padding when cuDNN is upgraded to 9.19 performance;unstale ### Proposal to improve performance After merging https://github.com/vllm-project/vllm/pull/34580 and: https://github.com/vllm-project/vllm/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
