# vllm-project/vllm#8531: [Bug]: benchmark_serving.py generates different numbers of tokens at different runs

| 字段 | 值 |
| --- | --- |
| Issue | [#8531](https://github.com/vllm-project/vllm/issues/8531) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: benchmark_serving.py generates different numbers of tokens at different runs

### Issue 正文摘录

### Your current environment 4xH100. ### Model Input Dumps _No response_ ### 🐛 Describe the bug When benchmarking the performance of vllm with `benchmark_serving.py`, it will generate different number of tokens at different runs. Code to launch vllm server ``` vllm serve meta-llama/Meta-Llama-3.1-70B-Instruct \ --disable-log-requests \ --tensor-parallel-size 4 ``` Code to run the benchmark ``` python benchmarks/benchmark_serving.py \ --backend vllm \ --model meta-llama/Meta-Llama-3.1-70B-Instruct\ --dataset-name sharegpt \ --dataset-path ShareGPT_V3_unfiltered_cleaned_split.json \ --request-rate 1 \ --num-prompts 200 \ --save-result ``` If I run the benchmark_serving.py script twice, the number of generated tokens is different for the two runs. The output of the first run: ``` ============ Serving Benchmark Result ============ Successful requests: 200 Benchmark duration (s): 203.41 Total input tokens: 42659 Total generated tokens: **38614** Request throughput (req/s): 0.98 Output token throughput (tok/s): 189.84 Total Token throughput (tok/s): 399.56 ---------------Time to First Token---------------- Mean TTFT (ms): 62.95 Median TTFT (ms): 64.68 P99 TTFT (ms): 141.49 -----Time per...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Bug]: benchmark_serving.py generates different numbers of tokens at different runs bug;stale ### Your current environment 4xH100. ### Model Input Dumps _No response_ ### 🐛 Describe the bug When benchmarking the perform...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rs of tokens at different runs bug;stale ### Your current environment 4xH100. ### Model Input Dumps _No response_ ### 🐛 Describe the bug When benchmarking the performance of vllm with `benchmark_serving.py`, it will gen...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: s at different runs bug;stale ### Your current environment 4xH100. ### Model Input Dumps _No response_ ### 🐛 Describe the bug When benchmarking the performance of vllm with `benchmark_serving.py`, it will generate diffe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: k_serving.py generates different numbers of tokens at different runs bug;stale ### Your current environment 4xH100. ### Model Input Dumps _No response_ ### 🐛 Describe the bug When benchmarking the performance of vllm wi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: to run the benchmark ``` python benchmarks/benchmark_serving.py \ --backend vllm \ --model meta-llama/Meta-Llama-3.1-70B-Instruct\ --dataset-name sharegpt \ --dataset-path ShareGPT_V3_unfiltered_cleaned_split.json \ --r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
