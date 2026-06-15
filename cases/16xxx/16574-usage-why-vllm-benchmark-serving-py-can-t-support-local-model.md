# vllm-project/vllm#16574: [Usage]: Why vllm benchmark_serving.py can't support local model?

| 字段 | 值 |
| --- | --- |
| Issue | [#16574](https://github.com/vllm-project/vllm/issues/16574) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Why vllm benchmark_serving.py can't support local model?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm python3 vllm/benchmarks/benchmark_serving.py \ --backend vllm \ --model NousResearch/Hermes-3-Llama-3.1-8B \ --endpoint /v1/completions \ --dataset-name sharegpt \ --dataset-path /ShareGPT_V3_unfiltered_cleaned_split.json \ --num-prompts 10 Why vllm can only suppert hf type model? What if I want to use my local model file path to do benchmark test? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: Why vllm benchmark_serving.py can't support local model? usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm python3 vllm/benchmarks/benchmark...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Usage]: Why vllm benchmark_serving.py can't support local model? usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm python3 vllm/benchmarks/benchmark...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: you like to use vllm python3 vllm/benchmarks/benchmark_serving.py \ --backend vllm \ --model NousResearch/Hermes-3-Llama-3.1-8B \ --endpoint /v1/completions \ --dataset-name sharegpt \ --dataset-path /ShareGPT_V3_unfilt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: m/benchmarks/benchmark_serving.py \ --backend vllm \ --model NousResearch/Hermes-3-Llama-3.1-8B \ --endpoint /v1/completions \ --dataset-name sharegpt \ --dataset-path /ShareGPT_V3_unfiltered_cleaned_split.json \ --num-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
