# vllm-project/vllm#11452: [Performance]: The 4090 takes up more gpu memory than the A30

| 字段 | 值 |
| --- | --- |
| Issue | [#11452](https://github.com/vllm-project/vllm/issues/11452) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: The 4090 takes up more gpu memory than the A30

### Issue 正文摘录

### Proposal to improve performance It's just weird. Why the difference The end result is that the service will be up, but the 4090 service will be OOM when requested, but the A30 will not ### Report of performance regression With all commands being the same, 4090， Graph capturing finished in 71 secs, took 6.56 GiB, A30， Graph capturing finished in 65 secs, took 1.43 GiB 4090 log ``` (VllmWorkerProcess pid=785) INFO 12-24 06:16:39 model_runner.py:1417] If out-of-memory error occurs during cudagraph capture, consider decreasing `gpu_memory_utilizat ion` or switching to eager mode. You can also reduce the `max_num_seqs` as needed to decrease memory usage. INFO 12-24 06:17:49 model_runner.py:1527] Graph capturing finished in 71 secs, took 6.56 GiB (VllmWorkerProcess pid=785) INFO 12-24 06:17:49 model_runner.py:1527] Graph capturing finished in 71 secs, took 6.56 GiB (VllmWorkerProcess pid=786) INFO 12-24 06:17:49 model_runner.py:1527] Graph capturing finished in 71 secs, took 6.56 GiB (VllmWorkerProcess pid=784) INFO 12-24 06:17:49 model_runner.py:1527] Graph capturing finished in 71 secs, took 6.56 GiB INFO 12-24 06:17:49 llm_engine.py:446] init engine (profile, create kv cache, war...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Performance]: The 4090 takes up more gpu memory than the A30 performance ### Proposal to improve performance It's just weird. Why the difference The end result is that the service will be up, but the 4090 service will...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: l be OOM when requested, but the A30 will not ### Report of performance regression With all commands being the same, 4090， Graph capturing finished in 71 secs, took 6.56 GiB, A30， Graph capturing finished in 65 secs, to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 2-24 06:16:39 model_runner.py:1417] If out-of-memory error occurs during cudagraph capture, consider decreasing `gpu_memory_utilizat ion` or switching to eager mode. You can also reduce the `max_num_seqs` as needed to d...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: k 1.43 GiB 4090 log ``` (VllmWorkerProcess pid=785) INFO 12-24 06:16:39 model_runner.py:1417] If out-of-memory error occurs during cudagraph capture, consider decreasing `gpu_memory_utilizat ion` or switching to eager m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: lt is that the service will be up, but the 4090 service will be OOM when requested, but the A30 will not ### Report of performance regression With all commands being the same, 4090， Graph capturing finished in 71 secs,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
