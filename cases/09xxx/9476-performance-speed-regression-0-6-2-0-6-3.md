# vllm-project/vllm#9476: [Performance]: speed regression 0.6.2 => 0.6.3?

| 字段 | 值 |
| --- | --- |
| Issue | [#9476](https://github.com/vllm-project/vllm/issues/9476) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: speed regression 0.6.2 => 0.6.3?

### Issue 正文摘录

### Report of performance regression Using your benchmark ``` git clone https://github.com/vllm-project/vllm cd vllm/benchmarks wget https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/resolve/main/ShareGPT_V3_unfiltered_cleaned_split.json mkdir results python benchmark_serving.py \ --backend vllm \ --model meta-llama/Meta-Llama-3-8B-Instruct \ --dataset-name sharegpt \ --dataset-path ShareGPT_V3_unfiltered_cleaned_split.json \ --port 9999 \ --save-result \ --result-dir results \ --result-filename test.json \ --num-prompts 2000 \ --request-rate inf \ --seed 42 ``` vllm==0.6.2 ``` python -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 --port 9999 \ --model meta-llama/Meta-Llama-3-8B-Instruct \ --tokenizer meta-llama/Meta-Llama-3-8B-Instruct \ --dtype=bfloat16 \ --seed 42 \ --num-scheduler-steps 8 \ --disable-log-requests \ -tp 2 ``` ``` ============ Serving Benchmark Result ============ Successful requests: 2000 Benchmark duration (s): 37.56 Total input tokens: 453502 Total generated tokens: 377235 Request throughput (req/s): 53.24 Output token throughput (tok/s): 10042.39 Total Token throughput (tok/s): 22115.08 ---------------Time to First Token------...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: [Performance]: speed regression 0.6.2 => 0.6.3? performance;stale ### Report of performance regression Using your benchmark ``` git clone https://github.com/vllm-project/vllm cd vllm/benchmarks wget https://huggingface....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: B-Instruct \ --tokenizer meta-llama/Meta-Llama-3-8B-Instruct \ --dtype=bfloat16 \ --seed 42 \ --num-scheduler-steps 8 \ --disable-log-requests \ -tp 2 ``` ``` ============ Serving Benchmark Result ============ Successfu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: one https://github.com/vllm-project/vllm cd vllm/benchmarks wget https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/resolve/main/ShareGPT_V3_unfiltered_cleaned_split.json mkdir results python benc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Performance]: speed regression 0.6.2 => 0.6.3? performance;stale ### Report of performance regression Using your benchmark ``` git clone https://github.com/vllm-project/vllm cd vllm/benchmarks wget https://huggingface....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: red_cleaned_split.json mkdir results python benchmark_serving.py \ --backend vllm \ --model meta-llama/Meta-Llama-3-8B-Instruct \ --dataset-name sharegpt \ --dataset-path ShareGPT_V3_unfiltered_cleaned_split.json \ --po...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
