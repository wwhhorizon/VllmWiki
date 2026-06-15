# vllm-project/vllm#32105: [Bug]:Pipeline parallelism cannot share kvcache across different GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#32105](https://github.com/vllm-project/vllm/issues/32105) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;moe;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:Pipeline parallelism cannot share kvcache across different GPUs

### Issue 正文摘录

### Your current environment vllm commit 2a4dbe24eadcb8e0354e47f608b53399aec52c4 nvidia rtx4090 ### 🐛 Describe the bug Is this a bug? command ```bash vllm serve Qwen/Qwen3-VL-30B-A3B-Thinking-FP8 --pipeline-parallel-size=3 --gpu-memory-utilization=0.97 ``` eCore_DP0 pid=3258054) vllm_config, kv_cache_specs, available_gpu_memory (EngineCore_DP0 pid=3258054) ) (EngineCore_DP0 pid=3258054) File "/home/iboc/vllm/.venv/lib/python3.13/site-packages/vllm/v1/core/kv_cache_utils.py", line 1514, in get_kv_cache_configs (EngineCore_DP0 pid=3258054) _check_enough_kv_cache_memory( (EngineCore_DP0 pid=3258054) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^ (EngineCore_DP0 pid=3258054) min(available_memory), (EngineCore_DP0 pid=3258054) ^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=3258054) ... ... (EngineCore_DP0 pid=3258054) ), (EngineCore_DP0 pid=3258054) ^^ (EngineCore_DP0 pid=3258054) ) (EngineCore_DP0 pid=3258054) ^ (EngineCore_DP0 pid=3258054) File "/home/iboc/vllm/.venv/lib/python3.13/site-packages/vllm/v1/core/kv_cache_utils.py", line 634, in _check_enough_kv_cache_memory (EngineCore_DP0 pid=3258054) raise ValueError( (EngineCore_DP0 pid=3258054) ... ... (EngineCore_DP0 pid=3258054) ) (EngineCore_DP0 pid=...

## 现有链接修复摘要

#33698 [Core][BugFix] Fix PP KV cache sharding memory validation

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]:Pipeline parallelism cannot share kvcache across different GPUs bug ### Your current environment vllm commit 2a4dbe24eadcb8e0354e47f608b53399aec52c4 nvidia rtx4090 ### 🐛 Describe the bug Is this a bug? command ```...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. performance attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory attention;cache;cuda;fp8;kernel;moe;quantization;triton...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Is this a bug? command ```bash vllm serve Qwen/Qwen3-VL-30B-A3B-Thinking-FP8 --pipeline-parallel-size=3 --gpu-memory-utilization=0.97 ``` eCore_DP0 pid=3258054) vllm_config, kv_cache_specs, available_gpu_memory (EngineC...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: x4090 ### 🐛 Describe the bug Is this a bug? command ```bash vllm serve Qwen/Qwen3-VL-30B-A3B-Thinking-FP8 --pipeline-parallel-size=3 --gpu-memory-utilization=0.97 ``` eCore_DP0 pid=3258054) vllm_config, kv_cache_specs,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 54) ) (EngineCore_DP0 pid=3258054) ValueError: To serve at least one request with the models's max seq len (262144), (24.0 GiB KV cache is needed, which is larger than the available KV cache memory (9.05 GiB). Based on...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#33698](https://github.com/vllm-project/vllm/pull/33698) | closes_keyword | 0.95 | [Core][BugFix] Fix PP KV cache sharding memory validation | Fixes #32105. Refs #32782. Regression introduced by #29431 (commit 8ee90c8). This PR fixes incorrect KV cache sharding memory validation under Pipeline Parallelism, which could ca |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
