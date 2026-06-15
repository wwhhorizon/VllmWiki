# vllm-project/vllm#31683: [Feature]: Error Logging Redesign

| 字段 | 值 |
| --- | --- |
| Issue | [#31683](https://github.com/vllm-project/vllm/issues/31683) |
| 状态 | open |
| 标签 | help wanted;feature request |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;gemm_linear;model_support;moe;quantization;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | attention;cuda;fp8;kernel;moe;operator;quantization |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Error Logging Redesign

### Issue 正文摘录

### 🚀 The feature, motivation and pitch vLLM has a multiprocess architecture with: - API Server --> EngineCore --> [N] Workers As a result, clean error message logging is challenging, since the error in the API server that occurs will often not be the root cause error. An example of this is at startup time: ``` (vllm) [robertgshaw2-redhat@nm-automation-h100-standalone-1-preserve vllm]$ just launch_cutlass_tensor VLLM_USE_DEEP_GEMM=0 VLLM_USE_FLASHINFER_MOE_FP8=1 VLLM_FLASHINFER_MOE_BACKEND=throughput chg run --gpus 2 -- vllm serve amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV -tp 2 --port 8002 --max-model-len 8192 Reserved 2 GPU(s): [1 3] for command execution (APIServer pid=116718) INFO 01-04 14:48:03 [api_server.py:1277] vLLM API server version 0.13.0rc2.dev185+g00a8d7628 (APIServer pid=116718) INFO 01-04 14:48:03 [utils.py:253] non-default args: {'model_tag': 'amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV', 'port': 8002, 'model': 'amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV', 'max_model_len': 8192, 'tensor_parallel_size': 2} (APIServer pid=116718) INFO 01-04 14:48:04 [model.py:522] Resolved architecture: MixtralForCausalLM (APIServer pid=116718) INFO 01-04 14:48:04 [model.py:1510] Using max model le...

## 现有链接修复摘要

#37757 [UX] Logging - Improve Startup Error Logs

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 7: shaw2-redhat@nm-automation-h100-standalone-1-preserve vllm]$ just launch_cutlass_tensor VLLM_USE_DEEP_GEMM=0 VLLM_USE_FLASHINFER_MOE_FP8=1 VLLM_FLASHINFER_MOE_BACKEND=throughput chg run --gpus 2 -- vllm serve amd/Mixtra...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: just launch_cutlass_tensor VLLM_USE_DEEP_GEMM=0 VLLM_USE_FLASHINFER_MOE_FP8=1 VLLM_FLASHINFER_MOE_BACKEND=throughput chg run --gpus 2 -- vllm serve amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV -tp 2 --port 8002 --max-model-len...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ver pid=116718) INFO 01-04 14:48:03 [api_server.py:1277] vLLM API server version 0.13.0rc2.dev185+g00a8d7628 (APIServer pid=116718) INFO 01-04 14:48:03 [utils.py:253] non-default args: {'model_tag': 'amd/Mixtral-8x7B-In...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Feature]: Error Logging Redesign help wanted;feature request ### 🚀 The feature, motivation and pitch vLLM has a multiprocess architecture with: - API Server --> EngineCore --> [N] Workers As a result, clean error messa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: request ### 🚀 The feature, motivation and pitch vLLM has a multiprocess architecture with: - API Server --> EngineCore --> [N] Workers As a result, clean error message logging is challenging, since the error in the API...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37757](https://github.com/vllm-project/vllm/pull/37757) | closes_keyword | 0.95 | [UX] Logging - Improve Startup Error Logs | Fixes #31683. Also addresses #37714. ## Summary This PR scopes #31683 to startup failures only, matching the guidance in the issue thread. - propagate structured startup fai |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
