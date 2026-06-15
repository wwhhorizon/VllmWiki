# vllm-project/vllm#6531: [Bug]: inter-token latency is lower than TPOT in serving benchmark result

| 字段 | 值 |
| --- | --- |
| Issue | [#6531](https://github.com/vllm-project/vllm/issues/6531) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: inter-token latency is lower than TPOT in serving benchmark result

### Issue 正文摘录

### Your current environment v0.5.2. vLLM env is not an issue so I will just skip the collection process ### 🐛 Describe the bug I am running benchmark tests and notice one potential problem. Seems the inter-token latency is lower than TPOT. Basically, inter-token latency takes TTFT into the consideration and should be higher than TPOT. However the data shows different result. I have not looked at the code yet and I will try to figure this out ```text root@fb5250e2ae4c:/workspace# python3 vllm/benchmarks/benchmark_serving.py --backend vllm --dataset-name sharegpt --dataset-path ./ShareGPT_V3_unfiltered_cleaned_split.json --model meta-llama/Llama-2-7b-chat-hf --num-prompts 200 --endpoint /v1/completions --tokenizer meta-llama/Llama-2-7b-chat-hf --save-result 2>&1 | tee benchmark_serving.txt Namespace(backend='vllm', base_url=None, host='localhost', port=8000, endpoint='/v1/completions', dataset=None, dataset_name='sharegpt', dataset_path='./ShareGPT_V3_unfiltered_cleaned_split.json', model='meta-llama/Llama-2-7b-chat-hf', tokenizer='meta-llama/Llama-2-7b-chat-hf', best_of=1, use_beam_search=False, num_prompts=200, sharegpt_output_len=None, sonnet_input_len=550, sonnet_output_len=150...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Bug]: inter-token latency is lower than TPOT in serving benchmark result bug;stale ### Your current environment v0.5.2. vLLM env is not an issue so I will just skip the collection process ### 🐛 Describe the bug I am ru...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: gpt --dataset-path ./ShareGPT_V3_unfiltered_cleaned_split.json --model meta-llama/Llama-2-7b-chat-hf --num-prompts 200 --endpoint /v1/completions --tokenizer meta-llama/Llama-2-7b-chat-hf --save-result 2>&1 | tee benchm...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: tokenizer='meta-llama/Llama-2-7b-chat-hf', best_of=1, use_beam_search=False, num_prompts=200, sharegpt_output_len=None, sonnet_input_len=550, sonnet_output_len=150, sonnet_prefix_len=200, random_input_len=1024, random_o...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: : inter-token latency is lower than TPOT in serving benchmark result bug;stale ### Your current environment v0.5.2. vLLM env is not an issue so I will just skip the collection process ### 🐛 Describe the bug I am running...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 250e2ae4c:/workspace# python3 vllm/benchmarks/benchmark_serving.py --backend vllm --dataset-name sharegpt --dataset-path ./ShareGPT_V3_unfiltered_cleaned_split.json --model meta-llama/Llama-2-7b-chat-hf --num-prompts 20...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
