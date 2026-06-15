# vllm-project/vllm#19459: [Bug]: [v0.9.0][v1/core/single_type_kv_cache_manager.py] block_hash = block_hashes[i] IndexError: list index out of range while Load testing with ngram decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#19459](https://github.com/vllm-project/vllm/issues/19459) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [v0.9.0][v1/core/single_type_kv_cache_manager.py] block_hash = block_hashes[i] IndexError: list index out of range while Load testing with ngram decoding

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I created the endpoint by enabling the n-gram prompt lookup decoding option in vLLM v0.9.0 on H100. The arguments are as follows. ``` - args: --served-model-name - "deepseek-r1-0528-qwen3-8b" - "llm" --model - /data/models/DeepSeek-R1-0528-Qwen3-8B --tensor-parallel-size - "1" --load-format - "auto" --block-size - "32" --max-model-len - "65536" --max-seq-len-to-capture - "65536" --gpu-memory-utilization - "0.9" --trust-remote-code --prefix-caching-hash-algo - "sha256" --disable-log-requests --uvicorn-log-level - "warning" --reasoning-parser - "deepseek_r1" --speculative-config - '{"method": "ngram", "prompt_lookup_min": 3, "prompt_lookup_max": 5, "num_speculative_tokens": 7}' env: - name: OMP_NUM_THREADS value: "16" - name: VLLM_USE_V1 value: "1" ``` And when I load tested and maintained the load until the kv-cache utilization reached 100%, I got the following error message. ``` INFO 06-10 17:05:23 [loggers.py:116] Engine 000: Avg prompt throughput: 11348.1 tokens/s, Avg generation throughput: 1905.8 tokens/s, Running: 72 reqs, Waiting: 8 reqs, GPU KV cache usage: 100.0%, Prefix cache hit rate: 44.6% INFO 06-10 17:05:23 [metrics....

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: rror: list index out of range while Load testing with ngram decoding bug;stale ### Your current environment ### 🐛 Describe the bug I created the endpoint by enabling the n-gram prompt lookup decoding option in vLLM v0.9...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: .0 on H100. The arguments are as follows. ``` - args: --served-model-name - "deepseek-r1-0528-qwen3-8b" - "llm" --model - /data/models/DeepSeek-R1-0528-Qwen3-8B --tensor-parallel-size - "1" --load-format - "auto" --bloc...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding cache;cuda;operato...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: t by enabling the n-gram prompt lookup decoding option in vLLM v0.9.0 on H100. The arguments are as follows. ``` - args: --served-model-name - "deepseek-r1-0528-qwen3-8b" - "llm" --model - /data/models/DeepSeek-R1-0528-...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: value: "1" ``` And when I load tested and maintained the load until the kv-cache utilization reached 100%, I got the following error message. ``` INFO 06-10 17:05:23 [loggers.py:116] Engine 000: Avg prompt throughput: 1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
