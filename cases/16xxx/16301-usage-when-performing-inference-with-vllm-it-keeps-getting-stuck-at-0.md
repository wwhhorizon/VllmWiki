# vllm-project/vllm#16301: [Usage]: When performing inference with vLLM, it keeps getting stuck at 0%.

| 字段 | 值 |
| --- | --- |
| Issue | [#16301](https://github.com/vllm-project/vllm/issues/16301) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: When performing inference with vLLM, it keeps getting stuck at 0%.

### Issue 正文摘录

### Your current environment NFO 04-09 02:05:52 [loader.py:447] Loading weights took 33.15 seconds INFO 04-09 02:05:53 [gpu_model_runner.py:1273] Model loading took 61.0374 GiB and 33.525153 seconds INFO 04-09 02:06:09 [backends.py:416] Using cache directory: /root/.cache/vllm/torch_compile_cache/e8c79b34a0/rank_0_0 for vLLM's torch.compile INFO 04-09 02:06:09 [backends.py:426] Dynamo bytecode transform time: 16.61 s INFO 04-09 02:06:10 [backends.py:115] Directly load the compiled graph for shape None from the cache INFO 04-09 02:06:25 [monitor.py:33] torch.compile takes 16.61 s in total INFO 04-09 02:06:28 [kv_cache_utils.py:578] GPU KV cache size: 16,064 tokens INFO 04-09 02:06:28 [kv_cache_utils.py:581] Maximum concurrency for 10,000 tokens per request: 1.61x INFO 04-09 02:07:01 [gpu_model_runner.py:1608] Graph capturing finished in 33 secs, took 3.17 GiB INFO 04-09 02:07:01 [core.py:162] init engine (profile, create kv cache, warmup model) took 68.69 seconds Processed prompts: 0%| | 0/1 [00:00<?, ?it/s, est. speed input: 0.00 toks/s, output: 0.00 toks/s] ### How would you like to use vllm ### Before submitting a new issue... - [x] Make sure you already searched for relevant is...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: in 33 secs, took 3.17 GiB INFO 04-09 02:07:01 [core.py:162] init engine (profile, create kv cache, warmup model) took 68.69 seconds Processed prompts: 0%| | 0/1 [00:00<?, ?it/s, est. speed input: 0.00 toks/s, output: 0....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel loading took 61.0374 GiB and 33.525153 seconds INFO 04-09 02:06:09 [backends.py:416] Using cache directory: /root/.cache/vllm/torch_compile_cache/e8c79b34a0/rank_0_0 for vLLM's torch.compile INFO 04-09 02:06:09 [ba...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 2:06:09 [backends.py:416] Using cache directory: /root/.cache/vllm/torch_compile_cache/e8c79b34a0/rank_0_0 for vLLM's torch.compile INFO 04-09 02:06:09 [backends.py:426] Dynamo bytecode transform time: 16.61 s INFO 04-0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: llm ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: e takes 16.61 s in total INFO 04-09 02:06:28 [kv_cache_utils.py:578] GPU KV cache size: 16,064 tokens INFO 04-09 02:06:28 [kv_cache_utils.py:581] Maximum concurrency for 10,000 tokens per request: 1.61x INFO 04-09 02:07...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
