# vllm-project/vllm#4440: [Performance]: Empirical Measurement of how to broadcast python object in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#4440](https://github.com/vllm-project/vllm/issues/4440) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Empirical Measurement of how to broadcast python object in vLLM

### Issue 正文摘录

### Proposal to improve performance When we use tensor parallel in vLLM, the driver worker need to broadcast some metadata to all workers, such as the input, the lora requests, etc. This functionality is currently implemented in: https://github.com/vllm-project/vllm/blob/9c7306ac114da3e31a5ff040a76f6c640354cce8/vllm/distributed/communication_op.py#L143 In essence, it uses `torch.distributed.broadcast_object_list` to broadcast a Python object. This function has many overhead. The overall procedure is: There are three layers of overhead: 1. device memory move: pickle works only for cpu memory. so we need to move data from cpu to device back and forth. 2. pickled data of multiple objects are concated, leading to one memory copy 3. two broadcast operation is needed, one for broadcasting the size of each pickled object, and the other for broadcasting data. Current vLLM implementation packs the data in a list of size one, thus overhead 2 is eliminated: https://github.com/vllm-project/vllm/blob/9c7306ac114da3e31a5ff040a76f6c640354cce8/vllm/distributed/communication_op.py#L173-L175 To remove overhead 1, we can use CPU operation to broadcast this kind of metadata. In addition, if we can kn...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: is the optimal case for broadcasting a Python object. I have wrote some benchmark code in https://gist.github.com/youkaichao/b33fcd70286eb45a4a2d5a6dc32d096b and the result is in https://docs.google.com/spreadsheets/d/1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: pu (gloo) to broadcast the data indeed works better than nccl (gpu). For small size metadata, the broadcast time reduces from 400us to 300us. 2. if we can estimate the rough size, the broadcast time can be reduced to 10...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: we use tensor parallel in vLLM, the driver worker need to broadcast some metadata to all workers, such as the input, the lora requests, etc. This functionality is currently implemented in: https://github.com/vllm-projec...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: d to broadcast some metadata to all workers, such as the input, the lora requests, etc. This functionality is currently implemented in: https://github.com/vllm-project/vllm/blob/9c7306ac114da3e31a5ff040a76f6c640354cce8/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
