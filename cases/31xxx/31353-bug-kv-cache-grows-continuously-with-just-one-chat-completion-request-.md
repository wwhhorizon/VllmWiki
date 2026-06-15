# vllm-project/vllm#31353: [Bug]: KV Cache grows continuously with just one chat completion request using meta-llama/Llama-3.2-1B on L40 GPU with Flash Attention and finally completed after 10 minutes

| 字段 | 值 |
| --- | --- |
| Issue | [#31353](https://github.com/vllm-project/vllm/issues/31353) |
| 状态 | closed |
| 标签 | bug;help wanted;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KV Cache grows continuously with just one chat completion request using meta-llama/Llama-3.2-1B on L40 GPU with Flash Attention and finally completed after 10 minutes

### Issue 正文摘录

### Your current environment (APIServer pid=324144) INFO 12-25 13:36:00 [loggers.py:248] Engine 000: Avg prompt throughput: 3.9 tokens/s, Avg generation throughput: 93.1 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.1%, Prefix cache hit rate: 18.8% (APIServer pid=324144) INFO 12-25 13:36:10 [loggers.py:248] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 213.0 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.3%, Prefix cache hit rate: 18.8% (APIServer pid=324144) INFO 12-25 13:36:20 [loggers.py:248] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 206.3 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.4%, Prefix cache hit rate: 18.8% (APIServer pid=324144) INFO 12-25 13:36:30 [loggers.py:248] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 201.5 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.6%, Prefix cache hit rate: 18.8% (APIServer pid=324144) INFO 12-25 13:36:40 [loggers.py:248] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 197.6 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: KV Cache grows continuously with just one chat completion request using meta-llama/Llama-3.2-1B on L40 GPU with Flash Attention and finally completed after 10 minutes bug;help wanted;stale ### Your current enviro...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: _chat_template_llama3.1_json.jinja Client Code ``` pyhon from openai import OpenAI client = OpenAI( base_url="http://localhost:8000/v1", api_key="token-abc123" ) completion = client.chat.completions.create( model="meta-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ne chat completion request using meta-llama/Llama-3.2-1B on L40 GPU with Flash Attention and finally completed after 10 minutes bug;help wanted;stale ### Your current environment (APIServer pid=324144) INFO 12-25 13:36:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: d " ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: KV Cache grows continuously with just one chat completion request using meta-llama/Llama-3.2-1B on L40 GPU with Flash Attention and finally completed after 10 minutes bug;help wanted;stale ### Your current enviro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
