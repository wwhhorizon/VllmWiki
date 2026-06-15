# vllm-project/vllm#22892: [Bug]: BGE Embedder not working with V1 Engine

| 字段 | 值 |
| --- | --- |
| Issue | [#22892](https://github.com/vllm-project/vllm/issues/22892) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: BGE Embedder not working with V1 Engine

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hey guys, I recently upgrade from V0 engine to V1 engine for my embedding server but I can't embed with V1 Engine for bge (bert based) model... Here is the error logging of it: ```text INFO 08-14 08:44:47 [__init__.py:241] Automatically detected platform cuda. WARNING 08-14 08:44:53 [__init__.py:1683] argument 'task' is deprecated (APIServer pid=43) INFO 08-14 08:44:53 [api_server.py:1787] vLLM API server version 0.10.2.dev2+gf5635d62e.d20250807 (APIServer pid=43) INFO 08-14 08:44:53 [utils.py:326] non-default args: {'model_tag': 'BAAI/bge-large-en-v1.5', 'host': '0.0.0.0', 'port': 30000, 'model': 'BAAI/bge-large-en-v1.5', 'task': 'embed', 'dtype': 'float32', 'max_model_len': 512, 'served_model_name': ['bge-embedding'], 'hf_token': '***', 'override_pooler_config': {'pooling_type': 'MEAN', 'normalize': True}, 'gpu_memory_utilization': 0.125, 'max_num_seqs': 32} (APIServer pid=43) INFO 08-14 08:44:54 [config.py:663] Found sentence-transformers tokenize configuration. (APIServer pid=43) INFO 08-14 08:45:01 [config.py:726] Resolved architecture: BertModel (APIServer pid=43) INFO 08-14 08:45:01 [config.py:561] Found sentence-transform...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: IServer pid=43) INFO 08-14 08:44:53 [api_server.py:1787] vLLM API server version 0.10.2.dev2+gf5635d62e.d20250807 (APIServer pid=43) INFO 08-14 08:44:53 [utils.py:326] non-default args: {'model_tag': 'BAAI/bge-large-en-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: y embedding server but I can't embed with V1 Engine for bge (bert based) model... Here is the error logging of it: ```text INFO 08-14 08:44:47 [__init__.py:241] Automatically detected platform cuda. WARNING 08-14 08:44:...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: rank 0, TP rank 0, EP rank 0 (EngineCore_0 pid=86) INFO 08-14 08:45:12 [topk_topp_sampler.py:49] Using FlashInfer for top-p & top-k sampling. (EngineCore_0 pid=86) INFO 08-14 08:45:12 [gpu_model_runner.py:1913] Starting...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: rver pid=43) INFO 08-14 08:45:01 [arg_utils.py:1609] (Disabling) chunked prefill by default (APIServer pid=43) INFO 08-14 08:45:01 [arg_utils.py:1612] (Disabling) prefix caching by default (APIServer pid=43) INFO 08-14...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
