# vllm-project/vllm#25502: [Bug]: This flash attention build does not support tanh softcapping: gemma-2-2b-it on H100 NVL

| 字段 | 值 |
| --- | --- |
| Issue | [#25502](https://github.com/vllm-project/vllm/issues/25502) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: This flash attention build does not support tanh softcapping: gemma-2-2b-it on H100 NVL

### Issue 正文摘录

### Your current environment Trying to run gemma-2-2b-it/gemma-2-9b-it on vLLM v0.10.2 on Nvidia H100 NVL. The model loads up and the endpoint comes up but as soon as the inference request is made the server dies and throws the following error: `RuntimeError: This flash attention build does not support tanh softcapping.` ### 🐛 Describe the bug **Error logs:** ``` /usr/local/lib/python3.12/dist-packages/torch/cuda/__init__.py:63: FutureWarning: The pynvml package is deprecated. Please install nvidia-ml-py instead. If you did not install pynvml directly, please report this to the maintainers of the package that installed pynvml for you. import pynvml # type: ignore[import] INFO 09-23 10:47:00 [__init__.py:216] Automatically detected platform cuda. WARNING 09-23 10:47:02 [__init__.py:1758] argument '--disable-log-requests' is deprecated and replaced with '--enable-log-requests'. This will be removed in v0.12.0. (APIServer pid=1) INFO 09-23 10:47:02 [api_server.py:1896] vLLM API server version 0.10.2 (APIServer pid=1) INFO 09-23 10:47:02 [utils.py:328] non-default args: {'model': '/mnt/models', 'dtype': 'bfloat16', 'max_model_len': 4096, 'served_model_name': ['gemma-2-2b-it']} (APISer...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: This flash attention build does not support tanh softcapping: gemma-2-2b-it on H100 NVL bug;stale ### Your current environment Trying to run gemma-2-2b-it/gemma-2-9b-it on vLLM v0.10.2 on Nvidia H100 NVL. The mod...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: n build does not support tanh softcapping: gemma-2-2b-it on H100 NVL bug;stale ### Your current environment Trying to run gemma-2-2b-it/gemma-2-9b-it on vLLM v0.10.2 on Nvidia H100 NVL. The model loads up and the endpoi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: [Bug]: This flash attention build does not support tanh softcapping: gemma-2-2b-it on H100 NVL bug;stale ### Your current environment Trying to run gemma-2-2b-it/gemma-2-9b-it on vLLM v0.10.2 on Nvidia H100 NVL. The mod...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: 9-23 10:47:02 [utils.py:328] non-default args: {'model': '/mnt/models', 'dtype': 'bfloat16', 'max_model_len': 4096, 'served_model_name': ['gemma-2-2b-it']} (APIServer pid=1) INFO 09-23 10:47:08 [__init__.py:742] Resolve...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: This flash attention build does not support tanh softcapping: gemma-2-2b-it on H100 NVL bug;stale ### Your current environment Trying to run gemma-2-2b-it/gemma-2-9b-it on vLLM v0.10.2 on Nvidia H100 NVL. The mod...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
