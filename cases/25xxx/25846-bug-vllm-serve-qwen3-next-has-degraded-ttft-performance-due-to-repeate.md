# vllm-project/vllm#25846: [Bug]: vllm serve qwen3-next has degraded TTFT/performance due to repeated huggingface api calls

| 字段 | 值 |
| --- | --- |
| Issue | [#25846](https://github.com/vllm-project/vllm/issues/25846) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm serve qwen3-next has degraded TTFT/performance due to repeated huggingface api calls

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug NOTE: not sure if this should be labeled bug or performance I was running normal benchmarks for Qwen3-Next on v0.10.2 when I noticed some really bad performance issues that I've pinned down to repeated calls to `from_pretrained` (makes a costly huggingface API call). My setup is 2x H200, here are my commands: ### Server: ``` vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct \ --port 8000 \ --host 0.0.0.0 \ --no-enable-prefix-caching \ --tensor-parallel-size 2 ``` ### Benchmark: ``` vllm bench serve \ --backend vllm \ --model Qwen/Qwen3-Next-80B-A3B-Instruct \ --endpoint /v1/chat/completions \ --endpoint-type openai-chat \ --dataset-name random \ --random-input-len 1024 \ --random-output-len 128 \ --num-prompts 1000 \ --max-concurrency 32 ``` This gives really terrible numbers due to super long TTFT: ``` ============ Serving Benchmark Result ============ Successful requests: 1000 Maximum request concurrency: 32 Benchmark duration (s): 1151.29 Total input tokens: 1021255 Total generated tokens: 127926 Request throughput (req/s): 0.87 Output token throughput (tok/s): 111.12 Total Token throughput (tok/s): 998.17 ---------------Time to Fir...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: sure if this should be labeled bug or performance I was running normal benchmarks for Qwen3-Next on v0.10.2 when I noticed some really bad performance issues that I've pinned down to repeated calls to `from_pretrained`...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: vllm serve qwen3-next has degraded TTFT/performance due to repeated huggingface api calls bug ### Your current environment ### 🐛 Describe the bug NOTE: not sure if this should be labeled bug or performance I was...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: found that the TTFT is really long due to api server pre-processing, specifically with getting the chat template. Each call to [`cached_get_processor`](https://github.com/vllm-project/vllm/blob/0307428d65acf5cf1a73a70a7...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: my initial thought is to handle the error case for `get_processor` in a smarter way that still "caches" the error result so that this function is only run once, instead of repeatedly making HF api calls with the same ex...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: --tensor-parallel-size 2 ``` ### Benchmark: ``` vllm bench serve \ --backend vllm \ --model Qwen/Qwen3-Next-80B-A3B-Instruct \ --endpoint /v1/chat/completions \ --endpoint-type openai-chat \ --dataset-name random \ --ra...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
