# vllm-project/vllm#41287: [Bug]: V1 + Ray multi-node pipeline parallel `KeyError` at KV-cache init due to missing `global_rank` update

| 字段 | 值 |
| --- | --- |
| Issue | [#41287](https://github.com/vllm-project/vllm/issues/41287) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: V1 + Ray multi-node pipeline parallel `KeyError` at KV-cache init due to missing `global_rank` update

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `vllm serve` with multi-node pipeline parallelism on V1 + Ray fails deterministically during KV-cache initialization with `KeyError 'model.layers. .self_attn.attn'`, where `N` is the first layer of some other pipeline parallel shard: ```none ray.exceptions.RayTaskError(KeyError): ray::RayWorkerWrapper.execute_method() (...) File ".../vllm/v1/worker/gpu_worker.py", line 536, in initialize_from_config self.model_runner.initialize_kv_cache(kv_cache_config) File ".../vllm/v1/worker/gpu_model_runner.py", line 6781, in initialize_kv_cache self.initialize_attn_backend(kv_cache_config) File ".../vllm/v1/worker/gpu_model_runner.py", line 6204, in initialize_attn_backend attn_backends = get_attn_backends_for_group(kv_cache_group_spec) File ".../vllm/v1/worker/gpu_model_runner.py", line 6163, in get_attn_backends_for_group attn_backend = layers[layer_name].get_attn_backend() ~~~~~~^^^^^^^^^^^^ KeyError: 'model.layers.21.self_attn.attn' ``` Each pipeline parallel rank ends up using another shard's projected KV-cache config, so when `gpu_model_runner.initialize_attn_backend` iterates `kv_cache_group_spec.layer_names` against the worker-local...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: y fails deterministically during KV-cache initialization with `KeyError 'model.layers. .self_attn.attn'`, where `N` is the first layer of some other pipeline parallel shard: ```none ray.exceptions.RayTaskError(KeyError)...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: he order the engine core built that list. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding cuda;o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ### 🐛 Describe the bug `vllm serve` with multi-node pipeline parallelism on V1 + Ray fails deterministically during KV-cache initialization with `KeyError 'model.layers. .self_attn.attn'`, where `N` is the first layer o...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: l_runner.py", line 6781, in initialize_kv_cache self.initialize_attn_backend(kv_cache_config) File ".../vllm/v1/worker/gpu_model_runner.py", line 6204, in initialize_attn_backend attn_backends = get_attn_backends_for_gr...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: bug `vllm serve` with multi-node pipeline parallelism on V1 + Ray fails deterministically during KV-cache initialization with `KeyError 'model.layers. .self_attn.attn'`, where `N` is the first layer of some other pipeli...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
