# vllm-project/vllm#7116: [Performance]: From SequenceGroup-native code to Sequence-native code

| 字段 | 值 |
| --- | --- |
| Issue | [#7116](https://github.com/vllm-project/vllm/issues/7116) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: From SequenceGroup-native code to Sequence-native code

### Issue 正文摘录

### Proposal to improve performance We have two concepts in vLLM: - SequenceGroup, a group of sequence, that originates from the same request. In most usecases, a sequence group contains only one sequence. In parallel sampling, a request can fork into many sequences, depending on the sampling parameter `n`. In beam search, sequences in the sequence group can change, grow, die. - Sequence, consists of a sequence seen by the inference engine. It has prompt, generated tokens, kv cache... In order to support diverse sampling algorithms, vLLM currently takes a SequenceGroup-native approach: many functions operate in the SequenceGroup-level, e.g. `prepare_input` takes in a list of `SequenceGroup`. The problem is, many functions in an inference engine, naturally fit into Sequence-level operations. For example, when we talk about the batchsize for decoding, it is the number of Sequence we are running for decoding, not the number of SequenceGroup. To fill in the gap, there are many code in vLLM, that receives SequenceGroup, and unpack the SequenceGroup into Sequence for further operations. Notably, prepare input: https://github.com/vllm-project/vllm/blob/825b044863a8e3af82a82a80cd2617486cc...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: a/vllm/worker/model_runner.py#L507-L510 This turns out to be very inefficient, makes the code difficult to read/maintain. To have a rough impression about how inefficient these conversion can be, take a look at https://...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: nce]: From SequenceGroup-native code to Sequence-native code performance;stale ### Proposal to improve performance We have two concepts in vLLM: - SequenceGroup, a group of sequence, that originates from the same reques...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: oving some `get_seqs` call in `SequenceGroup`, can lead to 1% end-to-end throughput gain. Per the discussion in https://github.com/vllm-project/vllm/issues/6226 , we will not directly drop beam search support. However,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: into many sequences, depending on the sampling parameter `n`. In beam search, sequences in the sequence group can change, grow, die. - Sequence, consists of a sequence seen by the inference engine. It has prompt, genera...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: sequence seen by the inference engine. It has prompt, generated tokens, kv cache... In order to support diverse sampling algorithms, vLLM currently takes a SequenceGroup-native approach: many functions operate in the Se...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
