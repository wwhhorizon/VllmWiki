# vllm-project/vllm#17586: [Feature]: benchmarks for vllm,  it should support OpenAI Chat Completions API

| 字段 | 值 |
| --- | --- |
| Issue | [#17586](https://github.com/vllm-project/vllm/issues/17586) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: benchmarks for vllm,  it should support OpenAI Chat Completions API

### Issue 正文摘录

### 🚀 The feature, motivation and pitch https://github.com/vllm-project/vllm/tree/main/benchmarks. # download dataset # wget https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/resolve/main/ShareGPT_V3_unfiltered_cleaned_split.json python3 vllm/benchmarks/benchmark_serving.py \ --backend vllm \ --model NousResearch/Hermes-3-Llama-3.1-8B \ --endpoint /v1/completions \ --dataset-name sharegpt \ --dataset-path /ShareGPT_V3_unfiltered_cleaned_split.json \ --num-prompts 10 benchmarks should support OpenAI Chat Completions API 。like: --endpoint /v1/chat/completions ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: llm-project/vllm/tree/main/benchmarks. # download dataset # wget https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/resolve/main/ShareGPT_V3_unfiltered_cleaned_split.json python3 vllm/benchmarks/b...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: chmarks for vllm, it should support OpenAI Chat Completions API feature request;stale ### 🚀 The feature, motivation and pitch https://github.com/vllm-project/vllm/tree/main/benchmarks. # download dataset # wget https://...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Feature]: benchmarks for vllm, it should support OpenAI Chat Completions API feature request;stale ### 🚀 The feature, motivation and pitch https://github.com/vllm-project/vllm/tree/main/benchmarks. # download dataset #...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ed_cleaned_split.json python3 vllm/benchmarks/benchmark_serving.py \ --backend vllm \ --model NousResearch/Hermes-3-Llama-3.1-8B \ --endpoint /v1/completions \ --dataset-name sharegpt \ --dataset-path /ShareGPT_V3_unfil...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: m/benchmarks/benchmark_serving.py \ --backend vllm \ --model NousResearch/Hermes-3-Llama-3.1-8B \ --endpoint /v1/completions \ --dataset-name sharegpt \ --dataset-path /ShareGPT_V3_unfiltered_cleaned_split.json \ --num-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
