# vllm-project/vllm#27194: [Bug]: vLLM crashes (EngineDeadError) during high‑concurrency benchmark

| 字段 | 值 |
| --- | --- |
| Issue | [#27194](https://github.com/vllm-project/vllm/issues/27194) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;fp8;quantization;sampling |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM crashes (EngineDeadError) during high‑concurrency benchmark

### Issue 正文摘录

### Your current environment Running docker image `vllm-openai:v0.10.2` ### 🐛 Describe the bug Running on 8xB200 with `VLLM_USE_DEEP_GEMM=1` and following params: ``` │ (APIServer pid=1) INFO 10-20 03:21:02 [utils.py:328] non-default args: {'model_tag': 's3://Qwen3-Coder-480B-A35B-Instruct-FP8', 'host': '0.0.0.0', 'enable_auto_tool_choice': True, 'tool_call_parser': 'qwen3_coder', 'max_model_len': 131072, 'served_model_name': ['Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8'], 'load_format': 'runai_streamer', 'tensor_parallel_size': 8, 'enable_expert_parallel': True, 'gpu_memory_utilization': │ │ 0.95, 'enable_prefix_caching': True} ```│ (APIServer pid=1) INFO 10-20 03:21:02 [utils.py:328] non-default args: {'model_tag': 's3://Qwen3-Coder-480B-A35B-Instruct-FP8', 'host': '0.0.0.0', 'enable_auto_tool_choice': True, 'tool_call_parser': 'qwen3_coder', 'max_model_len': 131072, 'served_model_name': ['Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8'], 'load_format': 'runai_streamer', 'tensor_parallel_size': 8, 'enable_expert_parallel': True, 'gpu_memory_utilization': │ ``` While performing some load tests using vllm `benchmark_serving.py`: ``` --dataset-name random \ --random-input-len 64512 \ --rando...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: 59.0 tokens/s, Avg generation throughput: 9.4 tokens/s, Running: 8 reqs, Waiting: 1 reqs, GPU KV cache usage: 12.8%, Prefix cache hit rate: 21.2% (APIServer pid=1) INFO: 100.80.2.232:55860 - "GET /metrics HTTP/1.1" 200...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ing high‑concurrency benchmark bug ### Your current environment Running docker image `vllm-openai:v0.10.2` ### 🐛 Describe the bug Running on 8xB200 with `VLLM_USE_DEEP_GEMM=1` and following params: ``` │ (APIServer pid=...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: 28] non-default args: {'model_tag': 's3://Qwen3-Coder-480B-A35B-Instruct-FP8', 'host': '0.0.0.0', 'enable_auto_tool_choice': True, 'tool_call_parser': 'qwen3_coder', 'max_model_len': 131072, 'served_model_name': ['Qwen/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: (APIServer pid=1) INFO 10-20 03:21:02 [utils.py:328] non-default args: {'model_tag': 's3://Qwen3-Coder-480B-A35B-Instruct-FP8', 'host': '0.0.0.0', 'enable_auto_tool_choice': True, 'tool_call_parser': 'qwen3_coder', 'max...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: docker image `vllm-openai:v0.10.2` ### 🐛 Describe the bug Running on 8xB200 with `VLLM_USE_DEEP_GEMM=1` and following params: ``` │ (APIServer pid=1) INFO 10-20 03:21:02 [utils.py:328] non-default args: {'model_tag': 's...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
