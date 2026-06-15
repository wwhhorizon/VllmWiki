# vllm-project/vllm#16961: [Bug]: vllm 0.8.4 v1  startup time is too long when using lora

| 字段 | 值 |
| --- | --- |
| Issue | [#16961](https://github.com/vllm-project/vllm/issues/16961) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | activation;attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm 0.8.4 v1  startup time is too long when using lora

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In version 0.8.3 of VLLM, using the v1 engine to start multi lora model will hangs in the torch.compile step (This step can't be finished after waiting for more than half an hour). However, it can be loaded successful by using V0 engine. It is also successful to load a model with only one lora using V1 engine. start sh： ``` export VLLM_LOGGING_LEVEL=DEBUG vllm serve /data/models/Qwen2.5-14B-Instruct_fp8 \ --host 0.0.0.0 \ --port 23301 \ --enable-lora \ --max-lora-rank 64 \ --max-loras 3 \ --lora-modules ***1=***1 ***2=***2 ***2=***2 ``` log: ``` DEBUG 04-21 19:43:49 [__init__.py:28] No plugins for group vllm.platform_plugins found. DEBUG 04-21 19:43:49 [__init__.py:34] Checking if TPU platform is available. DEBUG 04-21 19:43:49 [__init__.py:44] TPU platform is not available because: No module named 'libtpu' DEBUG 04-21 19:43:49 [__init__.py:52] Checking if CUDA platform is available. DEBUG 04-21 19:43:49 [__init__.py:72] Confirmed CUDA platform is available. DEBUG 04-21 19:43:49 [__init__.py:100] Checking if ROCm platform is available. DEBUG 04-21 19:43:49 [__init__.py:114] ROCm platform is not available because: No module named...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: rt VLLM_LOGGING_LEVEL=DEBUG vllm serve /data/models/Qwen2.5-14B-Instruct_fp8 \ --host 0.0.0.0 \ --port 23301 \ --enable-lora \ --max-lora-rank 64 \ --max-loras 3 \ --lora-modules ***1=***1 ***2=***2 ***2=***2 ``` log: `...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ing lora bug ### Your current environment ### 🐛 Describe the bug In version 0.8.3 of VLLM, using the v1 engine to start multi lora model will hangs in the torch.compile step (This step can't be finished after waiting fo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: e bug In version 0.8.3 of VLLM, using the v1 engine to start multi lora model will hangs in the torch.compile step (This step can't be finished after waiting for more than half an hour). However, it can be loaded succes...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: will hangs in the torch.compile step (This step can't be finished after waiting for more than half an hour). However, it can be loaded successful by using V0 engine. It is also successful to load a model with only one l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
