# vllm-project/vllm#21247: [Performance]: Move hash_request_tokens computation from input request threads

| 字段 | 值 |
| --- | --- |
| Issue | [#21247](https://github.com/vllm-project/vllm/issues/21247) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Move hash_request_tokens computation from input request threads

### Issue 正文摘录

### Proposal to improve performance Currently, [hash_request_tokens](https://github.com/vllm-project/vllm/blob/d1fb65bde367aa6e3d72520c84b60be3d1539917/vllm/v1/core/kv_cache_utils.py#L500C5-L500C24) executes in engine core to compute hashes of blocks based on the request token IDs (and lora IDs, MM tokens, etc). And the current design make it to become the hard blocker of inferences. As shown in the following charts, for small models opt128m with QPS 200 (input=700, output=1) scenarios, noticeable amount of time is used compute the hash. Ideally, in order to compute the hashes, all dependent metadata should be ready when the data received on input_socket processing threads who is running in parallel with engine core thread. With this move, we would be able to move the hashes computation out from critical path, as shown in the following chart. ### Report of performance regression N/A ### Misc discussion on performance N/A ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` N/A ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e the hard blocker of inferences. As shown in the following charts, for small models opt128m with QPS 200 (input=700, output=1) scenarios, noticeable amount of time is used compute the hash. Ideally, in order to compute...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: he_utils.py#L500C5-L500C24) executes in engine core to compute hashes of blocks based on the request token IDs (and lora IDs, MM tokens, etc). And the current design make it to become the hard blocker of inferences. As...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance]: Move hash_request_tokens computation from input request threads performance;stale ### Proposal to improve performance Currently, [hash_request_tokens](https://github.com/vllm-project/vllm/blob/d1fb65bde36...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ical path, as shown in the following chart. ### Report of performance regression N/A ### Misc discussion on performance N/A ### Your current environment (if you think it is necessary) ```text The output of `python colle...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: hard blocker of inferences. As shown in the following charts, for small models opt128m with QPS 200 (input=700, output=1) scenarios, noticeable amount of time is used compute the hash. Ideally, in order to compute the h...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
