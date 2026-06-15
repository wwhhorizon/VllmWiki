# vllm-project/vllm#25029: [Bug]: KeyError: 'layers.35.mlp.gate.g_idx' of qwen3-30b-a3b gptq int4 in v0.10.2

| 字段 | 值 |
| --- | --- |
| Issue | [#25029](https://github.com/vllm-project/vllm/issues/25029) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | install |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling |
| 症状 | build_error;crash;import_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KeyError: 'layers.35.mlp.gate.g_idx' of qwen3-30b-a3b gptq int4 in v0.10.2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The docker image of vllm-v0.10.2 failed to load the qwen3-30b-a3b gptq int4. But the docker image of vllm-v0.10.1.1 can success. ``` /usr/local/lib/python3.12/dist-packages/torch/cuda/__init__.py:63: FutureWarning: The pynvml package is deprecated. Please install nvidia-ml-py instead. If you did not install pynvml directly, please report this to the maintainers of the package that installed pynvml for you. import pynvml # type: ignore[import] INFO 09-16 20:56:28 [__init__.py:216] Automatically detected platform cuda. (APIServer pid=1) INFO 09-16 20:56:30 [api_server.py:1896] vLLM API server version 0.10.2 (APIServer pid=1) INFO 09-16 20:56:30 [utils.py:328] non-default args: {'host': '0.0.0.0', 'model': '/data/model', 'trust_remote_code': True, 'max_model_len': 8192, 'served_model_name': ['zoe-gpt'], 'gpu_memory_utilization': 0.48, 'max_num_batched_tokens': 20960, 'max_num_seqs': 200} (APIServer pid=1) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. (APIServer pid=1) INFO 09-16 20:56:38 [__init__.py:742] Resolved architecture: Qwen3MoeForCausalLM (APIServer pid=1) `torch_dty...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: v0.10.2 bug ### Your current environment ### 🐛 Describe the bug The docker image of vllm-v0.10.2 failed to load the qwen3-30b-a3b gptq int4. But the docker image of vllm-v0.10.1.1 can success. ``` /usr/local/lib/python3...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: KeyError: 'layers.35.mlp.gate.g_idx' of qwen3-30b-a3b gptq int4 in v0.10.2 bug ### Your current environment ### 🐛 Describe the bug The docker image of vllm-v0.10.2 failed to load the qwen3-30b-a3b gptq int4. But...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: KeyError: 'layers.35.mlp.gate.g_idx' of qwen3-30b-a3b gptq int4 in v0.10.2 bug ### Your current environment ### 🐛 Describe the bug The docker image of vllm-v0.10.2 failed to load the qwen3-30b-a3b gptq int4. But...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: untime. Using gptq_marlin kernel. (APIServer pid=1) INFO 09-16 20:56:41 [scheduler.py:222] Chunked prefill is enabled with max_num_batched_tokens=20960. /usr/local/lib/python3.12/dist-packages/torch/cuda/__init__.py:63:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
