# vllm-project/vllm#37261: [Bug]: KeyError when use lmcache layerwise mode in vllm 0.14.0

| 字段 | 值 |
| --- | --- |
| Issue | [#37261](https://github.com/vllm-project/vllm/issues/37261) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KeyError when use lmcache layerwise mode in vllm 0.14.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I use code below to start the server. ```sh LMCACHE_USE_LAYERWISE=True PYTHONHASHSEED=0 LMCACHE_CONFIG_FILE=lmcache_config.yaml CUDA_VISIBLE_DEVICES=0 vllm serve mistralai/Mistral-7B-Instruct-v0.2 --gpu-memory-utilization 0.8 --port 8000 --kv-transfer-config '{"kv_connector":"LMCacheConnectorV1", "kv_role":"kv_both"}' ``` The yaml file is ```yaml chunk_size: 16local_cpu: trueremote_url: "lm://localhost:8100"max_local_cpu_size: 20.0remote_serde: "naive" ``` and i use lmcache version is `0.4.1` After serveral requests ( about 500 requests each request about 4000 with input len avg in 16 batch size), i encounter an error ```sh (EngineCore_DP0 pid=17830) ERROR 03-17 14:38:51 [core.py:938] return forward_call(*args, **kwargs) (EngineCore_DP0 pid=17830) ERROR 03-17 14:38:51 [core.py:938] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=17830) ERROR 03-17 14:38:51 [core.py:938] File " .2", line 5, in forward (EngineCore_DP0 pid=17830) ERROR 03-17 14:38:51 [core.py:938] unified_attention_with_output = torch.ops.vllm.unified_attention_with_output(query_2, key_2, value, output_3, 'model.layers.0.self_attn.attn'); query_2 = key_2 = value =...

## 现有链接修复摘要

#37269 fix(lmcache): handle KeyError in layerwise storage mode | #37270 fix(lmcache): handle KeyError in layerwise mode

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: 8100"max_local_cpu_size: 20.0remote_serde: "naive" ``` and i use lmcache version is `0.4.1` After serveral requests ( about 500 requests each request about 4000 with input len avg in 16 batch size), i encounter an error...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: _serde: "naive" ``` and i use lmcache version is `0.4.1` After serveral requests ( about 500 requests each request about 4000 with input len avg in 16 batch size), i encounter an error ```sh (EngineCore_DP0 pid=17830) E...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: struct-v0.2', world_size=1, worker_id=0, chunk_hash=9190147360584713872, dtype=torch.bfloat16, request_configs=None, tags=None, _dtype_str='bfloat16', layer_id=0) (EngineCore_DP0 pid=17830) ERROR 03-17 14:38:51 [core.py...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: rt the server. ```sh LMCACHE_USE_LAYERWISE=True PYTHONHASHSEED=0 LMCACHE_CONFIG_FILE=lmcache_config.yaml CUDA_VISIBLE_DEVICES=0 vllm serve mistralai/Mistral-7B-Instruct-v0.2 --gpu-memory-utilization 0.8 --port 8000 --kv...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: :938] File "/usr/local/lib/python3.12/dist-packages/lmcache/v1/storage_backend/storage_manager.py", line 359, in batched_allocate (EngineCore_DP0 pid=17830) ERROR 03-17 14:38:51 [core.py:938] return self.allocator_backe...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37269](https://github.com/vllm-project/vllm/pull/37269) | closes_keyword | 0.95 | fix(lmcache): handle KeyError in layerwise storage mode | Fixes #37261 |
| [#37270](https://github.com/vllm-project/vllm/pull/37270) | closes_keyword | 0.95 | fix(lmcache): handle KeyError in layerwise mode | Fixes #37261 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
