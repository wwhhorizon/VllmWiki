# vllm-project/vllm#30320: [Bug]: v1 scheduler assert num_new_tokens > 0

| 字段 | 值 |
| --- | --- |
| Issue | [#30320](https://github.com/vllm-project/vllm/issues/30320) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v1 scheduler assert num_new_tokens > 0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I encountered an `AssertionError` in `vllm/v1/core/sched/scheduler.py` while running a benchmark script with prefix caching and KV transfer enabled. It appears that when a request matches the full prefix (likely due to prefix caching or KV transfer), `num_computed_tokens` equals `request.num_tokens`, causing `num_new_tokens` to be 0. The scheduler currently asserts that `num_new_tokens > 0` for waiting requests, which leads to this crash. ### Reproduction Command ```bash export LMCACHE_MAX_LOCAL_CPU_SIZE=100.0 export LMCACHE_LOG_LEVEL=WARNING python3 benchmarks/benchmark_prefix_caching.py \ --model Qwen/Qwen3-14B \ --dataset-path /xxx/ShareGPT_V3_unfiltered_cleaned_split.json \ --enable-prefix-caching \ --gpu-memory-utilization 0.7 \ --compilation-config '{"level": 0, "cudagraph_mode": "NONE"}' \ --kv-transfer-config '{"kv_connector":"LMCacheConnectorV1", "kv_role":"kv_both"}' \ --num-prompts 500 \ --repeat-count 3 \ --input-length-range 512:2048 \ --output-len 1 ``` ### Traceback ```text (EngineCore_DP0 pid=1325938) Traceback (most recent call last): (EngineCore_DP0 pid=1325938) File "/home/wk/.local/share/uv/python/cpython-3.12...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: v1 scheduler assert num_new_tokens > 0 bug ### Your current environment ### 🐛 Describe the bug I encountered an `AssertionError` in `vllm/v1/core/sched/scheduler.py` while running a benchmark script with prefix c...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory cuda;operator;sampling;triton build_err...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: E_LOG_LEVEL=WARNING python3 benchmarks/benchmark_prefix_caching.py \ --model Qwen/Qwen3-14B \ --dataset-path /xxx/ShareGPT_V3_unfiltered_cleaned_split.json \ --enable-prefix-caching \ --gpu-memory-utilization 0.7 \ --co...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: \ --gpu-memory-utilization 0.7 \ --compilation-config '{"level": 0, "cudagraph_mode": "NONE"}' \ --kv-transfer-config '{"kv_connector":"LMCacheConnectorV1", "kv_role":"kv_both"}' \ --num-prompts 500 \ --repeat-count 3 \...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: an `AssertionError` in `vllm/v1/core/sched/scheduler.py` while running a benchmark script with prefix caching and KV transfer enabled. It appears that when a request matches the full prefix (likely due to prefix caching...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
