# vllm-project/vllm#3297:  The benchmark_serving results using 8 GPUs are worse than those using 4 GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#3297](https://github.com/vllm-project/vllm/issues/3297) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

>  The benchmark_serving results using 8 GPUs are worse than those using 4 GPUs

### Issue 正文摘录

hardware: L40 * 8 OS:ubuntu 22.04 vllm：0.3.3 ### 8 GPU: server side: `python -m vllm.entrypoints.api_server --model /path/llama7b --swap-space 16 --disable-log-requests --tensor-parallel-size 8 --trust-remote-code --gpu-memory-utilization 0.95` client side: `python benchmark_serving.py --backend vllm --model /path/llama7b --dataset ShareGPT_V3_unfiltered_cleaned_split.json --request-rate 10 --trust-remote-code --num-prompts 100` result: > Successful requests: 100 > Benchmark duration: 29.521190 s > Total input tokens: 25900 > Total generated tokens: 22632 > Request throughput: 3.39 requests/s > Input token throughput: 877.34 tokens/s > Output token throughput: 766.64 tokens/s > Mean TTFT: 119.86 ms > Median TTFT: 96.76 ms > P99 TTFT: 299.82 ms > Mean TPOT: 49.34 ms > Median TPOT: 44.47 ms > P99 TPOT: 98.98 ms ### 4 GPU: server side: `python -m vllm.entrypoints.api_server --model /path/llama7b --swap-space 16 --disable-log-requests --tensor-parallel-size 4 --trust-remote-code --gpu-memory-utilization 0.95` client side(same as 8GPU): `python benchmark_serving.py --backend vllm --model /path/llama7b --dataset ShareGPT_V3_unfiltered_cleaned_split.json --request-rate 10 --trust-remote-...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: The benchmark_serving results using 8 GPUs are worse than those using 4 GPUs hardware: L40 * 8 OS:ubuntu 22.04 vllm：0.3.3 ### 8 GPU: server side: `python -m vllm.entrypoints.api_server --model /path/llama7b --swap-
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ：0.3.3 ### 8 GPU: server side: `python -m vllm.entrypoints.api_server --model /path/llama7b --swap-space 16 --disable-log-requests --tensor-parallel-size 8 --trust-remote-code --gpu-memory-utilization 0.95` client side:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: gpu-memory-utilization 0.95` client side: `python benchmark_serving.py --backend vllm --model /path/llama7b --dataset ShareGPT_V3_unfiltered_cleaned_split.json --request-rate 10 --trust-remote-code --num-prompts 100` re...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: can I improve performance with 8 GPUs? Any suggestions are greatly appreciated. thanks a lot!
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: trypoints.api_server --model /path/llama7b --swap-space 16 --disable-log-requests --tensor-parallel-size 8 --trust-remote-code --gpu-memory-utilization 0.95` client side: `python benchmark_serving.py --backend vllm --mo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
