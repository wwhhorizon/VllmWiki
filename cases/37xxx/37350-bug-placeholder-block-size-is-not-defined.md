# vllm-project/vllm#37350: [Bug]: 'placeholder_block_size' is not defined

| 字段 | 值 |
| --- | --- |
| Issue | [#37350](https://github.com/vllm-project/vllm/issues/37350) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 'placeholder_block_size' is not defined

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Error msg: ``` (EngineCore pid=207) DEBUG 03-17 22:55:01 [model_executor/models/qwen3_next.py:776] GDN prefill kernel warmup (T=64) completed for layer language_model.model.layers.38.linear_attn (EngineCore pid=207) INFO 03-17 22:55:01 [compilation/monitor.py:76] Initial profiling/warmup run took 158.40 s (APIServer pid=1) DEBUG 03-17 22:55:05 [v1/engine/utils.py:1021] Waiting for 1 local, 0 remote core engine proc(s) to start. (APIServer pid=1) DEBUG 03-17 22:55:15 [v1/engine/utils.py:1021] Waiting for 1 local, 0 remote core engine proc(s) to start. (EngineCore pid=207) INFO 03-17 22:55:16 [v1/core/kv_cache_utils.py:826] Overriding num_gpu_blocks=0 with num_gpu_blocks_override=512 (EngineCore pid=207) ERROR 03-17 22:55:16 [v1/engine/core.py:1099] EngineCore failed to start. (EngineCore pid=207) ERROR 03-17 22:55:16 [v1/engine/core.py:1099] Traceback (most recent call last): (EngineCore pid=207) ERROR 03-17 22:55:16 [v1/engine/core.py:1099] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 1073, in run_engine_core (EngineCore pid=207) ERROR 03-17 22:55:16 [v1/engine/core.py:1099] engine_core = EngineCore...

## 现有链接修复摘要

#37389 Fix placeholder_block_size undefined error in initialize_kv_cache

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ne/core.py:1099] File "/usr/local/lib/python3.12/dist-packages/vllm/tracing/otel.py", line 178, in sync_wrapper (EngineCore pid=207) ERROR 03-17 22:55:16 [v1/engine/core.py:1099] return func(*args, **kwargs) (EngineCore...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: cribe the bug Error msg: ``` (EngineCore pid=207) DEBUG 03-17 22:55:01 [model_executor/models/qwen3_next.py:776] GDN prefill kernel warmup (T=64) completed for layer language_model.model.layers.38.linear_attn (EngineCor...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 8080:8000 --ipc=host vllm/vllm-openai --model Qwen/Qwen3.5-35B-A3B-GPTQ-Int4 --dtype auto --api-key token-coiano --cpu-offload-gb 56 --gpu-memory-utilization 0.97 --tensor-parallel-size 1 ``` ### Before submitting a new...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: =207) DEBUG 03-17 22:55:01 [model_executor/models/qwen3_next.py:776] GDN prefill kernel warmup (T=64) completed for layer language_model.model.layers.38.linear_attn (EngineCore pid=207) INFO 03-17 22:55:01 [compilation/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ineCore pid=207) INFO 03-17 22:55:01 [compilation/monitor.py:76] Initial profiling/warmup run took 158.40 s (APIServer pid=1) DEBUG 03-17 22:55:05 [v1/engine/utils.py:1021] Waiting for 1 local, 0 remote core engine proc...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37389](https://github.com/vllm-project/vllm/pull/37389) | closes_keyword | 0.95 | Fix placeholder_block_size undefined error in initialize_kv_cache | Fix for issue #37350: NameError when initializing KV cache for CUDA graph profiling. The issue occurs when _init_minimal_kv_cache_for_profiling calls initialize_kv_cache, which re |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
