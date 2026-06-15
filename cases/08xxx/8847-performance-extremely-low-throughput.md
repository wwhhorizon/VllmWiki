# vllm-project/vllm#8847: [Performance]: Extremely low throughput

| 字段 | 值 |
| --- | --- |
| Issue | [#8847](https://github.com/vllm-project/vllm/issues/8847) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;import_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Extremely low throughput

### Issue 正文摘录

### Proposal to improve performance Hi all, I just started a vLLM server instance as follows: `python3 -m vllm.entrypoints.openai.api_server --model meta-llama/Meta-Llama-3-8B-Instruct --enforce-eager --max-num-seqs 16` However, the throughput seems to be extremely low (0.8, 0.9 token/s): ``` INFO: 2.36.8.92:56164 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO 09-26 11:35:23 engine.py:288] Added request chat-cc6296ad51b74d88bf17ba75459c06aa. INFO 09-26 11:35:25 metrics.py:351] Avg prompt throughput: 2.3 tokens/s, Avg generation throughput: 0.2 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.1%, CPU KV cache usage: 0.0%. INFO 09-26 11:35:31 metrics.py:351] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.8 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.2%, CPU KV cache usage: 0.0%. INFO 09-26 11:35:37 metrics.py:351] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.8 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.2%, CPU KV cache usage: 0.0%. INFO 09-26 11:35:43 metrics.py:351] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: prompt: ' user \n\nHere is the query:\nHey how are you?\n\nCreate a concise, 3-5 word phrase with an emoji as a title for the previous query. Suitable Emojis for the summary can be used to enhance understanding but avoi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: EXT.\n\nExamples of titles:\n📉 Stock Market Trends\n🍪 Perfect Chocolate Chip Recipe\nEvolution of Music Streaming\nRemote Work Productivity Tips\nArtificial Intelligence in Healthcare\n🎮 Video Game Development Insights...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: r instance as follows: `python3 -m vllm.entrypoints.openai.api_server --model meta-llama/Meta-Llama-3-8B-Instruct --enforce-eager --max-num-seqs 16` However, the throughput seems to be extremely low (0.8, 0.9 token/s):...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: at/completions HTTP/1.1" 200 OK INFO 09-26 11:35:23 engine.py:288] Added request chat-cc6296ad51b74d88bf17ba75459c06aa. INFO 09-26 11:35:25 metrics.py:351] Avg prompt throughput: 2.3 tokens/s, Avg generation throughput:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Performance]: Extremely low throughput performance ### Proposal to improve performance Hi all, I just started a vLLM server instance as follows: `python3 -m vllm.entrypoints.openai.api_server --model meta-llama/Meta-Ll...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
