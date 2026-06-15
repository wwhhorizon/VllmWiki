# vllm-project/vllm#40585: [Bug]: qwen3.5 can not use --decode-context-parallel-size with --enable-prefix-caching

| 字段 | 值 |
| --- | --- |
| Issue | [#40585](https://github.com/vllm-project/vllm/issues/40585) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;scheduler_memory;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | cache;cuda;moe;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: qwen3.5 can not use --decode-context-parallel-size with --enable-prefix-caching

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug - vllm-0.18.0 - 8*910B - `-tp 8 -dcp` 4 with `--enable-prefix-caching --mamba-cache-mode align` ``` vllm serve /dev/shm/Qwen3.5-35B-A3B --served-model-name default_model --enable-prompt-tokens-details --enable-mfu-metrics --max-num-batched-tokens=8K --max-num-seqs 128 --reasoning-parser qwen3 --enable-auto-tool-choice --tool-call-parser qwen3_xml --enable-prefix-caching --mamba-cache-mode align --enable-expert-parallel --load-format runai_streamer --port 8000 --host :: --tensor-parallel-size 8 -dcp 4 ``` the error message ``` (Worker_TP0_DCP0_EP0 pid=64160) INFO 04-22 11:54:08 [monitor.py:48] torch.compile and initial profiling/warmup run together took 23.82 s in total (Worker_TP0_DCP0_EP0 pid=64160) INFO 04-22 11:54:12 [worker.py:357] Available KV cache memory: 44.77 GiB (EngineCore pid=64025) INFO 04-22 11:54:12 [kv_cache_utils.py:1308] Multiplying the GPU KV cache size by the cp_world_size 4 (pcp_world_size 1 * dcp_world_size 4). (EngineCore pid=64025) INFO 04-22 11:54:12 [kv_cache_utils.py:1316] GPU KV cache size: 4,638,720 tokens (EngineCore pid=64025) INFO 04-22 11:54:12 [kv_cache_utils.py:1321] Maximum concurrency for 262,...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: qwen3.5 can not use --decode-context-parallel-size with --enable-prefix-caching bug ### Your current environment ### 🐛 Describe the bug - vllm-0.18.0 - 8*910B - `-tp 8 -dcp` 4 with `--enable-prefix-caching --mamb...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Worker_TP0_DCP0_EP0 pid=64160) INFO 04-22 11:54:08 [monitor.py:48] torch.compile and initial profiling/warmup run together took 23.82 s in total (Worker_TP0_DCP0_EP0 pid=64160) INFO 04-22 11:54:12 [worker.py:357] Availa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: qwen3.5 can not use --decode-context-parallel-size with --enable-prefix-caching bug ### Your current environment ### 🐛 Describe the bug - vllm-0.18.0 - 8*910B - `-tp 8 -dcp` 4 with `--enable-prefix-caching --mamb...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: pid=64160) INFO 04-22 11:54:08 [monitor.py:48] torch.compile and initial profiling/warmup run together took 23.82 s in total (Worker_TP0_DCP0_EP0 pid=64160) INFO 04-22 11:54:12 [worker.py:357] Available KV cache memory:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: by the cp_world_size 4 (pcp_world_size 1 * dcp_world_size 4). Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 100%|███████████████████████████████████████| 13/13 [00:09<00:00, 1.32it/s] (Worker_TP0_DCP0_EP0 pid...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
