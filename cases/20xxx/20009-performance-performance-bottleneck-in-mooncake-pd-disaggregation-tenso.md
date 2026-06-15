# vllm-project/vllm#20009: [Performance]: Performance Bottleneck in Mooncake PD Disaggregation: tensorhash() and safetensor_save() Overhead

| 字段 | 值 |
| --- | --- |
| Issue | [#20009](https://github.com/vllm-project/vllm/issues/20009) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Performance Bottleneck in Mooncake PD Disaggregation: tensorhash() and safetensor_save() Overhead

### Issue 正文摘录

### Proposal to improve performance Hi team, I've been conducting performance tests on vllm PD Disaggregation using mooncake_store_connector, and found that the most time-consuming parts are not the actual put() operations, but rather: - [tensorhash()](https://github.com/vllm-project/vllm/blob/b6553be1bc75f046b00046a4ad7576364d03c835/vllm/distributed/kv_transfer/kv_connector/mooncake_store_connector.py#L198) - [safetensor_save()](https://github.com/vllm-project/vllm/blob/b6553be1bc75f046b00046a4ad7576364d03c835/vllm/distributed/kv_transfer/kv_lookup_buffer/mooncake_store.py#L131) Based on profiling traces, these two steps dominate the runtime during PD disaggregation, more than the actual storage or network transmission: ![Image](https://github.com/user-attachments/assets/320e80c2-976e-4ff5-9fd4-ff65ecf3ba83) **Observations:** tensorhash() seems to repeatedly compute SHA256 hashes over possibly large tensors. safetensor_save() is used per tensor and appears to serialize, which is expensive when invoked frequently. **Questions:** Maybe we could parallelize the hash computation using multithreading? Is there any alternatives for safetensor_save()? Thanks! ### Report of performance r...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: posal to improve performance Hi team, I've been conducting performance tests on vllm PD Disaggregation using mooncake_store_connector, and found that the most time-consuming parts are not the actual put() operations, bu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: me during PD disaggregation, more than the actual storage or network transmission: ![Image](https://github.com/user-attachments/assets/320e80c2-976e-4ff5-9fd4-ff65ecf3ba83) **Observations:** tensorhash() seems to repeat...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Disaggregation: tensorhash() and safetensor_save() Overhead performance;stale ### Proposal to improve performance Hi team, I've been conducting performance tests on vllm PD Disaggregation using mooncake_store_connector,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
