# vllm-project/vllm#11345: [Performance]: 1P1D Disaggregation performance

| 字段 | 值 |
| --- | --- |
| Issue | [#11345](https://github.com/vllm-project/vllm/issues/11345) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: 1P1D Disaggregation performance

### Issue 正文摘录

### Proposal to improve performance I try to reproduce the P&D 1P1D benchmark to compare performance with chunked prefill https://github.com/vllm-project/vllm/blob/main/benchmarks/disagg_benchmarks/disagg_performance_benchmark.sh. TTFL is higher than what I expected. Because the overhead benchmark only shows ~20-30ms level. What's more, seems ITL is also much higher than chunked prefill. - GPU device: 2* L40S. - Model: Qwen/Qwen2.5-7B-Instruct - Parameters: gpu-memory-utilization 0.6 + kv_buffer_size 10e9 - dataset input 1024 output 50. /cc @KuntaiDu ### Report of performance regression ![image](https://github.com/user-attachments/assets/2c5ec50f-1e5b-48c6-aca2-ab0be42935ed) ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ale ### Proposal to improve performance I try to reproduce the P&D 1P1D benchmark to compare performance with chunked prefill https://github.com/vllm-project/vllm/blob/main/benchmarks/disagg_benchmarks/disagg_performanc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ITL is also much higher than chunked prefill. - GPU device: 2* L40S. - Model: Qwen/Qwen2.5-7B-Instruct - Parameters: gpu-memory-utilization 0.6 + kv_buffer_size 10e9 - dataset input 1024 output 50. /cc @KuntaiDu ### Rep...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance]: 1P1D Disaggregation performance performance;stale ### Proposal to improve performance I try to reproduce the P&D 1P1D benchmark to compare performance with chunked prefill https://github.com/vllm-project/...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: formance performance;stale ### Proposal to improve performance I try to reproduce the P&D 1P1D benchmark to compare performance with chunked prefill https://github.com/vllm-project/vllm/blob/main/benchmarks/disagg_bench...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
