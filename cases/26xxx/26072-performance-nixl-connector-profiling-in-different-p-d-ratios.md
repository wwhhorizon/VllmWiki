# vllm-project/vllm#26072: [Performance]: NIXL Connector Profiling in different P:D ratios

| 字段 | 值 |
| --- | --- |
| Issue | [#26072](https://github.com/vllm-project/vllm/issues/26072) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: NIXL Connector Profiling in different P:D ratios

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I am benchmarking performance of vLLM xPyD using NIXL connector in various configurations and observing some surprising numbers. Model: Llama 3.1 8B GPU: 4xA100 Num prompts: 100, rps = 25.0 Input length: 1000 Output length: 100 Dataset: Random P50 Latencies are reported in ms. | Config | ITL (ms) | TTFT (ms) | Output Throughput | |--------|----------|-----------|-------------------| | 1P1D | 103.40 | 2872.12 | 538.63 | | 2P1D | 180.73 | 2738.64 | 437.22 | | 3P1D | 215.54 | 2759.40 | 364.69 | | 1P2D | 184.51 | 5017.92 | 364.01 | | 2P2D | 226.87 | 3956.31 | 349.93 | I observe the following: 1. Increase Prefill GPUs worsens ITL, and does not help with TTFT. I expected TTFT improvements on increasing prefill because this is an input heavy workload, but understand that it might not be the case because the first token is output by the decode GPU worker. In the case of lower RPS (for example 10.0) TTFT in fact worsens with additional Prefill GPUs. Additionally, why is ITL getting worse? 2. Increase Decode GPUs worsens both ITL and TTFT. Why is this the c...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: [Performance]: NIXL Connector Profiling in different P:D ratios performance ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I am be...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: am benchmarking performance of vLLM xPyD using NIXL connector in various configurations and observing some surprising numbers. Model: Llama 3.1 8B GPU: 4xA100 Num prompts: 100, rps = 25.0 Input length: 1000 Output lengt...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ps = 25.0 Input length: 1000 Output length: 100 Dataset: Random P50 Latencies are reported in ms. | Config | ITL (ms) | TTFT (ms) | Output Throughput | |--------|----------|-----------|-------------------| | 1P1D | 103....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tions and observing some surprising numbers. Model: Llama 3.1 8B GPU: 4xA100 Num prompts: 100, rps = 25.0 Input length: 1000 Output length: 100 Dataset: Random P50 Latencies are reported in ms. | Config | ITL (ms) | TTF...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: | 3956.31 | 349.93 | I observe the following: 1. Increase Prefill GPUs worsens ITL, and does not help with TTFT. I expected TTFT improvements on increasing prefill because this is an input heavy workload, but understand...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
