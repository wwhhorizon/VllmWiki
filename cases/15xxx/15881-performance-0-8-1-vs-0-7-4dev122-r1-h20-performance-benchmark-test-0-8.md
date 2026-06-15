# vllm-project/vllm#15881: [Performance]: 0.8.1 vs 0.7.4dev122 R1 H20 performance benchmark test，0.8.1 What is the reason for the 14% performance improvement(throughput tokens/s)

| 字段 | 值 |
| --- | --- |
| Issue | [#15881](https://github.com/vllm-project/vllm/issues/15881) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: 0.8.1 vs 0.7.4dev122 R1 H20 performance benchmark test，0.8.1 What is the reason for the 14% performance improvement(throughput tokens/s)

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression perf test R1 model: input/output=3500/1500, on the same host, vllm 0.8.1 throughtput（total） improve 14%, v0.8.1 why? What are the technical optimizations python3 /root/vllm/benchmarks/benchmark_serving.py --backend vllm \ --model /data00/models/DeepSeek-R1 \ --base-url http://127.0.0.1:8000 \ --endpoint /v1/completions \ --num-prompts 4 \ --request-rate 1 \ --metric_percentiles '50,90,95,99' \ --goodput ttft:5000 tpot:250 \ --max-concurrency 4 \ --random-input-len 3500 \ --random-output-len 1500 \ --dataset-name random \ --ignore-eos --trust-remote-code \ --save-result \ **0.7.4dev122** perf result: Starting initial single prompt test run... Initial test run completed. Starting main benchmark run... Traffic request rate: 23.0 Burstiness factor: 1.0 (Poisson process) Maximum request concurrency: 23 100%|██████████| 92/92 [05:55<00:00, 3.86s/it] ============ Serving Benchmark Result ============ Successful requests: 92 Benchmark duration (s): 355.48 Total input tokens: 322000 Total generated tokens: 138000 Request throughput (req/s): 0.26 Request goodput (req/s): 0.22 Output token throughput (tok/...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: [Performance]: 0.8.1 vs 0.7.4dev122 R1 H20 performance benchmark test，0.8.1 What is the reason for the 14% performance improvement(throughput tokens/s) performance ### Proposal to improve performance _No response_ ### R...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ical optimizations python3 /root/vllm/benchmarks/benchmark_serving.py --backend vllm \ --model /data00/models/DeepSeek-R1 \ --base-url http://127.0.0.1:8000 \ --endpoint /v1/completions \ --num-prompts 4 \ --request-rat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: mance _No response_ ### Report of performance regression perf test R1 model: input/output=3500/1500, on the same host, vllm 0.8.1 throughtput（total） improve 14%, v0.8.1 why? What are the technical optimizations python3...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: --endpoint /v1/completions \ --num-prompts 4 \ --request-rate 1 \ --metric_percentiles '50,90,95,99' \ --goodput ttft:5000 tpot:250 \ --max-concurrency 4 \ --random-input-len 3500 \ --random-output-len 1500 \

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
