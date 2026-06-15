# vllm-project/vllm#21954: [Bug]: Console stats logging is incorrect when using api-server scaleout

| 字段 | 值 |
| --- | --- |
| Issue | [#21954](https://github.com/vllm-project/vllm/issues/21954) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Console stats logging is incorrect when using api-server scaleout

### Issue 正文摘录

StatsLoggers run in the front-end process. When there are multiple of these they will each be processing a subset of requests and thus have incomplete stats. The prometheus stats logger aggregates the stats via it's shm-based multiprocessing mode, but the periodic console log that shows request queue lengths, throughput, and kv cache usage will happen independently in each front-end process and thus be incomplete/incorrect. At a minimum we should disable this statslogger for `api_server_count > 1`.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: hen there are multiple of these they will each be processing a subset of requests and thus have incomplete stats. The prometheus stats logger aggregates the stats via it's shm-based multiprocessing mode, but the periodi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: Console stats logging is incorrect when using api-server scaleout bug StatsLoggers run in the front-end process. When there are multiple of these they will each be processing a subset of requests and thus have in...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: e periodic console log that shows request queue lengths, throughput, and kv cache usage will happen independently in each front-end process and thus be incomplete/incorrect. At a minimum we should disable this statslogg...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ing mode, but the periodic console log that shows request queue lengths, throughput, and kv cache usage will happen independently in each front-end process and thus be incomplete/incorrect. At a minimum we should disabl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
