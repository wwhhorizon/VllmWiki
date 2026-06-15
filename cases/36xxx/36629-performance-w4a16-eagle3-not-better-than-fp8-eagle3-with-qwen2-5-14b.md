# vllm-project/vllm#36629: [Performance]: W4A16+eagle3 not better than fp8+eagle3 with Qwen2.5-14B

| 字段 | 值 |
| --- | --- |
| Issue | [#36629](https://github.com/vllm-project/vllm/issues/36629) |
| 状态 | open |
| 标签 | performance |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: W4A16+eagle3 not better than fp8+eagle3 with Qwen2.5-14B

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression Under low concurrency (1-8), the performance of w4a16 + eagle3 is higher than that of fp8 + eagle3. However, under high concurrency (16-32), it seems that there is a conflict between w4a16 and eagle3, and the performance is even worse than that of fp8 + eagle3. fp8+eagle3 batch16 ============ Serving Benchmark Result ============ Successful requests: 500 Failed requests: 0 Maximum request concurrency: 16 Request rate configured (RPS): 50.00 Benchmark duration (s): 40.97 Total input tokens: 84383 Total generated tokens: 46345 Request throughput (req/s): 12.20 Output token throughput (tok/s): 1131.19 Peak output token throughput (tok/s): 464.00 Peak concurrent requests: 35.00 Total Token throughput (tok/s): 3190.81 ---------------Time to First Token---------------- Mean TTFT (ms): 121.16 Median TTFT (ms): 115.09 P95 TTFT (ms): 172.56 P99 TTFT (ms): 185.92 -----Time per Output Token (excl. 1st token)------ Mean TPOT (ms): 13.16 Median TPOT (ms): 12.78 P95 TPOT (ms): 16.98 P99 TPOT (ms): 19.36 ---------------Inter-token Latency---------------- Mean ITL (ms): 35.81 Median ITL (ms): 30.46 P95 ITL (ms)...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: roposal to improve performance _No response_ ### Report of performance regression Under low concurrency (1-8), the performance of w4a16 + eagle3 is higher than that of fp8 + eagle3. However, under high concurrency (16-3...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Performance]: W4A16+eagle3 not better than fp8+eagle3 with Qwen2.5-14B performance ### Proposal to improve performance _No response_ ### Report of performance regression Under low concurrency (1-8), the performance of...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: e3 batch16 ============ Serving Benchmark Result ============ Successful requests: 500 Failed requests: 0 Maximum request concurrency: 16 Request rate configured (RPS): 50.00 Benchmark duration (s): 40.97 Total
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Performance]: W4A16+eagle3 not better than fp8+eagle3 with Qwen2.5-14B performance ### Proposal to improve performance _No response_ ### Report of performance regression Under low concurrency (1-8), the performance of...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ecessary) ```text 4090d * 1 vllm 0.16.0 fp8 + eagle3 extra information ：CutlassFP8ScaledMMLinearKernel w4a16 + eagle3 extra information: MarlinLinearKernel ``` ### Before submitting a new issue... - [x] Make sure you al...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
