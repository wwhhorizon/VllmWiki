# vllm-project/vllm#25797: [Bug]: Qwen3-Next-80B-A3B-Instruct-AWQ-4bit KeyError: 'layers.45.mlp.shared_expert.down_proj.weight'

| 字段 | 值 |
| --- | --- |
| Issue | [#25797](https://github.com/vllm-project/vllm/issues/25797) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;operator;quantization;sampling |
| 症状 | crash;import_error;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Next-80B-A3B-Instruct-AWQ-4bit KeyError: 'layers.45.mlp.shared_expert.down_proj.weight'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` (vllm) root@xbnpc:~# VLLM_USE_MODELSCOPE=true vllm serve /ai/Qwen3-Next-80B-A3B-Instruct-AWQ-4bit \ --tensor-parallel-size 1 \ --> --tensor-parallel-size 1 \ > --gpu-memory-utilization 0.9 \ > --max-model-len 8192 \ > --dtype float16 INFO 09-27 11:31:35 [__init__.py:216] Automatically detected platform cuda. (APIServer pid=5963) INFO 09-27 11:31:37 [api_server.py:1896] vLLM API server version 0.10.2 (APIServer pid=5963) INFO 09-27 11:31:37 [utils.py:328] non-default args: {'model_tag': '/ai/Qwen3-Next-80B-A3B-Instruct-AWQ-4bit', 'model': '/ai/Qwen3-Next-80B-A3B-Instruct-AWQ-4bit', 'dtype': 'float16', 'max_model_len': 8192} (APIServer pid=5963) INFO 09-27 11:31:41 [__init__.py:742] Resolved architecture: Qwen3NextForCausalLM (APIServer pid=5963) `torch_dtype` is deprecated! Use `dtype` instead! (APIServer pid=5963) WARNING 09-27 11:31:41 [__init__.py:2767] Casting torch.bfloat16 to torch.float16. (APIServer pid=5963) INFO 09-27 11:31:41 [__init__.py:1815] Using max model len 8192 (APIServer pid=5963) WARNING 09-27 11:31:41 [_ipex_ops.py:16] Import error msg: No module named 'intel_extension_for_pytorch' (APIServer pid=5963) IN...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: erver pid=5963) INFO 09-27 11:31:37 [api_server.py:1896] vLLM API server version 0.10.2 (APIServer pid=5963) INFO 09-27 11:31:37 [utils.py:328] non-default args: {'model_tag': '/ai/Qwen3-Next-80B-A3B-Instruct-AWQ-4bit',...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ct-AWQ-4bit KeyError: 'layers.45.mlp.shared_expert.down_proj.weight' bug;stale ### Your current environment ### 🐛 Describe the bug ``` (vllm) root@xbnpc:~# VLLM_USE_MODELSCOPE=true vllm serve /ai/Qwen3-Next-80B-A3B-Inst...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: 1 \ > --gpu-memory-utilization 0.9 \ > --max-model-len 8192 \ > --dtype float16 INFO 09-27 11:31:35 [__init__.py:216] Automatically detected platform cuda. (APIServer pid=5963) INFO 09-27 11:31:37 [api_server.py:1896] v...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: PIServer pid=5963) INFO 09-27 11:31:41 [config.py:390] Setting attention block size to 544 tokens to ensure that attention page size is >= mamba page size. (APIServer pid=5963) INFO 09-27 11:31:41 [config.py:411] Paddin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
