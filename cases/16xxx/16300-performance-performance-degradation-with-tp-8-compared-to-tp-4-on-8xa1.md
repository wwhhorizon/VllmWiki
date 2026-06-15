# vllm-project/vllm#16300: [Performance]: Performance degradation with tp=8 compared to tp=4 on 8xA100(80G)

| 字段 | 值 |
| --- | --- |
| Issue | [#16300](https://github.com/vllm-project/vllm/issues/16300) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Performance degradation with tp=8 compared to tp=4 on 8xA100(80G)

### Issue 正文摘录

## Performance degradation with `tp=8` compared to `tp=4` I’m currently running some deployment experiments using vLLM and have noticed a performance issue when increasing the tensor parallelism (`--tensor-parallel-size`). Specifically: + When setting `tp=8`, the model throughput under high request load is **lower** than when using `tp=4`. + I expected the throughput to scale up (didn’t expect to scale linearly, but should at least be equal, according to other people's experiments such as [https://github.com/vllm-project/vllm/issues/8089](issue link) ), but it actually drops noticeably at `tp=8`. **Test environment:👇🏻** gpu: 8*A100(80GB) model: QwQ-32B software: vllm 0.7.2 + torch 2.5 test script: benchmark latency [https://github.com/vllm-project/vllm/blob/main/benchmarks/benchmark_latency.py](https://github.com/vllm-project/vllm/blob/main/benchmarks/benchmark_latency.py) **Here are our experimental results👇🏻** | | batch-size | tp=2 | tp=4 | tp=8 | | --- | --- | --- | --- | --- | | input=1 output=200 | 1 | 5.50s 36.2tok/s | 3.91s 50tok/s | 3.15s 63tok/s | | | 16 | 6.07s 528tok/s | 4.77s 660tok/s | 4.25s 760tok/s | | | 128 | 11.34s 2300tok/s | 10.68s 2350tok/s | 14.58s 1790tok/s |...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: -tensor-parallel-size`). Specifically: + When setting `tp=8`, the model throughput under high request load is **lower** than when using `tp=4`. + I expected the throughput to scale up (didn’t expect to scale linearly, b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Performance]: Performance degradation with tp=8 compared to tp=4 on 8xA100(80G) performance;stale ## Performance degradation with `tp=8` compared to `tp=4` I’m currently running some deployment experiments using vLLM a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ue when increasing the tensor parallelism (`--tensor-parallel-size`). Specifically: + When setting `tp=8`, the model throughput under high request load is **lower** than when using `tp=4`. + I expected the throughput to...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: rmance degradation with tp=8 compared to tp=4 on 8xA100(80G) performance;stale ## Performance degradation with `tp=8` compared to `tp=4` I’m currently running some deployment experiments using vLLM and have noticed a pe...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: load is **lower** than when using `tp=4`. + I expected the throughput to scale up (didn’t expect to scale linearly, but should at least be equal, according to other people's experiments such as [https://github.com/vllm-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
