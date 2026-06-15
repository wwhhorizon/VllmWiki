# vllm-project/vllm#14775: [Usage]: How to add Sampling Parameters (n and best_of ) for benchmark_serving.py

| 字段 | 值 |
| --- | --- |
| Issue | [#14775](https://github.com/vllm-project/vllm/issues/14775) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to add Sampling Parameters (n and best_of ) for benchmark_serving.py

### Issue 正文摘录

### Your current environment python3 /vllm/benchmarks/benchmark_serving.py --host localhost --backend openai \ --port 80 --model meta-llama/Llama-3.2-3B-Instruct \ --dataset-name random --max-concurrency 2048 --num-prompts 10240 \ --random-input-len 20 --random-output-len 256 \ --percentile-metrics e2el --profile --save-result \ --metric-percentiles 95 --endpoint '/vllm-server/v1/completions' --request-rate 40 --burstiness 0.5 ### How would you like to use vllm I want to run inference by using Sampling Parameters. I don't know how to integrate it with vllm serving benchmark. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Usage]: How to add Sampling Parameters (n and best_of ) for benchmark_serving.py usage;stale ### Your current environment python3 /vllm/benchmarks/benchmark_serving.py --host localhost --backend openai \ --port 80 --mo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: benchmark_serving.py --host localhost --backend openai \ --port 80 --model meta-llama/Llama-3.2-3B-Instruct \ --dataset-name random --max-concurrency 2048 --num-prompts 10240 \ --random-input-len 20 --random-output-len...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: add Sampling Parameters (n and best_of ) for benchmark_serving.py usage;stale ### Your current environment python3 /vllm/benchmarks/benchmark_serving.py --host localhost --backend openai \ --port 80 --model meta-llama/L...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: onment python3 /vllm/benchmarks/benchmark_serving.py --host localhost --backend openai \ --port 80 --model meta-llama/Llama-3.2-3B-Instruct \ --dataset-name random --max-concurrency 2048 --num-prompts 10240 \ --random-i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rk. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
