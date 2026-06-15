# vllm-project/vllm#20264: [Performance]: vllm taking high startup time even with persisting the torch compile between pod scaling

| 字段 | 值 |
| --- | --- |
| Issue | [#20264](https://github.com/vllm-project/vllm/issues/20264) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support |
| 子分类 | cold_start |
| Operator 关键词 | cache;cuda |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: vllm taking high startup time even with persisting the torch compile between pod scaling

### Issue 正文摘录

### Proposal to improve performance These are the logs: INFO 06-19 23:05:01 [loader.py:447] Loading weights took 0.69 seconds INFO 06-19 23:05:01 [gpu_model_runner.py:1273] Model loading took 3.4213 GiB and 0.902026 seconds INFO 06-19 23:05:09 [backends.py:416] Using cache directory: /root/.cache/vllm/torch_compile_cache/8715b0a56a/rank_0_0 for vLLM's torch.compile INFO 06-19 23:05:09 [backends.py:426] Dynamo bytecode transform time: **7.51 s** INFO 06-19 23:05:09 [backends.py:115] Directly load the compiled graph for shape None from the cache INFO 06-19 23:05:18 [monitor.py:33] torch.compile takes **7.51 s** in total INFO 06-19 23:05:18 [kv_cache_utils.py:578] GPU KV cache size: 613,024 tokens INFO 06-19 23:05:18 [kv_cache_utils.py:581] Maximum concurrency for 131,072 tokens per request: 4.68x INFO 06-19 23:05:35 [gpu_model_runner.py:1608] Graph capturing finished in **17 secs**, took 0.48 GiB INFO 06-19 23:05:35 [core.py:162] init engine (profile, create kv cache, warmup model) took **34.11 seconds** torch_compile_cache is being resued between pod startups. But cuda graph capturing takes 18s and even though the init engine shows 30.93s, the reponse is received after 59s in total...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: rformance]: vllm taking high startup time even with persisting the torch compile between pod scaling performance;stale ### Proposal to improve performance These are the logs: INFO 06-19 23:05:01 [loader.py:447] Loading...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: seconds** torch_compile_cache is being resued between pod startups. But cuda graph capturing takes 18s and even though the init engine shows 30.93s, the reponse is received after 59s in total. There's a loss of ~30s, wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: *17 secs**, took 0.48 GiB INFO 06-19 23:05:35 [core.py:162] init engine (profile, create kv cache, warmup model) took **34.11 seconds** torch_compile_cache is being resued between pod startups. But cuda graph capturing...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: oader.py:447] Loading weights took 0.69 seconds INFO 06-19 23:05:01 [gpu_model_runner.py:1273] Model loading took 3.4213 GiB and 0.902026 seconds INFO 06-19 23:05:09 [backends.py:416] Using cache directory: /root/.cache...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e even with persisting the torch compile between pod scaling performance;stale ### Proposal to improve performance These are the logs: INFO 06-19 23:05:01 [loader.py:447] Loading weights took 0.69 seconds INFO 06-19 23:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
